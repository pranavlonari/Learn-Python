def outer(x):
    def inner(y):
        return x + y
    return inner
add_five=outer(5)
result=add_five(6)

print(result)


#passing function as argument

print("passing function as argument")


def add(x,y):
    return x+y
def calculate(func,x,y):
    return func(x,y)
result=calculate(add,4,6)
print("result=",result)


print("Return function as a value")

def greet(name):
    def hello():
        return "Hello "+name+"!"
    return hello
greet= greet("Atlantis")

print(greet())


def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()



def make_pretty(func):
    def inner():
        print("I got decorated!!!!")
        func()
    return inner
@make_pretty
def ordinary():
    print("I am ordinary!!!!")
ordinary()