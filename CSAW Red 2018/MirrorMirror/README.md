# MirrorMirror
![Category Forensics](https://img.shields.io/badge/category-forensics-%23968af0.svg?longCache=true&style=popout)
![Score 50](https://img.shields.io/badge/score-50-brightgreen.svg?longCache=true&style=popout)
![182 solves](https://img.shields.io/badge/solves-182-%2317a2b8.svg?longCache=true&style=popout)

Write up By
**Robe Zhang** [ThirdRepublic](https://github.com/ThirdRepublic)

## Challenge Description
> Who's the fairest?
NOTE: You do NOT need nmap for this challenge
```
128.238.66.246
```

## Solution
An IP address is given.  What can you do with an IP address? <br />
Using [Nmap](https://nmap.org/)
> nmap 128.238.66.246

![screenshot](nmap.PNG) <br />

Using [nslookup](https://en.wikipedia.org/wiki/Nslookup) 
> nslookup 128.238.66.246

![screenshot](nslookup.PNG) <br />

Accessing http://reverse.reverse.nowtakeitbacknowyall.red.csaw.io/ yields the flag <br />
![screenshot](solution.PNG) <br />

## Flag
```
flag{awww_yeah_now_everybody_clap_your_hands}
```
