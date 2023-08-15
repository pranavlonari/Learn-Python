class parrot:
    #class attribute
    name=""
    age=0

#creating object
parrot1=parrot()
parrot1.name="Blue"
parrot1.age=2
#creating Second object
parrot2=parrot()
parrot2.name="aqua"
parrot2.age=4

#access attributes
print("1st Object data:\n", "name:",parrot1.name,"age:",parrot1.age)
print("2nd Object data:\n","name:",parrot2.name,"age:",parrot2.age)



#<base class>
class Animal:
    def eat(self):
        print("I can eat!")
    def sleep(self):
        print("I can sleep!")
    
class Dog(Animal):
    def bark(self):
        print("I can bark woof woof!!!")
dog1=Dog() #created object of dog class

#calling members of base class

dog1.eat()
dog1.sleep()

dog1.bark()

print("\nData Encapsulation Example:")

class Computer:
    def __init__(self):
        self.__maxprice=900
    
    def sell(self):
        print("selling price:{}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice = price

c=Computer()
c.sell

#change the price
c.__maxprice=1000
c.sell()

#using setter function
c.setmaxprice(1000)
c.sell()


print("\nPolymorphism example:")

class polygon:
    def render(self):
        print("rendering polygon")

class square(polygon):
    #renders square
    def render(self):
        print("Rendering square...")
class circle(polygon):
    #renders circle
    def render(self):
        print("Rendering circle")

#create an object of square
s1=square()
s1.render()

#creating object of circle
c1=circle()
c1.render()

#class example
print("\nClass Example:")
class emp:
    emp_id=0
    emp_name=""

emp1=emp()
emp1.emp_id=2000
emp1.emp_name="John"

emp2=emp()
emp2.emp_id=2002
emp2.emp_name="Sam"

print("emp1 data:","id:",emp1.emp_id,"Name:",emp1.emp_name)

print("emp2 data:","id:",emp2.emp_id,"Name:",emp2.emp_name)


#class example for class with python method

class Room:
    length=0.0
    breadth=0.0

    def area(self):
        print("Area of Room:",self.length*self.breadth)

study_room=Room()

study_room.length= 7.7
study_room.breadth= 22.2

study_room.area()

#Multiple Inheritance:

class car:
    def car_info(self):
        print("Car=BMW")


class Bus:
    def Bus_info(self):
        print("Bus is Started")

class Vehicle(car,Bus):
    pass

veh1= Vehicle()

veh1.car_info()
veh1.Bus_info()


#Multilevel inheritance

class superclass:
    print("superclass method called")

class derivedclass1(superclass):
    def derived_method(self):
        print("derived class 1 called")
class derivedclass2(derivedclass1):
    def derived_method2(self):
        print("derived class 2 called")

d2= derivedclass2()
d2.derived_method()
d2.derived_method2()

