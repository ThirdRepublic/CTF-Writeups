# SQLIntro
![Category Web](https://img.shields.io/badge/category-web-%232fc4e5.svg?longCache=true&style=popout)
![Score 50](https://img.shields.io/badge/score-50-brightgreen.svg?longCache=true&style=popout)
![195 solves](https://img.shields.io/badge/solves-195-%2317a2b8.svg?longCache=true&style=popout)

Write up By
**Robe Zhang** [ThirdRepublic](https://github.com/ThirdRepublic)

## Challenge Description
> Can you log into the admin's account without knowing the password?
```
web.chal.csaw.io:10104
```

## Background Information
The objective of the challenge is to use SQL injection to extract data from the database.  
The usage of the **OR** statement allows for additional logic in the SQL query.  Appending **OR 1=1** to a SQL query will make it always true since 1=1. <br />
[Read More](https://www.w3schools.com/sql/sql_injection.asp) <br />
[SQLi Cheat Sheet](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/)

## Solution
The webpage was given. <br /> <br />
![screenshot](page.PNG) <br />

Username:
> admin

Password:
> ' OR 1=1 --&nbsp;    

**Note** **```  --  ```** is an inline comment.  This ignores the rest of the SQL query.

![screenshot](solution.PNG)
## Flag
```
flag{j00'V3_pa223d_w38_s3cUri7Y_101}
```
