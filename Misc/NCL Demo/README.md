# NCL Demo
![Category Misc](https://img.shields.io/badge/category-misc-lightgrey.svg?longCache=true&style=popout) <br />
https://ncl.cyberskyline.com/module/demo/demo/demo 

## Challenge Description
> Help the operations team understand how to use their DNS tools by analyzing output from DiG.

## Challenge Output
```
; <<>> DiG 9.9.5-3ubuntu0.15-Ubuntu <<>> @208.67.222.123 facebook.com ANY
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 22083
;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;facebook.com.			IN	ANY

;; ANSWER SECTION:
facebook.com.		26	IN	A	31.13.67.35
facebook.com.		59	IN	AAAA	2a03:2880:f12c:83:face:b00c:0:25de
facebook.com.		127159	IN	NS	a.ns.facebook.com.
facebook.com.		127159	IN	NS	b.ns.facebook.com.
facebook.com.		119	IN	SOA	a.ns.facebook.com. dns.facebook.com. 1500245863 7200 1800 604800 120
facebook.com.		63015	IN	TXT	"v=spf1 redirect=_spf.facebook.com"

;; Query time: 2 msec
;; SERVER: 208.67.222.123#53(208.67.222.123)
;; WHEN: Sun Jul 16 18:59:46 EDT 2017
;; MSG SIZE  rcvd: 206
```
## Solution
1. **What is the domain being queried?**
> facebook.com
2. **According to these results, what is the IPv4 address that can be used to reach the Facebook website?**
> 31.13.67.35
3. **What is the IP address of the DNS resolver that was used?**
> 208.67.222.123