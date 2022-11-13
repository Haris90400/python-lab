string_1 = {x for x in input("Enter first string: ")}
string_2 = {x for x in input("Enter second string: ")}
print(f"String 1 :{string_1}\nString 2: {string_2}")

while True:
    print("**-----Menu Driven Program-----**")
    print("1. Display Common   2. Display Union   3. Display Set Difference   4. Display Symmetric difference")

    choice=input("Enter a choice: ")
    if choice=="1":
        print(string_1.intersection(string_2))
    elif choice=="2":
        print(string_1.union(string_2))
    elif choice=="3":
        print(string_1.difference(string_2))
    elif choice=="4":
        print(string_1.symmetric_difference(string_2))
    else:
        exit()
