#!/usr/bin/env python

import base64

data = "HxUYHgIQJgwKHB0mDRYmChgAJgAcHA0mEAsWFxAaGBUVACYbDA0mFxYOJhANCiYbHBoWFBwmCRgLDSYWHyYUACYPFhoYGwwVGAsABA=="
data = base64.b64decode(data)

output = ""

for x in range(256): # brute forcing the power to Xor
	for aChr in data: # looping each char
		ordValue = ord(aChr) # Converting to Ascii Value 
		xor = ordValue^x # Xor
		output += chr(xor) # Convering back to char

	if "flag" in output:
		print x
		print output
	output = ""