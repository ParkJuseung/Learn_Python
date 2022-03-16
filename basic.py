a=2
b=3
c = 'like this'
d = False
e = "False"
float = 3.12
none = None

print(a+b)

print (type(none))

days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]

print("Mon" in days) #Ture
print(len(days)) # 7
print(type(days))
days.append("Sunday")
print(days)

days.reverse()
print(days)

animals = ("cat", "dog", "bird", "mouse", "lion")
print(type(animals)) #tuple (immutable)

#dictionary
park = {
    "age" : 29,
    "Korean" : True,
    "hobby" : ["game", "music", "movie"]
}

print(park["age"]) #29
park["handsome"] = True
print(park)

#function
def say_hello():
    print("hello")
    
say_hello()

#return is finish the function
def r_plus(a,b):
    return a+b
    print("hihihihihihihiih")

r_result = r_plus(2,4)
print(r_result)

#keyworded Arguments
def say_hello(name, age):
    return f"hello {name} you are {age} years old"

hello= say_hello(age="29", name="park")
print(hello)

#if /else 
def plus(a,b):
    if type(a) and type(b) == int:
        return a+b
    else: 
        return None

result = plus(1,2)
print(result)
    
def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you can't drink")
    elif age == 18:
        print("you are new to this")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else :
        print("enjoy your drink")

age_check(23)

#for loop
days = ("Mon", "Tue", "Wed", "Thue", "Fri")
for x in days :
    print(x)

for number in [1, 2, 3, 4, 5]:
    if number is 4:
        break
    else :
        print(number)

for name in "ParkJuseung" :
    print(name)

#module
#필요한 것만 import해라
import math
print(math.ceil(1.2))

from math import ceil, fsum

print(ceil(1.2))
print(fsum([1,2,3,4,5,6]))

#이름 변경도 가능
from math import fsum as sexy
print(sexy([1,2,3,4,5]))