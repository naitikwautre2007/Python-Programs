file=open("File_Handling","w")
file.write("Hello! This is my first line in the file.\n")
file.write("File handling demonstration.\n")
file.close()
print("Data written successfully.\n")

file=open("File_Handling","r")
print("Reading file contents:")
content=file.read()
print(content)
file.close()
print("Data read succefully!\n")

file=open("File_Handling","a")
file.write("This is appended line.\n")
file.close()

print("Data appended successfully.\n")

file=open("File_Handling","r")
print("Updated file contents:")
updated_content=file.read()
print(updated_content)
file.close()