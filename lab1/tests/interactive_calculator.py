"""
Interactive Calculator Application
Users can manually test the calculator by entering their own values.
This is a hands-on testing experience.
"""

from calculator import Calculator


def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 60)
    print("INTERACTIVE CALCULATOR - Manual Testing")
    print("=" * 60)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (Exponentiation)")
    print("6. Exit")
    print("=" * 60)


def get_numbers(operation_name):
    """Get two numbers from user input."""
    try:
        print(f"\n--- {operation_name} ---")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("❌ Error: Please enter valid numbers!")
        return None, None


def main():
    """Main application loop. Returns number of tests performed."""
    calc = Calculator()
    test_count = 0
    
    print("\n" + "=" * 60)
    print("Welcome to the Interactive Calculator Tester!")
    print("Test the calculator by entering your own values.")
    print("=" * 60)
    
    while True:
        display_menu()
        choice = input("Select operation (1-6): ").strip()
        
        if choice == "1":
            test_count += 1
            num1, num2 = get_numbers("ADDITION")
            if num1 is not None:
                result = calc.add(num1, num2)
                print(f"✓ Result: {num1} + {num2} = {result}")
                print(f"Test #{test_count} completed")
        
        elif choice == "2":
            test_count += 1
            num1, num2 = get_numbers("SUBTRACTION")
            if num1 is not None:
                result = calc.subtract(num1, num2)
                print(f"✓ Result: {num1} - {num2} = {result}")
                print(f"Test #{test_count} completed")
        
        elif choice == "3":
            test_count += 1
            num1, num2 = get_numbers("MULTIPLICATION")
            if num1 is not None:
                result = calc.multiply(num1, num2)
                print(f"✓ Result: {num1} * {num2} = {result}")
                print(f"Test #{test_count} completed")
        
        elif choice == "4":
            test_count += 1
            num1, num2 = get_numbers("DIVISION")
            if num1 is not None:
                try:
                    result = calc.divide(num1, num2)
                    print(f"✓ Result: {num1} / {num2} = {result}")
                    print(f"Test #{test_count} completed")
                except ValueError as e:
                    print(f"❌ Error: {e}")
                    print("This is EXPECTED behavior for division by zero!")
                    print(f"Test #{test_count} completed (Error Handling Test)")
        
        elif choice == "5":
            test_count += 1
            num1, num2 = get_numbers("POWER (EXPONENTIATION)")
            if num1 is not None:
                result = calc.power(num1, num2)
                print(f"✓ Result: {num1} ** {num2} = {result}")
                print(f"Test #{test_count} completed")
        
        elif choice == "6":
            print("\n" + "=" * 60)
            print(f"Thank you for testing! You completed {test_count} tests.")
            print("=" * 60)
            return test_count  # Return test count instead of breaking
        
        else:
            print("❌ Invalid choice. Please select 1-6.")


# Allow direct execution
if __name__ == "__main__":
    test_count = main()
    print(f"\nInteractive testing completed. Total tests: {test_count}")