#!/usr/bin/env python3

with open("challenge_gzip.decompress", "rb") as f:
    blob = f.read()
    for key in range(256):
        # brute force XOR
        xorBlob = bytes(b ^ key for b in blob)
        try:
            decoded = xorBlob.decode("utf-8")
            if "flag" in decoded.lower() or "ctf" in decoded.lower():
                print (key ," : ", decoded, "\n") # Found Flag
        except Exception:
            continue