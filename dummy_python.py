"""Python is a popular programming language. It was created in 1991 by Guido van Rossum.
You will love it!!!!"""


# Hello World!
print ("Hello World!")


# This is a comment
"""This
is also a comment"""


# Variables

name = 'Khadija' # string
age = 18         # number


# String

a = 'Hi'         # a string
b = "Hello"      # also a string


# Number Types

c = 120          # integer
d = 1.23         # float
e = 2m           # complex


# Input

name = input("What is your name? ") # prints 'What is your name' to the console and takes the input as the new value of 'name'
print("Hello," + name)              # returns input


# Operators
# Arithmetic

f = 5 + 5       # 10
g = 5 - 2       # 3
h = 4 * 4       # 16
i = 10 / 2      # 5
j = 6 % 2       # 0  ,  % means Remainder


# Assignment

k += 4         # k = k + 4
l -= 2         # l = l - 2
m *= 11        # m = m * 11
n /= 9         # n = n / 9
o %= 3         # o = o % 3


# Comparison
# ==
#/ !=
# >
# <
# >=
# <=

p = 8
q = 7

print(x == y)  # returns 'False' because 8 is not equal to 7
print(x != y)  # returns 'True' because 8 is not equal to 7
print(x > y)   # returns 'True' because 8 is greater than 7
print(x < y)   # returns 'False' because 8 is greater than 7
print(x >= y)  # returns 'True' because 8 is greater than equal to 7
print(x <= y)  # returns 'False' because 8 is greater than equal to 7


# Collections
# List is a collection which is ordered and changeable and allows duplicate members.
# Tuple is a collection which is ordered and unchangeable and allows duplicate members.
# Set is a collection which is unordered and unindexed and does not allow duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed and does not allow duplicate members.

r = ["Muhammad", 2, 20, "Sadiq"]        # list

s = list(("Muhammad", 2, 20, "Sadiq"))  # also list

t = ("Abdul", "Mike")                   # tuple 

u = tuple(("Abdul", "Mike"))            # also tuple 

v = {"Ali", "Umar", "Yahya"}            # set 

w = set(("Ali", "Umar", "Yahya"))       # also set 

x = {
    "House": "Mansion", 
    "Car": "Tesla", 
    "Phone": "Samsung"
}                                       # dictionary

y = dict(
    "House": "Mansion", 
    "Car": "Tesla", 
    "Phone": "Samsung"
)                                      # also dictionary


# Conditions
# if..elif..else
# and..or..is..not

z = 99
aa = 10
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

"""if it is raining, take an umbrella
or maybe a rain coat
if not, then just a tshirt would do"""


# Loop
# For Loops
# While loops

ab = ["dev", "design", "google"]
ac = 3

for i in ab:                        # for loop
  print(i) 

while i < 3:                        # while loop
    print(i)
    i = i + 1


# Functions

def whatever(a,b)
    return a + b

whatever(5,5)                      # returns 10

# Lambda

ad = lambda a, b : a - b
print(ad(5, 6))                    # returns -1

# Classes

class Person:
  def __init__(whatever, name, age):
    whatever.name = name
    whatever.age = age

ae = Person("Khadija", 18)

print(ae.name + " " + ae.age)


# that was cool right?
# go practice, the sky is not the limit when it comes to learning, just keep doing it

