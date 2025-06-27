#!/usr/bin/env python3
import hashlib

Curr="" # Current string
isSecondLine=0 # Skipping lines

# Open the file in read mode
with open('puzzle3.txt', 'r') as file:
    # Loop through each line in the file
    for line in file:     
        # Skip the first line (md5sum & sha-1'flag' output) and the second line (sha3_256 of empty string)
        if isSecondLine<2:
            isSecondLine+=1
            continue
        # print("Attempting checksum bruteforce: ", line.strip())  # Print the line, remove trailing whitespace
        # Loop through Unicode code points from U+0000 to U+10FFFF
        for code_point in range(0, 0x110000):  # U+0000 to U+10FFFF
            try:
                # Convert Unicode code point to a character
                char = chr(code_point)
                # Compute the sha3-256 hash of the character
                sha3_256_hash = hashlib.sha3_256((Curr+char).encode('utf-8')).hexdigest()
                # Print the character and its sha3-256 hash
                # print(f"U+{code_point:04X}: {char} -> {sha3_256_hash}")
            except UnicodeEncodeError:
                # Skip characters that can't be encoded
                continue
            if sha3_256_hash == line.strip(): # A match was found!
                Curr+=char # Append to the current output
                break
print(Curr)