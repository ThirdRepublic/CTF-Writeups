# Irregular Expressions
![Category Tutorial](https://img.shields.io/badge/category-tutorial-lightgrey.svg?longCache=true&style=popout)
![Score 10](https://img.shields.io/badge/score-10-brightgreen.svg?longCache=true&style=popout)
![230 solves](https://img.shields.io/badge/solves-230-%2317a2b8.svg?longCache=true&style=popout)

Write up By
**Robe Zhang** [ThirdRepublic](https://github.com/ThirdRepublic)

## Challenge Description
> Can you find the flag in one of these files? Ctrl-F may not be enough.

## Attached Files
- [hello.zip](hello.zip)

## Solution
Extract the hello.zip folder. Use your terminal and navigate to the hello folder directory.
Use the *grep* command to extract the flag from the folder.
```
grep -r 'Hello' -e 'flag{'  
```
The *-e* flag looks for a pattern. <br />
The *-r* flag recursively looks in all the file in the directory.

## Flag
```
flag{jus7_@_r3gul4r_flag}
```
