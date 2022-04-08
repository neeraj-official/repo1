# strings are immuatable
string1 = "Neeraj"
# string1[2]="E"   #TypeError: 'str' object does not support item assignment

# x = string1.replace("e","E",2)

# print(x)

string1 = string1.replace("e","E",2)

print(string1)
print(string1)  # which means original string remains same
