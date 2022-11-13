n = int(input("Enter number of students: "))
lst_1 = list()

for i in range(0,n):
    r_no =int(input(f"Enter roll no. of student {i+1}: "))
    name = input("Enter name: ")
    m1 =int(input("Enter marks in subject1: "))
    m2 =int(input("Enter marks in subject2: "))
    m3 =int(input("Enter marks in subject3: "))
    l1=[r_no,name,m1,m2,m3]
    tpl = tuple(l1)
    lst_1.append(tpl)

tpl=tuple(lst_1)
while True:
    print("1.All elements 2.Element with python 3.Sorted tuple 4.Exit")
    choice=input("Enter a choice: ")
    if choice =="1":
        print("All elements:")
        for t in tpl:
            print(t)
    elif choice =="2":
        print("Element with python:")
        for t in tpl:
            if "python" in t:
                print(t)
    elif choice=="3":
        print("Sorted tules according to name:")
        print(sorted(tpl,key=lambda x: x[1]))
    elif choice=="4":
        exit()
    
