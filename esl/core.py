from myhdl import block, always_seq, always_comb, instance, intbv, modbv, Signal, delay, enum, ResetSignal, always
import chacha20


# modbv regresses to intbv on every non augmented operation
# use function to work around that
# this generates a Verilog module for every call but all of them are NOOP
def uint32(x):
    return modbv(x, min=0, max=2**32)

@block
def q_round(ai, bi, ci, di, ao, bo, co, do):
    a = uint32(0)
    b = uint32(0)
    c = uint32(0)
    d = uint32(0)

    @always_comb
    def qround():
        # val necessary for some reason
        a = ai.val
        b = bi.val
        c = ci.val
        d = di.val

        a += b
        d ^= a
        # manual rotations because right shift is always arithmetic in myhdl
        # not using a function for that because of Verilog generation weirdness
        d = uint32(d[(32-16):] << 16 | d[32:(32-16)])

        c += d
        b ^= c
        b = uint32(b[(32-12):] << 12 | b[32:(32-12)])

        a += b
        d ^= a
        d = uint32(d[(32-8):] << 8 | d[32:(32-8)])

        c += d
        b ^= c
        b = uint32(b[(32-7):] << 7 | b[32:(32-7)])

        ao.next = a
        bo.next = b
        co.next = c
        do.next = d

    return qround



t_State = enum("WAITING", "CALCULATING")

@block
def core(data, done, output, start, clk, reset):
    qsin = [Signal(uint32(0)) for _ in range(4*4)]
    qsout = [Signal(uint32(0)) for _ in range(4*4)]
    qs = [q_round(* (qsin[i*4:(i+1)*4] + qsout[i*4:(i+1)*4])) for i in range(4)]
    internal = intbv(0, max = 2**512)
    i = intbv(0, max = 20) 


    # constants [0:4] of chacha20
    constlist = (1634760805, 857760878, 2036477234, 1797285236)
    constvec = intbv(0, max = 2**(32*4))

    for v in reversed(constlist):
        constvec <<= 32
        constvec |= v


    # indices for even and odd rounds 
    iterindex = (
        (0,4,8,12, 1,5,9,13, 2,6,10,14, 3,7,11,15),
        (0,5,10,15, 1,6,11,12, 2,7,8,13, 3,4,9,14)
    )

    @instance
    def logic():
        state = t_State.WAITING
        internal = intbv(0, min = 0, max = 2**512)
        i = intbv(0, min=0, max = 20) 

        while True:
            yield clk.posedge, reset.posedge
            if reset:
                state = t_State.WAITING
                i = intbv(0, min=0, max = 20)
                internal[:] = 0
                done.next = False
                output.next = 0

            if state == t_State.WAITING:
                if start:
                    i = intbv(0, min=0, max = 20)
                    

                    internal[:] = data << (32*4) | constvec
                    done.next = False
                    state = t_State.CALCULATING
                    # start computing right away
                    for v in zip(range(16), iterindex[i % 2]):
                        qsin[v[0]].next = modbv(internal[32*(v[1]+1):32*v[1]], max=2**32)

                    # Unfortuantely MyHDL is not able to expand above during
                    # conversion. This would be very useful functionality.

            elif state == t_State.CALCULATING:
                # pull output of current round that was started before
                for v in zip(range(16), iterindex[i % 2]):
                    internal[32*(v[1]+1):32*v[1]] = qsout[v[0]]

                if i == 20 - 1:
                    output.next = internal
                    state = t_State.WAITING
                    done.next = True
                else:
                    i += 1
                    # start the next round
                    for v in zip(range(16), iterindex[i % 2]):
                        qsin[v[0]].next = modbv(internal[32*(v[1]+1):32*v[1]], max=2**32)

    return logic, qs


        
