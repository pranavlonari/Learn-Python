
#using iterator
my_list=[4,7,2,0]
iterator = iter(my_list)
print(next(iterator))
print(next(iterator))

#using loop

for element in iterator:
    print(element)

print("Buliding a custom iterator")
class powtwo:
    """power of two"""

    def __init__(self,max=0):
        self.max=max

    def __iter__(self):
        self.n=0
        return self
    def __next__(self):
        if self.n <= self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration
numbers=powtwo(4)
i=iter(numbers)

print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))



print("infinite iterator example")
from itertools import count

infinite_iterator = count(1)

for i in range(5):
    print(next(infinite_iterator))


print("Generator example")

def generator_example(n):
    value=0
    while value < n:
        yield value
        value +=1
for value in generator_example(3):
    print(value)


print("generator expression")


square_generator= (i*i for i in range(5))


for i in square_generator:
    print(i)