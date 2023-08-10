

num_set={22,23,22,'data','is','entered',4.5}
print(num_set)

empty_set = set()
print("data type of Empty_set",type(empty_set))

empty_dictionary = {}
print("data type of empty_dictionary",type(empty_dictionary))


#update python set example
companies = {'Lacoste','Ralph'}
tech_companies =['apple','google','microsoft']
companies.update(tech_companies)
print(companies)

#remove element from set example

lang = {'swift','java','c','c++','python','ruby'}

print("Set before deleting element:",lang)

removed_value = lang.discard('java')
print("set after deleting value:",lang)

num={1,22,32,44,56,87,2}
res = max(num)

print("maximum value is",res)

res=min(num)
print("minimum value is",res)


res=sum(num)
print("sum is:",res)

res=sorted(num)

print("sorted set is",res)

enumerate_lang = enumerate(lang)

print("enumerated set is:",list(enumerate_lang))


fruits = {'Apple', "Peach", "Mango"}

# for loop to access each fruits
for fruit in fruits: 
    print(fruit)

#calculating length

print("Length of a set",len(lang))

A={2,3,6}
B={4,3,8}

print("Union using |:",A|B)
print("Union using union():",A.union(B))

print("Intersection using &:",A&B)
print("Union using intersection():",A.intersection(B))

print("diffrence using -",A-B)
print("diffrence using diffrence():",A.difference(B))
print("Symmetric diffrence using ^",A^B)
print("Symmetric diffrence using symmetric_difference():",A.symmetric_difference(B))

print("Check if Two sets[A,B] are equal or not :")

if A==B:
    print("Sets are Equal")
else:
    print("Sets are not Equal")