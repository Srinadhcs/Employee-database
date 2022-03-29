class Person:
    id = 0
    name = ""
    gender = ""
    city = ""
    salary = 0

    def add_employee():
        f = open('./employee.txt', 'a')
        name = input("Enter employee name: ")
        name = name.replace(" ", "_")
        while True:
            if name.isdigit():
                name = input("Enter employee name with string format: ")
            else:
                f.write(name + ' ')
                break

        designation = input("Enter employee designation: ")
        designation = designation.replace(" ", "_")
        while True:
            if designation.isdigit():
                designation = input("Enter employee designation with string format: ")
            else:
                f.write(designation + ' ')
                break

        hours_worked = input("Enter the number of hours employee worked in a week: ")
        while True:
            if hours_worked.isdigit():
                f.write(hours_worked + ' ')
                break
            else:
                hours_worked = input("Enter the number of hours employee worked in a week in proper format(int): ")

        pay_rate = input("Enter employee hourly pay rate: ")
        while True:
            if pay_rate.isdigit():
                f.write(pay_rate + ' ')
                break
            else:
                pay_rate = input("Enter employee hourly pay rate in proper format(int): ")

        f.write("\n")
        f.close()

    def display_details():
        f = open('employee.txt')

        ip = input("\nChoose:\n1: Choose employee by Name\n2: All employees\nEnter your choice: ")

        if ip == '1':
            entered_name = input("\nEnter the Name of the employee: ")
            entered_name = entered_name.replace(" ", "_")
            flag = 1
            for line in f:
                li = line.split()
                if li[0].lower() == entered_name.lower():
                    flag = 0
                    print("--------------------------------")
                    print("Payroll Statement\n\n")
                    print("Employee Name:{}\nEmployee Designation:{}\nTotal hours worked:{}\nPay Rate:{}\n".format(
                        li[0].replace("_", " "), li[1].replace("_", " "), li[2], li[3]))
                    print("--------------------------------")
            if flag == 1:
                print("No Match! Enter correct name or add employee details")
        elif ip == '2':
            print("--------------------------------")
            print("Payroll Statement\n\n")
            for line in f:
                li = line.split()
                print("Employee Name:{}\nEmployee Designation:{}\nTotal hours worked:{}\nPay Rate:{}\n".format(
                    li[0].replace("_", " "), li[1].replace("_", " "), li[2], li[3]))
            print("--------------------------------")
        f.close()

    def remove_employee():
        f = open('employee.txt', mode='r')
        lines = f.readlines()
        f.close()
        name = input("Enter name of employee: ")
        name = name.replace(" ", "_")
        flag = 1
        for i in range(len(lines)-1):
            li = lines[i].split()
            if li[0].lower() == name.lower():
                flag = 0
                del lines[i]
        f1 = open('employee.txt', mode='w')
        for line in lines:
            f1.write(line)
        f1.close()

        if flag == 1:
            print("No Match! Enter correct name or add employee details")

    def calculate_wages():
        f = open('employee.txt', mode='r')
        lines = f.readlines()
        f.close()
        sum = 0
        for i in range(len(lines)-1):
            li = lines[i].split()
            sum += int((int(li[2])/5) * int(li[3]))
        print("Total Employees Wages are: ", sum)

    def give_raise():
        f = open('employee.txt', mode='r')
        lines = f.readlines()
        f.close()
        name = input("Enter name of employee: ")
        ras = input("Enter raise in Salary: ")
        name = name.replace(" ", "_")
        flag = 1
        for i in range(len(lines)-1):
            li = lines[i].split()
            if li[0].lower() == name.lower():
                flag = 0
                li[3] = int(li[3]) + int(ras)
                li[3] = str(li[3])
                lines[i] = li[0] + " " + li[1] + " " + li[2] + " " + li[3] + " " + "\n"
        f1 = open('employee.txt', mode='w')
        for line in lines:
            f1.write(line)
        f1.close()

        if flag == 1:
            print("No Match! Enter correct name or add employee details")
