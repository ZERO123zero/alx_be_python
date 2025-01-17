def match_case_calculator():  
    # Prompt for user input  
    num1 = float(input("Enter the first number: "))  
    num2 = float(input("Enter the second number: "))  
    
    # Ask for the operation  
    operation = input("Choose the operation (+, -, *, /): ")  

    # Perform calculation using match case  
    match operation:  
        case '+':  
            result = num1 + num2  
            print(f"The result is {result}.")  
        case '-':  
            result = num1 - num2  
            print(f"The result is {result}.")  
        case '*':  
            result = num1 * num2  
            print(f"The result is {result}.")  
        case '/':  
            if num2 == 0:  
                print("Cannot divide by zero.")  
            else:  
                result = num1 / num2  
                print(f"The result is {result}.")  
        case _:  
            print("Invalid operation. Please choose +, -, *, or /.")  

# Run the calculator  
if __name__ == "__main__":  
    match_case_calculator()