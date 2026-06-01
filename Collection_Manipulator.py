from datetime import datetime

print("Welcome to the Student Data Organizer !")

students = []   #List where all student records will be save.

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("\nEnter Your choice(ex. 1 to add student.) : "))

    match choice:
        case 1: 
            id = (int(input("\nEnter student ID : ")))
            name = str(input("Enter student name : "))
            age = int(input("Enter student age : "))
            grade = str(input("Enter student grade : "))
            dob_input = input("Enter your date of birth (DD-MM-YYYY) : ")
            dob = (datetime.strptime(dob_input,"%d-%m-%Y").date())  # strptime(str, format) function convert date from string to actual date and the formate here is %d-day, %m-month, %Y-year(Y is for 4 digit year, y is used to take only 2 digit year input)
            # id_dob = (id, dob)
            subList = {'Maths', 'Biology', 'Physics', 'Chemestry', 'English'}
            print("Subject List : ")
            for subj in subList: 
                print(subj)
            sub = set(input("Choose Subjects (comma-separated) : ").split(",")) #Taken input as a list comma seperated subjects and then converted into set.
            student = {'id':id, 'name':name, 'age':age, 'grade':grade, 'dob':dob, 'sub':sub}

            students.append(student)

            print("\nStudent Added Successfully...!\n")

        case 2:
            if not students:
                print("Database is empty. No students available to display...\n")
            for stu in students:
                print(f"ID : {stu['id']} | Name : {stu['name']} | Age : {stu['age']} | Grade : {stu['grade']} | DOB : {stu['dob']} | Subjects : {stu['sub']}\n")
        case 3:
            if not students:
                print("Database is empty. No students available to update....\n")
            else:
                id = int(input("Enter Student ID : "))
                found = False

                for stu in students:
                    if stu['id'] == id:
                        found = True
                        while True:
                            print("1. Update Name.")
                            print("2. Update Age.")
                            print("3. Update Grade.")
                            print("4. Update Subjects.")
                            print("5. Back.")

                            option = int(input("Enter your choice(ex. 1 for Update Name.) : "))

                            match option:
                                case 1:
                                    newName = str(input("Enter new Name : "))
                                    stu['name'] = newName
                                    print("Name updated successfully...\n")
                                case 2: 
                                    newAge = int(input("Enter new Age : "))
                                    stu['age'] = newAge
                                    print("Age updated successfully...\n")
                                case 3: 
                                    newGrade = str(input("Enter new Grade : "))
                                    stu['grade'] = newGrade
                                    print("Grade updated successfully...\n")
                                case 4: 
                                    subList = {'Maths', 'Biology', 'Physics', 'Chemestry', 'English'}
                                    print("Subject List : ")
                                    for subj in subList: 
                                        print(subj)
                                    newSubs = set(input("Enter new Subjects(comma-seperated) : ").split(","))
                                    stu['sub'] = newSubs
                                    print("Subjects updated successfully...\n")
                                case 5: 
                                    break
                                case _: 
                                    print("Invalid choice!\n")
                if found == False:
                    print("No record found...\n")

        case 4: 
            if not students:
                print("Database is empty. No students available for deletion...\n")
            else:
                id = int(input("Enter student ID : "))
                found = False

                for stu in students:
                    if stu['id'] == id:
                        found = True
                        students.remove(stu)
                        print("Student deleted successfully...\n")
                if found == False:
                    print("No record found...\n")
        case 5: 
            subList = {'Maths', 'Biology', 'Physics', 'Chemestry', 'English'}
            print("All Subjects :- ")
            for subj in subList: 
                print("-",subj)
            print()
        case 6:
            print("Exit! Thank you for using Student Data Organizer.") 
            break
        case _:
            print("Invalid choice! Choose from the given options only.\n")