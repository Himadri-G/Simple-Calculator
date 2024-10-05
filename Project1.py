# Simple Calculator:

# Disply menu

def show_menu():
    
    print("--SIMPLE CALCULATOR--")   
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiply")
    print("4: Divide")
    print("5: EXIT")
    
# Get numbers

def get_numbers():
    
    num1= (float(input("ENTER THE 1ST NUMBER: ")))
    num2= (float(input("ENTER THE 2ND NUMBER: ")))
    return num1,num2

# perform Calculation

def calculator():
    while True:
        show_menu()
        
        choice=input("ENTER YOUR CHOICE(1-5): ")
    
        if choice == '1':
            num1, num2 = get_numbers()
            
            print(f"THE RESULT OF {num1} + {num2} = {num1 + num2}")
        
        elif choice == '2':
            num1 ,num2 =get_numbers()
            
            print(f"THE RESULT OF {num1} - {num2} = {num1 - num2}")
            
        elif choice == '3':
            num1 ,num2 =get_numbers()
            
            print(f"THE RESULT OF {num1} * {num2} = {num1 * num2}")
        
        elif choice == '4':
            num1 ,num2 =get_numbers()
            if num2 != 0:
            
                print(f"THE RESULT OF {num1} / {num2} = {num1 / num2}")
            else:
                
                print("ERROR !.......DIVITION BY 0 IS NOT ALLOWED")
        
        elif choice == '5':
            
            print("EXIT.")
            
            break
        
        
        else:
            print("Invalid choice....Please choose a valide option.")
        
calculator()