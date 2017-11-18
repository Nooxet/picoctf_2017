#!/usr/bin/python3

import sys

def bin2ascii(s):
    arr = [s[i*8:i*8+8] for i in range(len(s) // 8)]
    return ''.join(chr(int(i, 2)) for i in arr)

def ascii2hex(s):
    return ''.join(hex(ord(i))[2:] for i in s)

def xmodn(x, n):
    return ''.join('1' for i in range(x))

inp = sys.argv[1]

asc = bin2ascii(inp)
print (asc)
hx = ascii2hex(asc)
print (hx)
print (int(hx, 16))
print (xmodn(10, 16))
