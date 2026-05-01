filename= input("Enter the filename:")

try:
  with open(filename,"r") as file:
    content=file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
  print("Error! File does not exist.")

except PermissionError:
  print("Error! You dont have permission to access this file.")

except Exception as e:
  print("An unxcepted error occured.",e)

