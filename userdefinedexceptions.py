class InvalidAgeException(Exception):
    "raise when input is less than 18"
    pass
number=18

try:
    input_num= int(input("Enter age:"))
    if input_num<number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
except InvalidAgeException:
    print("Exception Ocurred :Invalid age")