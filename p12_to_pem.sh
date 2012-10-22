#!/bin/bash

[ -n "$1" ] || { echo "Usage: $0 [p12]"; exit 1; }

echo -n "Enter export password: "
read password

openssl pkcs12 -in "$1" -nodes  -nocerts -password "pass:$password" -out push.key
openssl pkcs12 -in "$1" -nodes  -nokeys -password "pass:$password" -out push.cert
