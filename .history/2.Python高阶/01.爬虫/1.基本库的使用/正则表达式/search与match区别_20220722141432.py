#!/usr/bin/python3

import re

line = "Cats are smarter than dogs"

if matchObj := re.match(r'dogs', line, re.M | re.I):
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

if matchObj := re.search(r'dogs', line, re.M | re.I):
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

# 结果：
# No match!!
# search --> matchObj.group() :  dogs
