student={"name":"Naitik",
       "age":18,
       "college":"MIT ADT University",
       "course": "B.Tech CSE"}
print("Dictionery",student)

#Update dictionery 
student["age"]=19
student["Year"]= "First Year"
print("Updated Dictionery:", student )

#Removing elements 
student.pop("course")
print("After removing element:",student)

#Merging dictionaries
marks={"MFC": 80, "PL":91 } 
merged_dict= student | marks 
print("Merged dictionary:", merged_dict)
