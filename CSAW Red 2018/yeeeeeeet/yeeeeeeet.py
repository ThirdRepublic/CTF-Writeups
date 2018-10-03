import base64

data = "HwkEEwIcABENOhwRHBE6DRwAESsAAAAAJhwAEQ06HBEcEToNHAARKwAAAAAmHAARDTocERwROg0cABErAAAAACYcABENOhwRHBE6DRwAESsAAAAAJhwAEQ06HBEcEToNHAARKwAAAAAmHAARDTocERwROg0cABEJ"
data = base64.b64decode(data)

def findKey(idx,aChr):
	for x in range(256): # brute forcing the power to Xor
		asciiCode = ord(data[idx]) # Converting to Ascii Code
		asciiChr = chr(asciiCode^x) # Xor and convert back to Ascii Character
		if asciiChr == aChr: 
			print "key[%d] = %s"%(idx,chr(x))
			
#known structure of flag -> flag{
			
# findKey(0,"f") 
# findKey(1,"l")
# findKey(2,"a")
# findKey(3,"g")
# findKey(4,"{")

key = "yeet"

def decode(key):
	output = ""
	keyIdx = 0
	for aChr in data:
		asciiCode = ord(aChr) # Converting to Ascii Code
		asciiChr = chr(asciiCode^ord(key[keyIdx])) # Xor and convert back to Ascii Character
		output += asciiChr
		keyIdx +=1
		if keyIdx >= len(key):
			keyIdx = 0
	print output
	
decode(key)