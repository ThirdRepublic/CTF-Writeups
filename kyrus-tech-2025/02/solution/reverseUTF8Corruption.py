#!/usr/bin/env python3

import base64

with open("challenge_zlib.decompress", "r") as f:
    b64_data = f.read()
    decoded_base64 = base64.b64decode(b64_data)

    decoded_utf8 = decoded_base64.decode('utf-8')
    encoded_latin1 = decoded_utf8.encode('Latin-1')

    with open("challenge_gzip.fixed", "wb") as f: # fixed Gzip file format
        f.write(encoded_latin1)