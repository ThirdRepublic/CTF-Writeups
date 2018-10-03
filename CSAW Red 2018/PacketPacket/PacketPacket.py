#!/usr/bin/env python

import urllib 

url = "f+l+a+g+%7B+t+h+i+s+_+i+s+_+a+_+t+e+s+t+_+f+l+a+g+_+t+h+e+r+e+s+_+a+_+l+o+t+_+g+o+i+n+g+_+o+n+_+h+e+r+e+%7D+%0A"
input =  urllib.unquote(url).decode('utf8')
print input.replace("+","")