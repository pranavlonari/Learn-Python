class operator:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __str__(self):
           
           return "({0},{1})".format(self.x,self.y)
    def __add__(self,other):
         x=self.x+other.x
         y=self.y+other.y
         return operator(x,y)
p1=operator(1,2)
p2=operator(2,3)

print(p1+p2)


#[<] overloading comparison operator
class Person:
     
     def __init__(self,name,age):
          self.name=name
          self.age=age
     def __lt__(self,other):
          return self.age < other.age     
p1=Person("john",30)

p2=Person("Alice",40)


print(p1<p2)
print(p2<p1)
if(p1<p2):
     print(p1.age,p1.name)
