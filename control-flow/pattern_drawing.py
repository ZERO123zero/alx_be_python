# pattern_drawing.py  

# Prompt the user for the size of the pattern  
size = int(input("Enter the size of the pattern: "))  

# Ensure the user inputs a positive integer  
if size <= 0:  
    print("Please enter a positive integer.")  
else:  
    # Use a while loop to iterate through each row  
    row = 0  
    while row < size:  
        # Use a for loop to print asterisks side by side  
        for col in range(size):  
            print("*", end="")  
        # Move to the next line after completing a row  
        print()  
        row += 1