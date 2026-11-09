# 🟡 Task 3: Student Marks Management (Medium)
# Create a dictionary containing the names and marks of five students.

# Example:
# students = {    "Ali": 85,    "Ahmed": 76,    "Usman": 92,    "Sara": 88,    "Ayesha": 95}


# Requirements:
# 1. Display all students and their marks.
# 2. Find the student with the highest marks.
# 3. Calculate the average marks.
# 4. Display students who scored above 80.
# 5. Ask the user for a student name and search for that student.
# 6. Update a student's marks.

students = {    "Ali": 85,    "Ahmed": 76,    "Usman": 92,    "Sara": 88,    "Ayesha": 95}
print(students)
hihest_student=max(students , key=students.get)
print(hihest_student)
sum=sum(students.values())
len=len(students)
print("Average : " , sum/len)
for name, marks in students.items():
    if marks > 80:
        print(name, ":", marks)
student_name = input("Enter student name: ")

if student_name in students:
    new_marks = int(input("Enter new marks: "))
    students[student_name] = new_marks

    print("Marks updated successfully!")
    print(students)
else:
    print("Student not found.")
