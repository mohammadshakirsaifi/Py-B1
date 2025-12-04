# Task 1: Basic Mathematical Operations
# This program takes two numbers as input and performs basic arithmetic operations

def main():
    print("Task 1: Basic Mathematical Operations")
    print("=" * 40)
    
    try:
        # Taking input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("\n" + "=" * 40)
        print("Results:")
        print("=" * 40)
        
        # Performing arithmetic operations
        # Addition
        addition = num1 + num2
        print(f"Addition: {addition}")
        
        # Subtraction
        subtraction = num1 - num2
        print(f"Subtraction: {subtraction}")
        
        # Multiplication
        multiplication = num1 * num2
        print(f"Multiplication: {multiplication}")
        
        # Division with zero division check
        if num2 != 0:
            division = num1 / num2
            print(f"Division: {division}")
        else:
            print("Division: Cannot divide by zero!")
            
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
