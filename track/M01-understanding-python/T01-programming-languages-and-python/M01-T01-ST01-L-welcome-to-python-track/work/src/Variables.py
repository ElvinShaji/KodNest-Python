name = "Rahul"
age = 23
print(name)
print(id(name))
print(type(name))

print("Hello Python!", end =" - ")
print("Thank you python")

print("Hello Python! \nThank you python")

print("My name is",name , "and age is", age)
print("My name is "+ name + " and age is "+ str(age))

print(f"My name is {name} and age is {age}")

# single line comment
"""Multi
   line
   comment
"""

a = 20
b = 30
c = 40
print(a+b+c)

a,b,c = 20, 30 , 40
print(a+b+c)

a = b = c = 50

a, b, c = "Abhi", "Ravi", "Sree"
print(b)
print(a+b+c)

x, y, z = 30, 4, 8
print(x+z)
print(a+str(x))# cant concaternate int and str directly using +
print(b+c)
print(a, x)# can cocatenate int and str using comma


print(type(a), a)

