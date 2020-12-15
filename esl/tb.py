from myhdl import block, always_seq, always_comb, instance, intbv, modbv, Signal, delay, enum, ResetSignal, always

import random
random.seed(5)

import core
import chacha20

def rotate(v, c):
    return ((v << c) & 0xffffffff) | v >> (32 - c)

def quarter_round(x, a, b, c, d):
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 16)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 12)
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 8)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 7)

@block
def testbench_qr():

    a,b,c,d = [Signal(modbv(0, min=0,  max=2**32)) for _ in range(4)]
    ao,bo,co,do = [Signal(modbv(0, min=0, max=2**32)) for _ in range(4)]

    q1 = core.q_round(a, b, c, d, ao, bo, co, do)
    
    @instance
    def stimulus():
        for _ in range(100):
            calc = [random.randrange(2**32) for _ in range(4)]
            a.next, b.next, c.next, d.next = calc
            quarter_round(calc, 0,1,2,3)
            yield delay(10)
            print('Result: ' + ('%08X' * 4) % (a,b,c,d))
            print('Should: ' + ('%08X' * 4) % tuple(calc))
            assert(calc == [ao, bo, co, do])

    return q1, stimulus


def convert_qround():
    signals = [Signal(modbv(0, min=0,  max=2**32)) for _ in range(8)]
    q1 = core.q_round(*signals) 
    q1.convert(hdl='Verilog')


@block
def testbench_core():
    clock = Signal(bool(0))
    done = Signal(bool(0))
    data = Signal(intbv(0, max=2**((16-4)*32)))
    reset = ResetSignal(False, True, False)
    start = Signal(bool(0))
    output = Signal(intbv(0, max=2**512))
    
    dut = core.core(data, done, output, start, clock, reset)

    @always(delay(10))
    def clockgen():
        clock.next = not clock

    @instance
    def check():
        yield clock.negedge
        data.next = 0
        start.next = True
        yield clock.negedge
        start.next = False
        yield done.posedge
        print('Done')
        print('Result: %0128X' % output.val)
        target = ('%08X'*16) % tuple(reversed(chacha20.state([0] * 12)))
        print('Should: ' + target)

        assert('%0128X' % output.val == target) 

        yield clock.negedge
        data.next = 555
        start.next = True
        yield clock.negedge
        start.next = False
        yield done.posedge

        print('Done')
        print('Result: %0128X' % output.val)
        target = ('%08X'*16) % tuple(reversed(chacha20.state([555] + ([0] * 11))))
        print('Should: ' + target)

        assert('%0128X' % output.val == target) 
        for _ in range(30):
            rng = random.randrange(2**32)
            yield clock.negedge
            data.next = rng
            start.next = True
            yield clock.negedge
            start.next = False
            yield done.posedge

            print('Result: %0128X' % output.val)
            target = ('%08X'*16) % tuple(reversed(chacha20.state([rng] + ([0] * 11))))
            print('Should: ' + target)

            assert('%0128X' % output.val == target) 


    return dut, clockgen, check


def convert_core():
    clock = Signal(bool(0))
    done = Signal(bool(0))
    data = Signal(intbv(0, max=2**((16-4)*32)))
    reset = ResetSignal(False, True, False)
    start = Signal(bool(0))
    output = Signal(intbv(0, max=2**512))
    
    c = core.core(data, done, output, start, clock, reset)
    c.convert(hdl='Verilog')
    

print('Running core simulation')
tb = testbench_core()
tb.run_sim(duration=20000)
tb.quit_sim()
print('Done')
#convert_core()

print('Running qround simulation')
tb = testbench_qr()
tb.run_sim()
tb.quit_sim()
print('Done')
convert_qround()
