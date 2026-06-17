class Employee:
    def __init__(self,name,ID,position,department,salary,joindate):
        self.name=name
        self.ID=ID
        self.position=position
        self.department=department
        self.salary=salary
        self.joindate=joindate
    def display_employee_details(self):
        print("Employee ID    =",self.ID)
        print("Employee Name  =",self.name)
        print("Department     =",self.department)
        print("salary         =",self.salary)
        print("joining date   =",self.joindate)
        print("Position       =",self.position)
class Employee_record_system:
    def __init__(self):
        self.employee=[]
    def Add_Employee(self):
        try:
            name=input("Enter Employee name             :")
            ID=int(input("Enter Employee ID             :"))
            salary=int(input("Enter Employee Salary     :"))
            position=input("Enter position of employee  :")
            department=input("Enter Department          :")
            joindate=input("Enter Joindate              :")
            Emp=Employee(name,ID,position,department,salary,joindate)
            

            duplicate=False
            for e in self.employee:
                if e.ID==ID:
                    duplicate=True
                    break
            if duplicate==True:
                print("EID already exists")
            else:
                self.employee.append(Emp)
                self.Save_Data()
                print("Employee Added Succesfully")
        except ValueError:
            print("Please provide correct values for ID and salary")
    def Update_Employee(self):
        try:
            found=False
            search_id=int(input("Enter search id to update"))
            for j in self.employee:
                if j.ID==search_id:
                    found=True
                    print("What do you want to Update","\n1.ID","\n2.Name","\n3.Position","\n4.Department",
                      "\n5.Salary")
                    choice=int(input("Enter your choice to change:"))
                    match choice:
                        case 1:
                            new_id=int(input("Enter id to change:"))
                            duplicate=False
                            for e in self.employee:
                                if e.ID==new_id and e!=j:
                                    duplicate=True
                                    break
                            if duplicate:
                                print("EID already exists")
                            else:
                                j.ID=new_id
                                print("Updated successfully")
                                self.Save_Data()
                        case 2:
                            new_name=input("Enter name to change:")
                            j.name=new_name
                            print("Updated Successfully")
                            self.Save_Data()
                        case 3:
                             new_position=input("Enter position to change:")
                             j.position=new_position
                             print("Updated Successfully")
                             self.Save_Data()
                        case 4:
                            new_department=input("Enter department to change:")
                            j.department=new_department
                            print("Updated Successfully")
                            self.Save_Data()
                        case 5:
                            new_salary=int(input("Enter salary to change:"))
                            j.salary=new_salary
                            print("Updated Successfully")
                            self.Save_Data()
                        case _:
                            print("Invaliid option try again")
                            break
            if found==False:
                print("Employee not found")
        except ValueError:
            print("Enter the value in integer and string")
    def Remove_Employee(self):
        try:
            found=False
            search_id=int(input("Enter id to remove:"))
            for k in self.employee:
                if k.ID==search_id:
                    found=True
                    self.employee.remove(k)
                    self.Save_Data()
                    print("Employee removed successfully")
                    break
            if found==False:
                print("Cannot find the employee")
        except ValueError:
            print("Enter the value in integer and string")
    def Search_Employee(self):
        try:
            found=False
            search_id=int(input("Enter employee ID to search:"))
            search_name=input("Enter Employee name to search:")
            for k in self.employee:
                if k.ID==search_id or k.name==search_name:
                    found=True
                    print("Employee details")
                    k.display_employee_details()
                    break
            if found==False:
                print("Cannot find the employee")
        except ValueError:
            print("Enter the value in integer and string")
    def Display_Employee(self):
        if self.employee==[]:
            print("No Employees Found")
        else:
            for g in self.employee:
                g.display_employee_details()
    def Save_Data(self):
        try:
            with open("Samples.txt","w") as f1:
                for em in self.employee:
                    f1.write(f"{em.ID},{em.name},{em.position},{em.department},{em.salary},{em.joindate}\n")
        except IOError:
            print("Error while saving file")
    def Load_Data(self):
        try:
            self.employee.clear()
            with open("Samples.txt","r") as f1:
                for line in f1:
                    data = line.strip().split(",")
                    Emp = Employee(
                        data[1],
                        int(data[0]),
                        data[2],
                        data[3],
                        int(data[4]),
                        data[5])
                    self.employee.append(Emp)
                
            f1.close()
        except FileNotFoundError:
            print("File not found")
e1=Employee_record_system()
e1.Load_Data()
while True:
    try:
        print("1.Add Employee")
        print("2.Update Employee")
        print("3.Remove Employee")
        print("4.Search Employee")
        print("5.Display Employee")
        print("6.Exit")
        option=int(input("Enter your option:"))
        match option:
            case 1:
                e1.Add_Employee()
            case 2:
                e1.Update_Employee()
            case 3:
                e1.Remove_Employee()
            case 4:
                e1.Search_Employee()
            case 5:
                e1.Display_Employee()
            case 6:
                print("Exiting Program....")
                break
            case _:
                print("Invalid option try again")
    except ValueError:
        print("Enter the correct input ")
