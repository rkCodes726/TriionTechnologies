num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice= int(input("Enter your choice: "))
if choice==1:
    print("Addition: ", num1 + num2)
elif choice==2:
    print("Subtraction: ", num1 - num2)
elif choice==3:
    print("Multiplication: ", num1 * num2)
elif choice==4:
    if num2!=0:
        print("Division: ", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice! Please select a valid operation.")
