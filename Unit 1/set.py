# creating and access set element

my_set = {10,20,30,40}
print(my_set)
if 30 in my_set:
    print("30 is in the set")

# union of the set
set1 = {1,2,3,4}
set2 = {3,4,2,5}
union_set = set1|set2
print(union_set)

#intersection of the element
intersection_set = set1&set2
print(intersection_set)

#difference of the element
difference_set = set1- set2
print(difference_set)
