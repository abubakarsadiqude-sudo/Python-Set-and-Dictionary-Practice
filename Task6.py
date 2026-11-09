# Task 1: Student Information (Basic)
# Create a Python dictionary to store the following student information:
# - Name
# - Age
# - University
# - Department
# - Semester
# - CGPA
# Requirements:
# 1. Create a dictionary containing the information.
# 2. Display all dictionary keys.
# 3. Display all dictionary values.
# 4. Update the student's CGPA.
# 5. Add a new key called email.
# 6. Remove the age key.

Student_dic={
    "name" : "Abubakar" ,
    "age" : 18,
    "university":"KFUEIT",
    "semester": 1,
    "CGPA":3.65
}
print(Student_dic.keys())
print(Student_dic.values())
Student_dic.update({"CGPA": 3.50})
Student_dic.update({"email": "abubakar@gmail.com"})
Student_dic.pop("age")
print(Student_dic)
