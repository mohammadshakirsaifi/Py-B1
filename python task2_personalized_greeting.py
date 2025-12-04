# Task 2: Personalized Greeting
# This program takes user's first and last name and creates a personalized greeting

def main():
    print("Task 2: Personalized Greeting")
    print("=" * 40)
    
    # Taking input from user
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    
    # Validating input
    if not first_name or not last_name:
        print("Error: Both first name and last name are required!")
        return
    
    # Concatenating names
    full_name = f"{first_name} {last_name}"
    
    # Creating personalized greeting
    greeting = f"Hello, {full_name}! Welcome to the Python program."
    
    print("\n" + "=" * 40)
    print(greeting)
    print("=" * 40)

if __name__ == "__main__":
    main()
