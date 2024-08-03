

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

def remainder(num1, num2):
    return num1 % num2

def square(num):
    return num * num

def cube(num):
    return num * num * num

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Remainder")
    print("6. Square of a number")
    print("7. Cube of a number")
    print("8. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '8':
        print("You chose to exit, goodbye!")
        break
    
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Addition of {num1} and {num2} is {addition(num1, num2)}")
        elif choice == '2':
            print(f"Subtraction of {num1} and {num2} is {subtraction(num1, num2)}")
        elif choice == '3':
            print(f"Multiplication of {num1} and {num2} is {multiplication(num1, num2)}")
        elif choice == '4':
            print(f"Division of {num1} and {num2} is {division(num1, num2)}")
        elif choice == '5':
            print(f"Remainder of {num1} and {num2} is {remainder(num1, num2)}")
    
    elif choice in ['6', '7']:
        num = float(input("Enter the number: "))
        
        if choice == '6':
            print(f"Square of {num} is {square(num)}")
        elif choice == '7':
            print(f"Cube of {num} is {cube(num)}")
    else:
        print("Invalid input. Please enter a number between 1 and 8.")

