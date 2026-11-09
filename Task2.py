# Create two sets:
# set_a = {10, 20, 30, 40, 50}set_b = {30, 40, 50, 60, 70}


# Perform the following operations:
# 1. Find the union of both sets.
# 2. Find the intersection.
# 3. Find the difference between set_a and set_b.
# 4. Find the symmetric difference.


set_a = {10, 20, 30, 40, 50}
set_b = {30, 40, 50, 60, 70}
set_union=set_a.union(set_b)
set_intersection=set_a.intersection(set_b)
set_diffirence=set_a.difference(set_b)
set_symetericDF=set_a.symmetric_difference(set_b)
print("Union = " , set_union)
print("Intersection = " , set_intersection)
print("Diffirence = " , set_diffirence)
print("Symeteric diffirence = " , set_symetericDF)
