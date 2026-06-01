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
git clone https://github.com/Dhruvvv0320/.git
```

### Navigate to Project Folder

```bash
cd student-data-organizer
```

### Run the Program

```bash
python try.py
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

Replace with screenshot:

```md
![Main Menu](images/main-menu.png)
```

---

### Add Student

Replace with screenshot:

```md
![Add Student](images/add-student.png)
```

---

### Display Students

Replace with screenshot:

```md
![Display Students](images/display-students.png)
```

---

### Update Student

Replace with screenshot:

```md
![Update Student](images/update-student.png)
```

---

### Delete Student

Replace with screenshot:

```md
![Delete Student](images/delete-student.png)
```

---

### Subjects Offered

Replace with screenshot:

```md
![Subjects](images/subjects.png)
```

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
