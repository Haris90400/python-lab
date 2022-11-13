while True:
    print("***------Menu Driven Program-----***")
    print("1.Create a dictionary 2.Update the key and value  3.Remove key and value  4.Find a key  5.Exit")
    choice=input("Enter a choice: ")
    if choice=="1":
        lst_1 = [int(i) for i in input("Enter dictionary keys: ")]
        lst_2 = [i for i in input("Enter dictionary values: ")]
        z1=zip(lst_1,lst_2)
        d1=dict(z1)
        print(d1)
    elif choice =="2":
        add_key = [int(i) for i in input("Enter dictionary keys to be updated: ")]
        add_value = [i for i in input("Enter dictionary values to be updated: ")]
        z2=zip(add_key,add_value)
        d2=dict(z2)
        d1.update(d2)
        print(d1)
    elif choice=="3":
        remove_key = int(input("Enter the key to be removed: "))
        d1.pop(remove_key)
        print(d1)
    elif choice=="4":
        lst_3=d1.keys()
        search_key = int(input("Enter the key to be searched: "))
        for x in lst_3:
            if search_key==x:
                print("value of {} is {}".format(search_key,d1[search_key]))
    else:
        exit()