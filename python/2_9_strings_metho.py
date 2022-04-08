# string methods - I

name = "Neeraj Kumar"

# 1. len() function
# 2. methods  - lower(),upper(),title(),count()  -- we use dot in methods

print(len(name))

print(name.lower())
print(name.upper())
print(name.title())
print(name.count("n"))

#Exer1

name1,letter = input("enter name and character separated by comma").split(",")
print(f"{name1} and it's length is {len(name1)} \n  {letter} has occured {name1.count(letter)}")

print(f"{name1} and it's length is {len(name1)} \n  {letter} has occured {name1.lower().count(letter)}")

# string replace() find()-find character position in string ||
# replace("what to replace","replacing obj",till how many occurences)
# find("what to find",start serch position)

string1 = "she is beautiful and she is good dancer"
print(string1.replace(" ",""))

string1 = "she is beautiful and she is good dancer"
print(string1.replace("is","was",1))

print(string1.find("is"))
print(string1.find("is",5))

# center()  method
nam = "nee"
print(nam.center(7,"*"))

