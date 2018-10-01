# In My Element
![Category Tutorial](https://img.shields.io/badge/category-tutorial-lightgrey.svg?longCache=true&style=popout)
![Score 10](https://img.shields.io/badge/score-10-brightgreen.svg?longCache=true&style=popout)
![243 solves](https://img.shields.io/badge/solves-243-%2317a2b8.svg?longCache=true&style=popout)

Write up By
**Robe Zhang** [ThirdRepublic](https://github.com/ThirdRepublic)

## Challenge Description
> There is a flag somewhere on this page. Can you find it?

## Solution
Use the Chrome broswer as your tool.  Look in source of the page by clicking F12.  Right click and *Expand Recursively* in elements.
Find a comment within the footer tag. 
![Screenshot](footer.PNG)  
<!--ZmxhZ3tuZXdfa3VuZ19mdV9rZW5ueX0=-->
Observe that the comment is base64 encoded.  Use https://www.asciitohex.com/ to decode it.

## Flag
```
flag{youtu.be/_RWWKFqv7EM}
```
