#!/usr/bin/env python3
from cipher import AES
from sbox import SBox
import os

with open('flag', 'rb') as f:
    flag = f.read()

def menu():
    print('1. Encrypt message')
    print('2. Encrypt flag')
    print('3. Exit')
    print('> ', end='')

if __name__ == '__main__':
    key = os.urandom(16)
    sbox = SBox(4)
    
    sbox.print()
    print('fill blank yourself to complete SBox (hex)> ')
    sbox.set_blanks([int(x,16) for x in input().split()])
    
    print('This is final SBox')
    sbox.print()

    aes = AES(key, sbox)

    while True:
        menu()
        i = int(input())
        if i == 1:
            print('message> ', end='')
            msg = bytes.fromhex(input())
            print(f'enc> {aes.encrypt(msg).hex()}')
        elif i == 2:
            print(f'flag> {aes.encrypt(flag).hex()}')
        elif i == 3:
            break
        else:
            print('invalid')
            continue
