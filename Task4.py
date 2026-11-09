# Create an empty set and perform these operations:
# 1. Add five numbers to the set.
# 2. Remove one number using remove().
# 3. Add two more numbers using update().
# 4. Remove an element using discard().
# 5. Check whether a particular number exists in the set.
# 6. Display the final set.

my_set=set()
for i in range(0,6):
    value=int(input("Enter five numbers : "))
    my_set.add(value)
my_set.remove(23)
my_set.update([45,56])
my_set.discard(45)
if 23 in my_set:
    print("Number is peresent in set")
else:
    print("Number is not present .")
print(my_set)
