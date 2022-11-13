def pallindrome ():
    s=input("Enter a string to be reversed?")
    s_reversed = s[::-1]
    print(f"The reverse of the string is {s_reversed}")
    if (s_reversed==s):
        print("The entered string is pallindrome")
    else:
        print("The entered string is not pallindrome")

def factorial ():
    number = input("Enter a number:")
    factorial = 0
    if number ==0:
        print("Factorial is 1")
    elif number==0:
        print("The factorial does not exist for the entered number.")
    else:
        for i in range(1,number+1):
            factorial = factorial*i
        print(f"The factorial of {number} is {factorial}")

choice = input("Enter a choice: ")

if choice =="1":
    pallindrome()
elif choice =="2":
    factorial()
else:
    exit










