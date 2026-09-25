print("Welcome to the Student Records System!")

student_records = {}

def add_student(name, Reg, courses):
    if name in student_records:
        print(f"Student '{name}' already exists.")
        return
    student_records[name] = {"Reg.No": Reg, "grades": {}, "courses": courses}
    print(f"Student '{name}' added successfully.")

def add_grade(name, course, grade):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return

    if course not in student_records[name]["courses"]:
        print(f"Student '{name}' is not enrolled in {course}.")
        return

    student_records[name]["grades"][course] = grade
    print(f"Grade {grade} added for {course} for student '{name}'.")

def is_enrolled(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    return course in student_records[name]["courses"]

def list_students_by_course(course):
    students_in_course = []
    for name, details in student_records.items():
        if course in details["courses"]:
            students_in_course.append(name)
    return students_in_course

def add_course(name, course):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return
    student_records[name]["courses"].append(course)
    print(f"Course '{course}' added for student '{name}'.")

# Display menu
print("\nMenu:")
print("1. Add a new student")
print("2. Add a grade")
print("3. View all student records")
print("4. Check course enrollment")
print("5. List students by course")
print("6. Add a course")
print("7. Exit")

while True:

    choice = input("\nEnter your choice: ")

    if choice == "1":
        # Add a new student
        name = input("Enter student name: ").strip()
        Reg = input("Enter student Reg.No: ").strip()
        courses = [course.strip() for course in input("Enter courses separated by commas: ").split(",")]

        add_student(name, Reg, courses)


    elif choice == "2":
        # Adding grade in a course
        name = input("Enter student name: ").strip()
        course = input("Enter course name: ").strip()
        grade = input("Enter grade: ").strip() # Grades in character format (Ex. A+,A,B,etc.)

        add_grade(name, course, grade)

    elif choice == "3":
        # View all student records
        if len(student_records) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")

            for name, details in student_records.items():
                print(f"\nName: {name}")
                print(f"Reg.No: {details['Reg.No']}")
                print(f"Enrolled Courses: {details['courses']}")
                print(f"Grades: {details['grades']}")

    elif choice == "4":
        # Check course enrollment
        name = input("Enter student name: ").strip()
        course = input("Enter course name: ").strip()

        if is_enrolled(name, course):
            print(f"{name} is enrolled in {course}.")
        else:
            print(f"{name} is not enrolled in {course}.")

    elif choice == "5":
        # List students by course
        course = input("Enter course name: ").strip()

        students = list_students_by_course(course)

        if len(students) == 0:
            print("No students found for this course.")
        else:
            print("Students enrolled in this course:")
            for student in students:
                print(student)

    elif choice == "6":
        # Add a course
        name = input("Enter student name: ").strip()
        course = input("Enter course name: ").strip()

        add_course(name, course)

    elif choice == "7":
        # Exit
        print("Exiting the Student Records System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
