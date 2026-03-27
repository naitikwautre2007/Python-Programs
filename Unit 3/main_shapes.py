import Shapes

print("Choice:")
print("1.Circle")
print("2.Rectangle")
print("3.Triangle")

choice=int(input("Enter your Choice(1-3):"))

if choice==1:
    r=float(input("Enter radius:"))
    
    print(" Area circle:",Shapes.area_of_circle(r))
elif choice==2:
    l=float(input("Enter Lenght:"))
    w=float(input("Enter Width:"))
    print("Area Rectangle:", Shapes.area_of_rectangle(l,w))
elif choice==3:
    b=float(input("Enter Base:"))
    h=float(input("Enter Height:"))
    print("Area Triangle:", Shapes.area_of_triangle(b,h))  
else:
    print("Invalid Choice!")    

