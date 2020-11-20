from socket import *

#
# Ethernet Frame:
# [
#   [ Destination address, 6 bytes ]
#   [ Source address, 6 bytes      ]
#   [ Ethertype, 2 bytes           ]
#   [ Payload, 40 to 1500 bytes    ]
#   [ 32 bit CRC chcksum, 4 bytes  ]
# ]
#

s = socket(AF_PACKET, SOCK_RAW)
s.bind(("en0", 0))
src_addr = "\x01\x02\x03\x04\x05\x06"
dst_addr = "\x00\x0c\x29\x78\x1b\xbd"
payload = ("["*30)+"PAYLOAD"+("]"*30)
checksum = "\x00\x00\x00\x00"
ethertype = "\x08\x01"
s.send(dst_addr+src_addr+ethertype+payload+checksum)

