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


str1='abc 12\
de 23 \n f45 6'
patrn1='\s+'

replace=''
nw_str1= re.subn(patrn1,replace,str1)
print(nw_str1)




print("re.search")

str2='python is fun'

match= re.match('\Apython',str2)

if match:
    print(match)
else:
    print("no match found")


#match.group
print("Match.group()")

str3=' 39801 356,2102 1111'
patrn2='(\d{3}) (\d{2})'
match= re.search(patrn2,str3)
if match:
    print(match.group())
else:
    print("no match found")



print(match.start())
print(match.end())
print(match.span())
