# LLVN
![Category Misc](https://img.shields.io/badge/category-misc-lightgrey.svg?longCache=true&style=popout)
![Score 200](https://img.shields.io/badge/score-200-yellow.svg?longCache=true&style=popout)
![47 solves](https://img.shields.io/badge/solves-47-%2317a2b8.svg?longCache=true&style=popout)

Write up By
**Robe Zhang** [ThirdRepublic](https://github.com/ThirdRepublic)

## Challenge Description
> Can You Follow Instructions?
```
nc misc.chal.csaw.io 10101
```

## Background Information
Here is a sample output when connecting to the server.
```
***************************************************************************
Your job is to write a simple program that executes instructions!
Each instruction is in the following format:
Value = op1 operand op2
A given Value stores the result of an instruction

Ex:
%0 = 0x158763 # All programs start this way setting %0 to a hex number
%1 = rshift %0, 67 #    %1 = %0 >> 67
%2 = sub %1, %0 #    %2 = %1 - %0
show %0 + %1 + %2#     You must submit the result of the show command

The show command is the output of the program
It is basically the sum of a subset of Values from the program

Since:
    %0 = 0x158763
    %1 = 0
    %2=-1410915
Show instruction outputs:   0
***************************************************************************
>%0 = 0x18
>%1 = xor %0, 5
>%2 = add %0, %0
>%3 = add %1, 7
>%4 = or %2, %2
>%5 = mult %3, 2
>%6 = or %5, %3
>%7 = xor %1, 1
>%8 = or %4, %2
>%9 = sub %7, 5
>%10 = xor %1, %0
>%11 = sub %4, 7
>%12 = or %9, %1
>%13 = or %6, 7
>%14 = mult %12, %13
>%15 = and %10, 4
>%16 = or %6, %10
>%17 = xor %4, 1
>%18 = mult %13, %15
>%19 = or %9, 1
>%20 = add %12, %12
>%21 = or %5, 5
>%22 = and %19, %3
>%23 = add %4, 2
>%24 = mult %14, %14
>show %8 + %14 + %10 + %3 + %1 + %17 + %24
What does the program output??:
***************************************************************************
```
The objective is to solve the the problem given a list of instructions. 
- *ADD*     Addition Operand 
- *AND*     Bitwise AND Operand
- *MULTI*   Multiplication Operand
- *OR*      Bitwise OR Operand
- *SUB*		Subtraction Operand
- *XOR*     Bitwise XOR Operand

[Read Python Syntax](https://www.programiz.com/python-programming/operators#bitwise_operators)

## Solution
I wrote a python script that parses through the output given by the server.  I performed the calculations for each instruction and stored the value in the respective index in the list.  The script calculates the correct answer and returns it back to the server.  This process occurred in a loop until the flag was obtained.  
[LLVN Script](LLVN.py)

## Flag
```
flag{SsA_Variables_ar3_the_c0olest_shiz}
```
