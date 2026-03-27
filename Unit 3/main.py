from Temperature import Celsius_to_Fahrenheit
from Temperature import Fahrenheit_to_Celsius
from Temperature import Celsius_to_Kelvin

def main():
    while True:
        print("Temperature conversion options:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")

        try:
            choice = int(input("Enter your Choice (1-4):"))    
            if choice== 1:
                c=float(input("Enter temperature in Celsius:"))
                print("Fahrenheit:",Celsius_to_Fahrenheit.convert(c))

            elif choice==2:
                f=float(input("Enter temperature in Fahrenheit: "))
                print("Celsius:",Fahrenheit_to_Celsius.convert(f))    

            elif choice==3:
                c=float(input("Enter temperature in Celsius:"))
                print("Kelvin:",Celsius_to_Kelvin.convert(c))

            elif choice == 4:
                 print("Exiting program")
                 break


            else:
                print("Enter a valid choice.")    
                
        except ValueError:
            print("Invalid input! Pls eneter numeric value.")

if __name__=="__main__":
    main()            




                
