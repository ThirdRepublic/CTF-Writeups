#!/usr/bin/env python

# fmcj aj rzxn mpxc knwxabb
c1 = "fmcj"
c2 = "aj"
c3 = "rzxn"
c4 = "mpxc"
c5 = "knwxabb"

alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

def test(cipher):
	print "CipherText: " + cipher + "~~~~~~~~~~~~~~~~~~~~~~"
	start = 0
	while start < 26:
		print alpha[start:start+len(cipher)] + ":            " + decode(cipher,alpha[start:start+len(cipher)])
		start+=1 
	
def decode(cipher,key):
	output = ""
	for x in range(len(cipher)):
		diff = abs(ord(cipher[x])-97) - abs(ord(key[x])-97)
		output += chr(diff%26 + 97)
	return output

def findKey(plainText,cipherText):
	print "CipherText: " + cipherText + "~~~~~~~~~~~~~~~~~~~~~~"
	output = ""
	for x in range(len(plainText)):
		for y in range(26): 
			asciiCode = ord(plainText[x])-97+y
			asciiChr = chr(asciiCode%26 + 97)
			if asciiChr == cipherText[x]: 
				output += alpha[y]
	print output + ":            " + plainText

# key:           plainText
	
findKey("flag",c1)			
# abcd:            flag **GOOD**

test(c2)
# ef:            we ?
# uv:            go ?

test(c3)
# klmn:            hola ?

test(c4)
# none ??????                

test(c5)
# stuvwxy:            succeed  **GOOD**

# c3 is not correct
# break up ciphertext further 

test(c3[:2])
# kl:            ho 

test(c3[2:]) 
# ij:            pe

#kl ij:           ho pe  **GOOD**

# c2:             we  **GOOD**

test(c4[:2]) 
# op:            ya

test(c4[2:])        # ?
#guessing yall
