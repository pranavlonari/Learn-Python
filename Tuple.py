#empty tuple

my_tuple = ()
print(my_tuple)

#Tuple having integer values
my_tuple=(1,2,3)
print("elements are :",my_tuple)

#Tuple having mixed data 
my_tuple=(1,2,3,"hello")
print("elements are :",my_tuple)

#nested tuple
my_tuple=("abc",[2,4,6],(1,2,3))
print("elements are :",my_tuple)
# my_tuple += 4
# print(my_tuple) # will show TypeError: can only concatenate tuple (not "int") to tuple

#accessing element by index
print(my_tuple[0])

#accessing by negative index

print(my_tuple[-1])

#accessing elements by slicing
print(my_tuple[-1:])

print(my_tuple.count('abc'))


print(my_tuple.index('abc'))

#iterating tuple

for my_tuple in my_tuple:
    print(my_tuple)