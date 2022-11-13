from operation import subtraction,multiplication,division
from addition import addition

while True:
    print("1.Subtraction  2.Multiplication  3.Division  4.Addition  5.Exit")
    choice = input("Enter your choice: ")
    if choice =="1":
        a=int(input("Enter a number: "))
        b=int(input("Enter a number: "))
        print(f"Subtracting the two number gives {subtraction(a,b)}")
    elif choice=="2":
        a=int(input("Enter a number: "))
        b=int(input("Enter a number: "))
        print(f"Multiplying the two number gives {multiplication(a,b)}")
    elif choice=="3":
        a=int(input("Enter a number: "))
        b=int(input("Enter a number: "))
        print(f"Dividing the two number gives {division(a,b)}")
    elif choice =="4":
        n = input("Enter number of numbers to be added (2 or 3): ")
        if n=="2":
            a=int(input("Enter a number: "))
            b=int(input("Enter a number: "))
            print(f"Adding the two number gives {addition(a,b)}")
        elif n=="3":
            a=int(input("Enter a number: "))
            b=int(input("Enter a number: "))
            c=int(input("Enter a number: "))
            print(f"Adding the  three number gives {addition(a,b,c)}")
        else:
            print("Enter a valid choice!")
    elif choice =="5":
        print("Exited")
        exit