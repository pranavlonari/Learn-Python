#creating string type variables
String1 = "Python programming"

print(String1)

String2 = 'python programming'
print(String2)

print(String1[1]) #it will print y

print(String1[0:5])

#Strings are immutable 
msg='hello world'

print(msg)

#msg[0]='H' // will throw TypeError: 'str' object does not support item assignment
#print(msg)

msg='Hello there'
print(msg)

#it will create new string object with new value

str= '''
        never give up
        never let you down
    '''
#multiline string
print(str)


str1 = "Hello,world!  "
str2 = "Python programming"
str3 = "Hello,world!  "


print(str1==str2)
print(str1==str3)


result = str1 + str2

print(result)

#iterating string
for letter in str1:
    print(letter)


#String memebership Test : we can check substring exists within a string or not

print('a' in 'program')
print('at' in 'cattle')


#converting to uppercase

print(" ",result.upper())

#converting to lower
print(" ",result.lower())


#swapcase: converts all characters in opposite characters(upper to lower)

str_ex = 'hellO worlD'
print("String before swapcase:",str_ex)
print("String after using swapcase: ",str_ex.swapcase())


random_string = '  this is good'

print(random_string.lstrip())

print(random_string.lstrip('sti'))
print(random_string.lstrip('s ti'))



song ='cold,cold heart'
print(song.replace('cold','Coldheart'))

song = 'let it be,let it be,let it be'

print(song.replace('let',"dont let",2))

#refind example

result = song.rfind(' it')
print(result)

#rindex example
# result = song.rindex('not')
# print(result)

#split-example

cars= 'BMW-Tesla-Range Rover-Audi'
print("starts with BMW is True or False:",cars.startswith('BMW'))
print(cars.split('-'))

data = 'Animal ,Human, Science, Space'

print(data.split(',',2))

data = 'Animal\nHuman \nScience \nSpace'

print(data.splitlines())





