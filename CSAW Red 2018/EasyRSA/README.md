# EasyRSA
![Category Crypto](https://img.shields.io/badge/category-crypto-%23d98817.svg?longCache=true&style=popout)
![Score 50](https://img.shields.io/badge/score-50-brightgreen.svg?longCache=true&style=popout)
![126 solves](https://img.shields.io/badge/solves-126-%2317a2b8.svg?longCache=true&style=popout)

Write up By
**Robe Zhang** [ThirdRepublic](https://github.com/ThirdRepublic)

## Challenge Description
> Decrypt the message from these RSA values:

```
N = 6771554318063279431848312702694599935973610341134793457387179802502340410323800956250664791676927908216176954377514952594523181778019541527306915289382187

d = 3711713166116654516231852804048066183987365980813665339727476998417559154417292248328844545850669766064400494699780124631469902379473449927403374793877457

c = 2649742855208609235845145293813962935889320032224555958279459176413803529115896568523205268199338089322793362288745663650880219089218944837255286873757915
```

## Background Information
>> RSA, which is an abbreviation of the author's names (Rivest–Shamir–Adleman), is a cryptosystem which allows for asymmetric encryption. Asymmetric cryptosystems are alos commonly referred to as Public Key Cryptography where a public key is used to encrypt data and only a secret, private key can be used to decrypt the data. [Continue Reading](https://ctf101.org/cryptography/what-is-rsa/)

[Read More](https://www.di-mgt.com.au/rsa_alg.html)

## Solution
Decrypt the ciphertext using:
> m = c<sup>d</sup> mod N 

Here is some python to decrypt the ciphertext.
```
n = 6771554318063279431848312702694599935973610341134793457387179802502340410323800956250664791676927908216176954377514952594523181778019541527306915289382187
d = 3711713166116654516231852804048066183987365980813665339727476998417559154417292248328844545850669766064400494699780124631469902379473449927403374793877457
c = 2649742855208609235845145293813962935889320032224555958279459176413803529115896568523205268199338089322793362288745663650880219089218944837255286873757915

num = pow(c,d,n)
print hex(num)[2:-1].decode("hex")
```

[EasyRSA Script](EasyRSA.py)

## Flag
```
flag{R0n_Adi_&_Leo_wou1d_b3_pr0ud}
```