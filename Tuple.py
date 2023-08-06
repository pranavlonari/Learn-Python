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
my_tuple += 4
print(my_tuple) # will show TypeError: can only concatenate tuple (not "int") to tuple