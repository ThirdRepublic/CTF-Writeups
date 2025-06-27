#!/usr/bin/env python3
import hashlib

Curr="" # Current string
isSecondLine=0 # Skipping lines

# Open the file in read mode
with open('../puzzle.txt', 'r') as file:
	# Loop through each line in the file
	for line in file:
		# An empty string contains no characters, so it contains no Unicode code point (md5 of empty string)
		if isSecondLine<1:
			isSecondLine+=1
			continue
		# print("Attempting checksum bruteforce: ", line.strip())  # Print the line, remove trailing whitespace
		# Loop through Unicode code points from U+0000 to U+10FFFF
		for code_point in range(0, 0x110000):  # U+0000 to U+10FFFF
			try:
				# Convert Unicode code point to a character
				char = chr(code_point)
				# Compute the MD5 hash of the character
				md5_hash = hashlib.md5((Curr+char).encode('utf-8')).hexdigest()
				# Print the character and its MD5 hash
				# print(f"U+{code_point:04X}: {char} -> {md5_hash}")
			except UnicodeEncodeError:
				# Skip characters that can't be encoded
				continue
			if md5_hash == line.strip(): # A match was found!
				Curr+=char # Append to the current output
				break
print(Curr)