import requests

r = requests. get(' https : I /www . baidu . com/’ )
print(type(r))
print(r. status_ code)
print (type(r. text))
print(r. text)
print(r.cookies) 
