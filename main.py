# Beneath each comment, write the code and print out the result to check it works

'''LISTS'''

# Create a list and assign it to a variable
list1 = [1, 2, "divya", "shonu"]

# Find the length of the list
length = len(list1)
 print(length) ===> 4

# Append an item to the list
list1.append("rishu")
 print(list1) ===> [1, 2, 'divya', 'shonu', 'rishu']

# Find the value of an item in the list at a specific index
print(list1[1]) ===> 2
# Set the value of an item at a specific index
list1[2] = "flower"
print(list1) ===> [1, 2, 'flower', 'shonu', 'rishu']
# Check whether an item is in the list
print("shonu" in list1) ===> True
# Sort the list
num = [3,9,5,7,1,8]
num.sort()
print(num) ===> [1, 3, 5, 7, 8, 9]

num.sort(reverse=True)
print(num) ===> [9,8,7,5,3,1]

# Iterate over the list using range, printing out each element and the index
alpha = ["a","b","c","d"]
for index in range(len(alpha)):
  print(index, alpha[index])  ===> 0 a
1 b
2 c
3 d
  
# Iterate over the list without using range, printing out each element
for i in alpha:
  print(i) ===> a
b
c
d
===========================================================================
'''TUPLES'''

# Create a tuple and assign it to a variable
flowers = ("rose", "lily", "marigold", "tulips", "dahlia")
print(flowers) ===> ('rose', 'lily', 'marigold', 'tulips', 'dahlia')

# Find the length of the tuple
print(len(flowers)) ===> 5

# Find the value of an item in the tuple at a specific index
print(flowers[2]) ===> marigold

# Check whether an item is in the tuple
print("rose" in flowers) ===> True

# Iterate over the tuple using range, printing out each element and the index
for index in range(len(flowers)):
  print(index, flowers[index]) ===> 0 rose
1 lily
2 marigold
3 tulips
4 dahlia

# Iterate over the tuple without using range, printing out each element
for i in flowers:
  print(i) ===> rose
lily
marigold
tulips
dahlia
===========================================================
'''STRINGS'''

# Create a string and assign it to a variable
str = "color"
print(str) ===> color

# Find the length of the string
print(len(str)) ===> 5

# Find the value of a character in the string at a specific index
print(str[2]) ===> l

# Check whether an item is in the string
print("k" in str) ===> False
print("c" in str) ===> True

# Concatenate (add) two strings together
s1 = "divya"
s2 = "palusa"
print(s1+s2) ===> divyapalusa

# Create an f-string
name = "Divya"
age = 35
message = f"My name is {name} and I am {age} years old."
print(message) ===> My name is Divya, and I am 35 years old.

# Split a string using .split
sentence = "I love India"
words = sentence.split()
print(words) ===> ['I', 'love', 'India']

# Join a list of strings using .join
words = ["I", "love", "Python"]
sentence = "&".join(words)
print(sentence) ===> I&love&Python

# Iterate over the string using range, printing out each character and the index
for index in range(len(words)):
  print(index, words[index]) ===> 0 I
1 love
2 Python

# Iterate over the string without using range, printing out each character
for i in words: 
print(i) ===> I
love
Python
================================================
'''DICTIONARIES'''

# Create a dictionary and assign it to a variable
student = {
    "name": "Divya",
    "age": 35,
    "language": "Python"
}
print(student) ===> {'name': 'Divya', 'age': 35, 'language': 'Python'}
# Find the length of the dictionary
print(len(student)) ===> 3

# Add a new key/value pair
student["course"] = "Ada"
print(student) ===> {'name': 'Divya', 'age': 35, 'language': 'Python', 'course': 'Ada'}
# Replace value for a given key
student["language"] = "Java"
print(student) ===> {'name': 'Divya', 'age': 35, 'language': 'Java', 'course': 'Ada'}

# Check whether a key is in the dictionary
print("name" in student)===> True
print("city" in student)===> False

# Iterate over keys, printing each key
for key in student:
  print(key) ===> name
age
language
course

# Iterate over over key/value pairs using .items(), printing each key and value
for key, value in student.items():
    print(key, value) ===> name Divya
age 35
language Java
course Ada
  
  =====================================================================
'''SETS'''

# Create a set and assign it to a variable
fruits = {"apple", "banana", "orange"}
print(fruits) ===> {'orange', 'banana', 'apple'}

# Find the length of the set
print(len(fruits)) ===> 3

# Add a new element
fruits.add("mango")
print(fruits) ===> {'orange', 'banana', 'mango', 'apple'}

# Remove an element
fruits.remove("apple")
print(fruits) ===> {'orange', 'banana', 'mango'}

# Check whether an element is in the set
print("banana" in fruits) ===> True
print("mango" in fruits) ===> True

# Iterate over elements, printing each one out
for fruit in fruits:
  print(fruit) ===> orange
banana
mango
=================================================================================================
'''NUMBERS'''

# Add/subtract/multiply 2 numbers
num1 = 5
num2 = 3
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
print(addition)
print(subtraction)
print(multiplication) ===> 8
2
15

# Divide two numbers using normal (float) division
num1 = 5
num2 = 3
division = num1 / num2
print(division) ===> 1.6666666666666667
# Divide two numbers using integer division
num1 = 10
num2 = 3
result = num1 // num2
print(result) ===> 3 (Modulus operator(//))

# Find the modulo (remainder) of two numbers
num1 = 10
num2 = 3
remainder = num1 % num2
print(remainder) ===> 1

# Check whether a number is even/odd
number = 8
if number % 2 == 0:
    print("Even")
else:
    print("Odd") ===> Even
  
# Round a float down to an int
import math
number = 7.8
result = math.floor(number)
print(result) ===> 7
num = 4.56
result = int(num)
print(result) ===> 4

==============================================================================================================
'''FUNCTIONS'''

# Write a function that takes no arguments and call it
def say_hello():
    print("Hello!")
say_hello() ===> Hello!

# Write a function that takes one or more arguments and call it
def greet(name):
    print(f"Hello, {name}!")
greet("Divya") ===> Hello, Divya!

# Write a function that returns a value. Call the function and store the return value in a variable
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 5)
print(result) ===> 15
========================================================================================

'''LOOPS'''

# Write a while loop
count = 1
while count <= 5:
    print(count)
    count += 1 ===> 1 2 3 4 5
  
# Write a for loop that loops a set number of times (e.g. 10 times)
for i in range(10):
    print("Hi") ===> Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
Hi
============================================================================  
'''CONDITIONALS'''

# Write an if/elif/else statement
age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult") ===> Adult
  
# Write conditionals for the following operators:
# ==
# !=
# <
# >
# <=
# >=
a = 10
b = 5

if a == b:
    print("a is equal to b") ===> False
if a != b:
    print("a is not equal to b") ===> a is not equal to b
a is greater than b
if a < b:
    print("a is less than b") ===> False
if a > b:
    print("a is greater than b") ===> a is greater than b
if a <= b:
    print("a is less than or equal to b") ===> False
if a >= b:
    print("a is greater than or equal to b") ===> a is greater than or equal to b 

=======================================================================================================================

'''NESTED DATA'''

# Write a nested list (a list of lists) and assign it to a variable
students = [
    ["Divya", 25],
    ["John", 30],
    ["Sarah", 28]
]
print(students) ===> [['Divya', 25], ['John', 30], ['Sarah', 28]]

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second
print(students[1][0]) ===> John

# Iterate through the nested data structure using range
for row in range(len(students)):
    for column in range(len(students[row])):
        print(students[row][column]) ===> Divya
25
John
30
Sarah
28

# Iterate through the nested data structure without using range 
for row in students:
    for item in row:
        print(item) ===> Divya
25
John
30
Sarah
28
      
'''REMINDER'''

# You're doing great, and you got this!
