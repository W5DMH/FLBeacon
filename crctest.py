#! /usr/bin/env/ python3
import binascii
#print binascii.crc32("hello world")
maxcrc = 0xffff
def inverse_crc(data):
    crc = binascii.crc_hqx(data, 2) & maxcrc
    invcrc = maxcrc - crc
    return invcrc.to_bytes(2, 'big')

def check_crc(data):
    return binascii.crc_hqx(data, 2) & maxcrc == maxcrc    

#Test
somevar = b"this is a 25 char message:"
data = somevar
newdata = data + inverse_crc(data)
print(check_crc(newdata))
newdata2 = b'0x00' + newdata
print(check_crc(newdata2))
print(newdata)

