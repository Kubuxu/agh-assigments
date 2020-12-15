#! /usr/bin/python
# by pts@fazekas.hu at Thu May 24 18:44:15 CEST 2018

"""Pure Python 2 implementation of the ChaCha20 stream cipher.

It works with Python 2.4, 2.5, 2.6 and 2.7.

Based on https://gist.github.com/cathalgarvey/0ce7dbae2aa9e3984adc
Based on Numpy implementation: https://gist.github.com/chiiph/6855750
Based on http://cr.yp.to/chacha.html

More info about ChaCha20: https://en.wikipedia.org/wiki/Salsa20
"""

import struct

def state(data):
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

  ctx = [0] * 16
  ctx[:4] = (1634760805, 857760878, 2036477234, 1797285236)
  ctx[4:16] = data

  x = list(ctx)
  for i in xrange(10):
    quarter_round(x, 0, 4,  8, 12)
    quarter_round(x, 1, 5,  9, 13)
    quarter_round(x, 2, 6, 10, 14)
    quarter_round(x, 3, 7, 11, 15)
    quarter_round(x, 0, 5, 10, 15)
    quarter_round(x, 1, 6, 11, 12)
    quarter_round(x, 2, 7,  8, 13)
    quarter_round(x, 3, 4,  9, 14)

  return x
