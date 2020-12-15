## myhld-chacha20

ChaCha20 is stream cipher based on Salsa20 which was designed by Daniel Bernstein.
It is one of the most used stream ciphers today.

The project is contained inside the `core.py` which contains the `q_round` block -
quarter round of ChaCha20 and the `core` block which is responsible for scheduling operations on
four `q_round` blocks and mixing data between `q_round` blocks.

The `core` exposes `data`, `start` and `reset` input signals (plus `clock`), and outputs
result of ChaCha20 ready to be XORed do encrypt or decrypt 64 bytes of data, along with
`done` signal when `output` is ready to be read.

The testbed is contained in `tb.py`. It tests both the whole core as well as the `q_round` block.
Results from random inputs into both blocks are compared against native python functions of both
quarter round and whole encryption.

----

Due to issues in MyHDL I was not able to get the conversion of whole core to work.
The primary cause seems to be inability to index any array or tuple within `for ... range` clause.
See comments in `core.py` for better explanation.

Other than that in the testbed the core works and computes ChaCha20 correctly.



