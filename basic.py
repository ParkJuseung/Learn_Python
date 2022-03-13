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