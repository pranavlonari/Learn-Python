#nested function
print("Nested Function")

def greet(name):
    def display_name():
        print("Hi",name)
    display_name()
greet("John")



def greet():
    name="alex"
    return lambda:"Hi "+name
message=greet()
print(message())

def calculate():
    num=1
    def inner_function():
        nonlocal num
        num +=2
        return num
    return inner_function
odd=calculate()
print(odd())
print(odd())
print(odd())

odd2=calculate()
print(odd2())
