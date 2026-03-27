numbers=[10,5,20,24,14,59]
print("Original List:",numbers)
#Access elements
print("First element:",numbers[0])
print("Last element:",numbers[-1])
#Add elements
numbers.append(30) #adds at the end
numbers.insert(1,7) #adds at a specific index
print("List after adding elements:",numbers)
#Remove elements
numbers.remove(24)
print("List after removing elements:",numbers)
removed_element=numbers.pop(4)
print("List after element removed using pop:",removed_element)
#Sorting list elements
numbers.sort()
print("Sorted list (ascending order):",numbers)
numbers.sort(reverse=True)
print("Sorted list (descending order):",numbers)
#Reverse list
numbers.reverse()
print("Reversed list:",numbers)
