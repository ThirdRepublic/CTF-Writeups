#!/usr/bin/env python

import binascii

file = open("TheBigPicture.txt","r")
output = open("output.PNG", "wb")

for line in file:
	output.write(binascii.unhexlify(''.join(line.split())))