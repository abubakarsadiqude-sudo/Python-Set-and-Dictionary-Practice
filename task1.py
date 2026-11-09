# #ask 1: Remove Duplicate Elements (Easy)
# Create a Python program that:
# 1. Takes 10 numbers from the user.
# 2. Stores them in a list.
# 3. Converts the list into a set.
# 4. Displays the set without duplicate values

list=[]
for i in range(0,11):
    value=int(input("Enter ten numbers : "))
    list.append(value)
my_set=set(list)
print(my_set)