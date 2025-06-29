#! +---------------------------------+
#! | STUDENT GRADE MANAGEMENT SYSTEM |
#! +---------------------------------+

def display_menu():
    print("\nStudent Grade Management System")
    print("1. Add Student")
    print("2. Show All Student")
    print("3. Search Student")
    print("4. Update Student Grade")
    print("5. Delete Student")
    print("6. Exit")
    print()


students = []


def add_student(student_list):
    name = input("Enter student's name: ").strip()

    for student in student_list:
        if student[0].lower() == name.lower():
            print("ERROR: Student with this name already exists!")
            return

    grade = input("Enter student's grade: ").strip()

    student = (name, grade)
    student_list.append(student)
    print("Student Added Successfully!")


def show_students(student_list):
    if len(student_list) == 0:
        print("No students to display")
    else:
        print("\nList of students")
        print("=" * 30)
        for student in student_list:
            print("Name: ", student[0], ", Grade: ", student[1])
        print("=" * 30)


def search_student(student_list):
    search_name = input("Enter student's name to search: ")

    # [("amar", 30), (), ()]
    for student in student_list:
        if student[0].lower() == search_name.lower():
            print(f"Student Found! Name: {student[0]}, Grade: {student[1]}")
            return
    else:
        print("Student Not Found!")


def update_student(student_list):
    update_name = input("Enter student's name to change grade: ")

    # [("amar", 30), (), ()]
    for i in range(len(student_list)):
        if student_list[i][0].lower() == update_name.lower():
            new_grade = input("Enter new grade for " + student_list[i][0] +": ")
            student_list[i] = (student_list[i][0], new_grade)
            print("Grade Update Successfully")
            return
    else:
        print("Student Not Found.")


def delete_student(student_list):

    delete_name = input("Enter Student's Name to Delete: ")

    for i in range(len(student_list)):
        if student_list[i][0].lower() == delete_name.lower():
            print("Deleting Student: ", student_list[i][0])
            del student_list[i]
            print("Student Deleted Successfully!")
            return
    else:
        print("Student Not Found.")


while True:
    display_menu()
    choice = input("Enter Your Choice: ")

    match choice:
        case "1":
            add_student(students)
        case "2":
            show_students(students)
        case "3":
            search_student(students)
        case "4":
            update_student(students)
        case "5":
            delete_student(students)
        case "6":
            print("Exiting Program. Goodbye!")
            break
        case _:
            print("Invalid Choice. Please select a valid option.")













