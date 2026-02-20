set1={1,2,3,4,5}
set2={4,5,6,7,8}

#accessing elements
print("Set 1 elements:")
for elements in set1:
    print(elements,end="")
print("Set 2 elements:")
for elements in set2:
    print(elements,end="")

#Union of elements
union=set1.union(set2)
print(" Union of two sets:",union)

#Intersection of elements
intersection_set=set1.intersection(set2)
print("Intersection of set1 and set2:",intersection_set)

#Difference of the elements
difference_set=set1.difference(set2)
print("Difference of set1 and set2:", difference_set)




