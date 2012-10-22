#!/usr/bin/env python

import struct
from binascii import a2b_hex
import socket
import ssl
import time
import sys
import os

args = sys.argv[1:]
if len(args) == 0:
  print >>sys.stderr, 'Usage: %s <token> [<token> ...]' % sys.argv[0]
  print >>sys.stderr, 'Tokens should be 64-byte hex ascii push tokens'
  print >>sys.stderr, 'The working directory is scanned for the pem-formatted push.cert and push.key'
  sys.exit(1)

tokens = []
for token in sys.argv[1:]:
  if len(token) != 64:
    print >>sys.stderr, 'Token %s is not length 64' % token
    sys.exit(1)

  try:
    bin_token = a2b_hex(token)
  except TypeError:
    print >>sys.stderr, 'Could not parse token %s' % token
    sys.exit(1)
  tokens.append(bin_token)

PUSH_KEY = 'push.key'
PUSH_CERT = 'push.cert'

if not os.path.exists(PUSH_KEY):
  print >>sys.stderr, 'Missing key file %s' % PUSH_KEY
  sys.exit(1)

if not os.path.exists(PUSH_CERT):
  print >>sys.stderr, 'Missing cert file %s' % PUSH_CERT
  sys.exit(1)

payload = '{"aps":{"alert":"Broadcasting direct to apple with p12"}}'
fmt = '!BH32sH%ds' % len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('gateway.push.apple.com', 2195))
ssl = ssl.wrap_socket(s, 'push.key', 'push.cert', ssl_version=3, cert_reqs=ssl.CERT_NONE)
for token in tokens:
  packet = struct.pack(fmt, 0, 32, token, len(payload), payload)
  count = ssl.write(packet)
  print 'wrote %d bytes' % count

