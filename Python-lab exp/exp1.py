import sys

a =(sys.argv[1])
b =(sys.argv[2])

print(f"Before swapping\n a={a}\n b={b}")


temp = a
a=b
b = temp

print(f"After swapping\n a={a}\n b={b}")

a=int(a)
if(a>0):
    print("a is positive number.")
elif (a<0):
    print("a is negative number.")
else:
    print("a is zero.")