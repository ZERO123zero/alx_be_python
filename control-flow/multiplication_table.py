# multiplication_table.py  

# Prompt the user for a number  
number = int(input("Enter a number to see its multiplication table: "))  

# Generate and print the multiplication table  
print(f"\nMultiplication table of {number}:")  

for i in range(1, 11):  
    product = number * i  
    print(f"{number} * {i} = {product}")