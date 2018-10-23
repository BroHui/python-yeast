#!/bin/python
# coding: utf-8

import math
import time

alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_'
length = 64
t_map = {}
seed = 0
i = 0
prev = None

for i in xrange(length):
    t_map[alphabet[i]] = i

def encode(num):
    encoded = ''
    while True:
        encoded = alphabet[int(num % length)] + encoded
        num = math.floor(num / length)
        # simulate do-while
        if not (num > 0):
            break
    return encoded

def decode(enc_str):
    decoded = 0
    for i in xrange(len(enc_str)):
        decoded = decoded * length + t_map[enc_str[i]]
    return decoded

def yeast():
    global prev, seed
    ts = int(time.time() * 1000)
    now = encode(ts)
    if now != prev:
        seed = 0
        prev = now
        return now
    else:
        r = now + '.' + encode(seed)
        seed += 1
        return r

if __name__ == '__main__':
    print yeast()
