#!/usr/bin/env python

from pwn import *
host_address = 'misc.chal.csaw.io'
host_port = 10101

p = remote(host_address,host_port)

# list to hold all values 
values = [None] * 30

def seperateValue(instruction):
	# remove string before and including %
	# replace new line characters
	# seperate value and expression
	# output[0] = valueIndex, output[1] = expression 
	output = instruction[instruction.index("%")+1:].replace("\n","").split(" = ")
	# store value of solved expression in respective index
	values[int(output[0])] = doOperation(output[1])
	# print instruction.replace("\n","")
	# print values[int(output[0])]

def doOperation(expression):
	if "%" not in expression:
		return int(expression,16)
	value1 = int(getValue(expression.split(" ")[1].replace(",","")))
	value2 = int(getValue(expression.split(" ")[2].replace("\n","")))
	if "xor" in expression:
		return value1 ^ value2
	if "or" in expression:
		return value1 | value2
	if "mult" in expression:
		return value1 * value2
	if "and" in expression:
		return value1 & value2
	if "add" in expression:
		return value1 + value2
	if "sub" in expression:
		return value1 - value2
	
# strip % and return value
def getValue(input):
	if "%" in input:
		return values[int(input.replace("%",""))]
	return input

p.recvuntil("***************************************************************************")
p.recvuntil("***************************************************************************")

while True:
	data = p.recv()

	if "flag" in data:
		print data
		break
		
	data = data.split(">")
	data.pop(0)
	
	# clear
	values = [None] * 30
		
	for x in data:
		if "show" in x:
			# strip and split 
			numbers = x.split("\n")[0].replace(" ","").replace("show","").split("+")	
			sum = 0;
			for num in numbers:
				sum+=getValue(num)
			p.send(str(sum)+"\n")
		else:
			seperateValue(x)	