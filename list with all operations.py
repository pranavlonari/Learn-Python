
list1 = [1,2,3,4,5,11,12,11,12]
#adding with append

list1.append(24)

print(list1)

#adding element with extend

list2=[21,22,23]

list1.extend(list2)

print(list1)

#adding element with insert

list1.insert(2,44)
print(list1)
#deleting element using remove

list1.remove(3)
print(list1)

#delete element using pop

list1.pop(2)
print(list1)

#counting occurences
count=list1.count(11)
print("11's occurence in list are :",count)

#remove element using pop
removed =list1.pop(3)
print("removed element is :",removed)

#accessing elements using index

print("list1[9]: ",list1[9])

#sorting in Ascending order

list1.sort()
print("sorted in Ascending order:",list1)

#sorting in descending order
list1.sort(reverse=True)

print("Descending order sorting: ",list1)


list3=['a','b','c','d']

#reverse order

for i in reversed(list3):
    print("\t",i)

#copy example

list_1=['a','b','c','d','e','f']

print("list_1 Elements:",list_1)
new_list= list_1.copy()

print("new_list elements after copying are :",new_list)

#copy using slicing operator

nw = list_1[:-1]

print("copied list after slicing:",nw)

#clearing list is removes all element from list

nw.clear()

print("nw:",nw)

#iterating through list
for list_1 in list_1:
    print(" \t",list_1)


#finding element exist or not
print('d' in list_1)


#finding length of a list

print("length of list1 :",len(list1))


#list comprehension

numbers=[n**3 for n in range(1,6)]
print(numbers)



