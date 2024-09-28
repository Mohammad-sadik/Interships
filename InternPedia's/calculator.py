def welcome():
    print("Welcome to simple console-based calculator application")
    print("You can perform addition, subtraction, multiplication, and division operation")
    print("="*50)
#1233
def operation():
    return input("Enter operator: '/', '*', '-', '+' (or) type 'exit' to quit: ")

def farewell():
    print("="*50)
    print("Thank you for using the simple calculator, Good Bye")
    print("="*50)

def addition(a, b):
    print("Addition of {} and {} is {}".format(a, b, a+b))

def subtraction(a, b):
    print("Subtraction of {} and {} is {}".format(a, b, a-b))

def multiplication(a, b):
    print("Multiplication of {} and {} is {}".format(a, b, a * b))

def division(a, b):
    if b != 0:
        print("Division of {} and {} is {}".format(a, b, a / b))
    else:
        print("Error: Division by zero is not allowed.")

def main():
    welcome()
    
    while True:
        op = operation()
        
        if op in ['+', '-', '*', '/']:
            try:
                a = float(input("Enter the first value: "))
                b = float(input("Enter the second value: "))
                
                if op == "+":
                    addition(a, b)
                elif op == "-":
                    subtraction(a, b)
                elif op == "*":
                    multiplication(a, b)
                elif op == "/":
                    division(a, b)
                    
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                
        elif op == "exit":
            farewell()
            break
        else:
            print("Invalid operation entered. Please try again.")

if __name__ == "__main__":
    main()

