import re
string= 'hello 12 hi 89. Howdy 34'
pattern= '\d+'
print("Using findall method")
result= re.findall(pattern,string)
print(result)

print("using re.split ")
result=re.split(pattern,string,1)
print(result)

print("using sub method")

str= 'abc 12\
    de 23\n f 45 6'
patrn = '\s+'
replace=''
nw_str= re.sub(patrn,replace,str)
print(nw_str)