# Task 5: Nested Dictionary – University Management (Very Hard)
# Create a university management system using a nested dictionary.

# Example:
# university = {    "Student1": {        "name": "Ali",        "age": 20,        "department": "AI",        "marks": {            "Python": 90,            "Math": 85,            "ICT": 88        }    },    "Student2": {        "name": "Ahmed",        "age": 21,        "department": "CS",        "marks": {            "Python": 78,            "Math": 82,            "ICT": 80        }    }}


# Requirements:
# 1. Display all students' information.
# 2. Search for a student using their ID.
# 3. Add a new student.
# 4. Update a student's subject marks.
# 5. Calculate each student's total marks.
# 6. Calculate each student's average marks.
# 7. Find the student with the highest average.
# 8. Display students whose average is greater than 80.
# 9. Delete a student using their ID.
university = {
    "Student1": {
        "name": "Ali",
        "age": 20,
        "department": "AI",
        "marks": {
            "Python": 90,
            "Math": 85,
            "ICT": 88
        }
    },

    "Student2": {
        "name": "Ahmed",
        "age": 21,
        "department": "CS",
        "marks": {
            "Python": 78,
            "Math": 82,
            "ICT": 80
        }
    }
}


while True:

    print("\n===== UNIVERSITY MANAGEMENT SYSTEM =====")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Add New Student")
    print("4. Update Student Marks")
    print("5. Calculate Total Marks")
    print("6. Calculate Average Marks")
    print("7. Find Highest Average Student")
    print("8. Display Students Above 80 Average")
    print("9. Delete Student")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    # 1. Display all students
    if choice == "1":

        for student_id, details in university.items():

            print("\nStudent ID:", student_id)
            print("Name:", details["name"])
            print("Age:", details["age"])
            print("Department:", details["department"])
            print("Marks:", details["marks"])

    # 2. Search student
    elif choice == "2":

        student_id = input("Enter Student ID: ")

        if student_id in university:
            print("\nStudent Found!")
            print(university[student_id])

        else:
            print("Student Not Found!")

    # 3. Add new student
    elif choice == "3":

        student_id = input("Enter New Student ID: ")

        if student_id in university:
            print("Student ID Already Exists!")

        else:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            department = input("Enter Department: ")

            python_marks = int(input("Enter Python Marks: "))
            math_marks = int(input("Enter Math Marks: "))
            ict_marks = int(input("Enter ICT Marks: "))

            university[student_id] = {
                "name": name,
                "age": age,
                "department": department,
                "marks": {
                    "Python": python_marks,
                    "Math": math_marks,
                    "ICT": ict_marks
                }
            }

            print("Student Added Successfully!")

    # 4. Update student marks
    elif choice == "4":

        student_id = input("Enter Student ID: ")

        if student_id in university:

            subject = input("Enter Subject Name: ")

            if subject in university[student_id]["marks"]:

                new_marks = int(input("Enter New Marks: "))

                university[student_id]["marks"][subject] = new_marks

                print("Marks Updated Successfully!")

            else:
                print("Subject Not Found!")

        else:
            print("Student Not Found!")

    # 5. Calculate total marks
    elif choice == "5":

        for student_id, details in university.items():

            total = sum(details["marks"].values())

            print(details["name"], "Total Marks:", total)

    # 6. Calculate average marks
    elif choice == "6":

        for student_id, details in university.items():

            marks = details["marks"]

            total = sum(marks.values())

            average = total / len(marks)

            print(details["name"], "Average:", average)

    # 7. Find highest average student
    elif choice == "7":

        highest_student = None
        highest_average = 0

        for student_id, details in university.items():

            marks = details["marks"]

            average = sum(marks.values()) / len(marks)

            if average > highest_average:

                highest_average = average
                highest_student = details["name"]

        if highest_student is not None:
            print("Highest Average Student:", highest_student)
            print("Average Marks:", highest_average)

        else:
            print("No Students Available!")

    # 8. Students above 80 average
    elif choice == "8":

        for student_id, details in university.items():

            marks = details["marks"]

            average = sum(marks.values()) / len(marks)

            if average > 80:

                print(details["name"], "Average:", average)

    # 9. Delete student
    elif choice == "9":

        student_id = input("Enter Student ID: ")

        if student_id in university:

            del university[student_id]

            print("Student Deleted Successfully!")

        else:
            print("Student Not Found!")

    # 10. Exit
    elif choice == "10":

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")