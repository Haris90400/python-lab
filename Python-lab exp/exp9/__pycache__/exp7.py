class Emp:
    def __init__(self,id1,name1):
        self.id = id1
        self.name = name1
    def display(self):
        print(self.id)
        print(self.name)
    def setvalue(self,id1,name1):
        self.id = id1
        self.name = name1

l1=list()

while True:
    print("1.Read an employee  2.Modify the employee  3.Display employee  4.Delete emplyee  5.Exit")
    choice = input("Enter a choice")
    if choice =="1":
        number_of_employees = int(input("Enter umber of employees: "))
        for i in range(number_of_employees):
            eid = int(input("Enter emplyee id: "))
            ename = input("Enter employee name: ")
            e1 = Emp(eid,ename)
            l1.append(e1)

    elif choice =="2":
        upid = int(input("Enter employee id to be updated: "))
        upname = input("Enter employee name to be updated: ")
        for q in l1:
            if q.id ==upid:
                q.setvalue(upid,upname)

    elif choice =="3":
        for i in l1:
            print(f"Id: {i.id} Name:{i.name}")

    elif choice=="4":
        did = int(input("Enter employee id to be deleted: "))
        for d in l1:
            if d.id==did:
                l1.remove(d)
    elif choice =="5":
        exit()
