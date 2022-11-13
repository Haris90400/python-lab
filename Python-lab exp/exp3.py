lst_1 = [int(i) for i in input("Enter odd element list: ")]
lst_2 = [int(i) for i in input("Enter even element list: ")]
lst_1.sort()
lst_2.sort()
lst_3 = lst_1+lst_2
add_num = int(input("Enter a number to be added in the first positon: "))
lst_3[0]=add_num



print(lst_3)