# slicing/selecting sub sequence
# syntax -[start arg : stop arg-1 : step arg(opt)]
# if steporgis -1 it eans we are traversersing backward.
# [::-1]  -reverse, equivalent to [-1::-1]

name = input("enter your name")
rev = name[::-1]
print(f"reverse of your name {rev}")
print(f"reverse of your name {name[::-1]}")