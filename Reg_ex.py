import re
pattern ='^a...s$'
test_string='abyss'
res=re.match(pattern,test_string)
if res:
    print("search is successful")
else:
    print("Search is unsucessful")