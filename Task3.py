# You have two groups of students:
# python_students = {"Ali", "Ahmed", "Sara", "Usman", "Ayesha"}
# ai_students = {"Sara", "Usman", "Zain", "Fatima", "Ali"}


# Write a program to:
# 1. Find students enrolled in both courses.
# 2. Find students enrolled only in Python.
# 3. Find students enrolled only in AI.
# 4. Find all unique students.
python_students = {"Ali", "Ahmed", "Sara", "Usman", "Ayesha"}
ai_students = {"Sara", "Usman", "Zain", "Fatima", "Ali"}


both_courses = python_students.intersection(ai_students)


only_python = python_students.difference(ai_students)


only_ai = ai_students.difference(python_students)


all_students = python_students.union(ai_students)


print("Students in Both Courses:", both_courses)
print("Students Only in Python:", only_python)
print("Students Only in AI:", only_ai)
print("All Unique Students:", all_students)
