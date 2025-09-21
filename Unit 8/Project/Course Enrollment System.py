#! +--------------------------+
#! | COURSE ENROLLMENT SYSTEM |
#! +--------------------------+

# List to store course details as tuples (course_name, course_code)
courses = []

# List to store enrollments as tuples (student_name, {course_codes})
enrollments = []


# Helper Functions
def find_course(course_code):
    for course in courses:
        if course[1] == course_code:
            return course
    return None


def find_enrollment(student_name):
    for enrollment in enrollments:
        if enrollment[0] == student_name:
            return enrollment
    return None



# Display Meny
def display_menu():
    print("\n---COURSE ENROLLMENT SYSTEM---")
    print("1. Add Course")
    print("2. Enroll Student")
    print("3. View Students in a Course")
    print("4. View Courses of a Student")
    print("5. Exit\n")

# 1. Main Function : add a course
def add_course():
    course_name = input("Enter Course Name: ").strip()
    course_code = input("Enter Course Code: ").strip()

    if not course_name or not course_code:
        print("Course name or code cannot be empty. Try again!")
        return

    if find_course(course_code):
        print(f"Course Code: {course_code} already exist. Kindly recheck the code and try again.")
        return

    courses.append((course_name, course_code))
    print(f"Course: '{course_name}' added successfully!")

# 2. Main Function : enroll a student in a course

def enroll_student():
    student_name = input("Enter Student Name: ").strip()
    course_code = input("Enter Course Code: ").strip()

    if not student_name or not course_code:
        print("Student name or code cannot be empty. Try again!")
        return

    if not find_course(course_code):
        print("Course not found. Please check the code and try again")
        return

    # (student_name, {course_codes})

    enrollment = find_enrollment(student_name)

    if enrollment:
        if course_code in enrollment[1]:
            print(f"{student_name} is already enrolled in '{course_code}'")
            return
        enrollment[1].add(course_code)
    else:
        enrollments.append((student_name, {course_code}))

    print(f"{student_name} enrolled in '{course_code}' successfully")


# 3. Main Function : view students in a course

def view_students_in_course():
    course_code = input("Enter Course Code: ").strip()
    course = find_course(course_code)

    print("\n====================================================")
    if not course:
        print(f"Course with code: '{course_code}' not found")
        print("====================================================\n")
        return



    print(f"Course: {course[0]} ({course_code})")
    print("====================================================")

    # (student_name, {course_codes})
    students = sorted([enrollment[0] for enrollment in enrollments if course_code in enrollment[1]])

    if students:
        print("Students Enrolled:")

        for i, student in enumerate(students, 1):
            print(f"\t{i}. {student}")
    else:
        print("No students are enrolled in this course.")

    print("====================================================\n")


# 4. Main Function : view courses a student is enrolled in

def view_courses_of_student():
    student_name = input("Enter Student Name: ").strip()
    enrollment = find_enrollment(student_name)

    print("\n====================================================")
    print(f"Student Name: {student_name}")
    print("====================================================\n")

    if not enrollment:
        print("This student is not enrolled in any course.")
        print("\n====================================================")
        return

    print("Enrolled Courses:")

    # courses    → (course_name, course_code)
    # enrollment → (student_name, {course_codes})

    for i, course_code in enumerate(sorted(enrollment[1]), 1):

        course_name = "Unknown Course"

        for course in courses:
            if course[1] == course_code:
                course_name = course[0]
                break

        print(f"\t{i}. {course_name} ({course_code})")

    print("====================================================\n")


# Main Driver Code
while True:
    display_menu()

    choice = input("Enter Your Choice: ").strip()

    match choice:
        case "1":
            add_course()
        case "2":
            enroll_student()
        case "3":
            view_students_in_course()
        case "4":
            view_courses_of_student()
        case "5":
            print("Exiting the system!")
            break
        case _:
            print("Invalid Choice! Please enter a valid option.")