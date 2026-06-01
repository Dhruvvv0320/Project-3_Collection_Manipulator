# 🎓 Student Data Organizer

A simple command-line based **Student Data Organizer** built with Python. This project allows users to manage student records by performing CRUD operations (Create, Read, Update, Delete) and view available subjects.

## 📌 Features

* Add new student records
* Display all student records
* Update student information
* Delete student records
* Display available subjects
* Store Date of Birth using Python's `datetime` module
* Menu-driven interface using `match-case`

---

## 🛠 Technologies Used

* Python 3.10+
* Datetime Module
* Lists
* Dictionaries
* Sets
* Match-Case Statements

---

## 📂 Student Record Structure

Each student is stored as a dictionary:

```python
student = {
    'id': 101,
    'name': 'Dhruv',
    'age': 23,
    'grade': 'A',
    'dob': '2003-01-03',
    'sub': {'Maths', 'Physics'}
}
```

---

## 🚀 How to Run

### Clone the Repository

```bash
[git clone https://github.com/Dhruvvv0320/.git](https://github.com/Dhruvvv0320/Project-3_Collection_Manipulator.git)
```

### Navigate to Project Folder

```bash
cd Collection_Manipulator.py
```

### Run the Program

```bash
python Collection_Manipulator.py
```

---

## 📋 Menu Options

```text
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
```

---

## 📸 Program Outputs

### Main Menu

<img width="1366" height="286" alt="image" src="https://github.com/user-attachments/assets/f91ae01d-91ea-4db6-96c2-1fcb5240dacb" />

---

### Add Student

<img width="1377" height="450" alt="image" src="https://github.com/user-attachments/assets/f3292eb6-808d-4398-8692-702ee73ba628" />

---

### Display Students

<img width="1363" height="266" alt="image" src="https://github.com/user-attachments/assets/8c6a44f3-1c59-4d24-bfa4-0e006ffb3545" />

---

### Update Student

<img width="1375" height="465" alt="image" src="https://github.com/user-attachments/assets/2e74ec7c-f31a-458d-807a-a59434089221" />

---

### Delete Student

<img width="1368" height="277" alt="image" src="https://github.com/user-attachments/assets/eeecc0fa-fc6d-43d3-85fc-90ff86f1a5a4" />

---

### Subjects Offered

<img width="1370" height="376" alt="image" src="https://github.com/user-attachments/assets/48e6ed26-e69b-4051-a525-9f0132c73b5a" />

---

## 🧪 Sample Output

```text
Welcome to the Student Data Organizer !

1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter Your Choice : 1

Enter student ID : 101
Enter student name : Dhruv
Enter student age : 19
Enter student grade : A
Enter your date of birth (DD-MM-YYYY) : 01-01-2006

Subject List :
Maths
Physics
Biology
Chemistry
English

Choose Subjects (comma-separated) : Maths,Physics

Student Added Successfully...!
```

---

## 📚 Concepts Practiced

* User Input Handling
* Data Structures

  * List
  * Dictionary
  * Set
* Loops
* Conditional Statements
* Match-Case
* Date Handling with Datetime
* CRUD Operations

---

## 🔮 Future Improvements

* Save records in a file (JSON/CSV)
* Data persistence after program closes
* Search student by ID
* Input validation
* Sorting records
* GUI version using Tkinter
* Database integration using SQLite

---

## 👨‍💻 Author

Dhruv Makwana

Built as a Python practice project to strengthen programming fundamentals and data structure concepts.
