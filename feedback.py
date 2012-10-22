#!/usr/bin/env python

import struct
from binascii import a2b_hex, b2a_hex
import socket
import ssl
import time
import sys

fmt = '!IH32s'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('feedback.push.apple.com', 2196))
ssl = ssl.wrap_socket(s, 'push.key', 'push.cert', ssl_version=3, cert_reqs=ssl.CERT_NONE)

data = ssl.read(struct.calcsize(fmt))

if not data:
  print 'no data'
  sys.exit(0)

while data:
  timestamp, length, token = struct.unpack(fmt, data)
  print 'got token: %s' % b2a_hex(token)
  data = ssl.read(struct.calcsize(fmt))
