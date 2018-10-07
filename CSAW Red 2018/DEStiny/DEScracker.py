from Crypto.Cipher import DES

# https://en.wikipedia.org/wiki/Weak_key
# http://www.umich.edu/~x509/ssleay/des-weak.html

weakKeys = ["FEFEFEFEFEFEFEFE","FFFFFFFFFFFFFFFF","1F1F1F1F0E0E0E0E","E0E0E0E0F1F1F1F1",
"E1E1E1E1F0F0F0F0","0000000000000000","0101010101010101","0101010101010101","fefefefefefefefe","1f1f1f1f1f1f1f1f","e0e0e0e0e0e0e0e0","01fe01fe01fe01fe","fe01fe01fe01fe01","1fe01fe01fe01fe0","e01fe01fe01fe01f","01e001e001e001e0","e001e001e001e001","1ffe1ffe1ffe1ffe","fe1ffe1ffe1ffe1f","011f011f011f011f","1f011f011f011f01","e0fee0fee0fee0fe","fee0fee0fee0fee0","1f1f01010e0e0101","e00101e0f10101f1","011f1f01010e0e01","fe1f01e0fe0e01f1","1f01011f0e01010e","fe011fe0fe010ef1","01011f1f01010e0e","e01f1fe0f10e0ef1","fe0101fefe0101fe","e0e00101f1f10101","e01f01fef10e01fe","fefe0101fefe0101","e0011ffef1010efe","fee01f01fef10e01","fe1f1ffefe0e0efe","e0fe1f01f1fe0e01","fee0011ffef1010e","1ffe01e00efe01f1","e0fe011ff1fe010e","01fe1fe001fe0ef1","e0e01f1ff1f10e0e","1fe001fe0ef101fe","fefe1f1ffefe0e0e","01e01ffe01f10efe","fe1fe001fe0ef101","0101e0e00101f1f1","e01ffe01f10efe01","1f1fe0e00e0ef1f1","fe01e01ffe01f10e","1f01fee00e0ef1f1","e001fe1ff101fe0e","011ffee0010efef1","1f01e0fe0e01f1fe","01e0e00101e1e101","011fe0fe010ef1fe","1ffee0010efef001","0101fefe0101fefe","1ffee0010ef1fe01","1f1ffefe0e0efefe","01fefe0101fefe01","1fe0e0f10ef1f10e","fefee0e0fefef1f1","01fee01f01fef10e","e0fefee0f1fefef1","01e0fe1f01f1fe0e","fee0e0fefef1f1fe","1ffefe1f0efefe0e","e0e0fefef1f1fefe"
]

iv = '66642069'
file = 'destiny.enc'

ciphertext = ""
with open(file,'rb') as f:
    for line in f.readlines():
        ciphertext += line

ciphertext = ciphertext.replace(iv,"")		
		
for x in weakKeys:
	key = x.decode("hex")
	cipher = DES.new(key, DES.MODE_OFB, iv)
	ans = cipher.decrypt(ciphertext)
	if "flag" in ans:
		print x
		print ans