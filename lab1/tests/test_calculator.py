"""
Test Suite for Calculator Module - Lab 1: Basic Functions Testing
This module contains manual test functions to verify calculator operations.
Tests cover: basic operations, boundary values, negative numbers, and error handling.
"""

from calculator import Calculator

# Initialize calculator object
calc = Calculator()

# Test counter variables for reporting
tests_run = 0
tests_passed = 0
tests_failed = 0
failed_tests = []


def run_test(test_name, actual, expected):
    """
    Helper function to run a test and track results.
    Args:
        test_name: Name of the test
        actual: Actual result from calculator
        expected: Expected result
    Returns:
        True if test passed, False if failed
    """
    global tests_run, tests_passed, tests_failed, failed_tests
    
    tests_run += 1
    
    # Check if actual matches expected (with small tolerance for floats)
    if isinstance(expected, float):
        passed = abs(actual - expected) < 0.0001
    else:
        passed = actual == expected
    
    if passed:
        tests_passed += 1
        print(f"✓ PASS: {test_name}")
        print(f"  Expected: {expected}, Got: {actual}\n")
        return True
    else:
        tests_failed += 1
        failed_tests.append(test_name)
        print(f"✗ FAIL: {test_name}")
        print(f"  Expected: {expected}, Got: {actual}\n")
        return False


def run_automated_tests():
    """
    Run all automated tests and return results.
    Returns:
        dict: Test results summary
    """
    global tests_run, tests_passed, tests_failed, failed_tests
    
    # Reset counters in case function is called multiple times
    tests_run = 0
    tests_passed = 0
    tests_failed = 0
    failed_tests = []
    
    # =====================================================
    # ADDITION TESTS
    # =====================================================
    print("=" * 60)
    print("ADDITION TESTS")
    print("=" * 60 + "\n")

    # Test Case 1.1: Basic positive numbers
    run_test("Addition: 5 + 3", calc.add(5, 3), 8)

    # Test Case 1.2: Positive numbers with different values
    run_test("Addition: 10 + 20", calc.add(10, 20), 30)

    # Test Case 1.3: Zero as one operand
    run_test("Addition: 0 + 5", calc.add(0, 5), 5)

    # Test Case 1.4: Both zeros
    run_test("Addition: 0 + 0", calc.add(0, 0), 0)

    # Test Case 1.5: Negative numbers
    run_test("Addition: -5 + 3", calc.add(-5, 3), -2)

    # Test Case 1.6: Two negative numbers
    run_test("Addition: -5 + -3", calc.add(-5, -3), -8)

    # Test Case 1.7: Large numbers
    run_test("Addition: 1000000 + 2000000", calc.add(1000000, 2000000), 3000000)

    # Test Case 1.8: Decimal numbers
    run_test("Addition: 1.5 + 2.5", calc.add(1.5, 2.5), 4.0)


    # =====================================================
    # SUBTRACTION TESTS
    # =====================================================
    print("=" * 60)
    print("SUBTRACTION TESTS")
    print("=" * 60 + "\n")

    # Test Case 2.1: Basic positive numbers
    run_test("Subtraction: 10 - 5", calc.subtract(10, 5), 5)

    # Test Case 2.2: Result is negative
    run_test("Subtraction: 5 - 10", calc.subtract(5, 10), -5)

    # Test Case 2.3: Subtract zero
    run_test("Subtraction: 10 - 0", calc.subtract(10, 0), 10)

    # Test Case 2.4: Subtract from zero
    run_test("Subtraction: 0 - 10", calc.subtract(0, 10), -10)

    # Test Case 2.5: Both zeros
    run_test("Subtraction: 0 - 0", calc.subtract(0, 0), 0)

    # Test Case 2.6: Negative numbers
    run_test("Subtraction: -5 - 3", calc.subtract(-5, 3), -8)

    # Test Case 2.7: Two negative numbers
    run_test("Subtraction: -5 - (-3)", calc.subtract(-5, -3), -2)

    # Test Case 2.8: Decimal numbers
    run_test("Subtraction: 5.5 - 2.3", calc.subtract(5.5, 2.3), 3.2)


    # =====================================================
    # MULTIPLICATION TESTS
    # =====================================================
    print("=" * 60)
    print("MULTIPLICATION TESTS")
    print("=" * 60 + "\n")

    # Test Case 3.1: Basic positive numbers
    run_test("Multiplication: 5 * 4", calc.multiply(5, 4), 20)

    # Test Case 3.2: Multiply by zero
    run_test("Multiplication: 5 * 0", calc.multiply(5, 0), 0)

    # Test Case 3.3: Zero times zero
    run_test("Multiplication: 0 * 0", calc.multiply(0, 0), 0)

    # Test Case 3.4: Multiply by one
    run_test("Multiplication: 5 * 1", calc.multiply(5, 1), 5)

    # Test Case 3.5: Negative numbers
    run_test("Multiplication: -5 * 4", calc.multiply(-5, 4), -20)

    # Test Case 3.6: Two negative numbers
    run_test("Multiplication: -5 * -4", calc.multiply(-5, -4), 20)

    # Test Case 3.7: Large numbers
    run_test("Multiplication: 1000 * 2000", calc.multiply(1000, 2000), 2000000)

    # Test Case 3.8: Decimal numbers
    run_test("Multiplication: 2.5 * 4", calc.multiply(2.5, 4), 10.0)


    # =====================================================
    # DIVISION TESTS
    # =====================================================
    print("=" * 60)
    print("DIVISION TESTS")
    print("=" * 60 + "\n")

    # Test Case 4.1: Basic positive numbers
    run_test("Division: 20 / 4", calc.divide(20, 4), 5.0)

    # Test Case 4.2: Division resulting in decimal
    run_test("Division: 10 / 3", calc.divide(10, 3), 10/3)  # Use Python's calculation

    # Test Case 4.3: Divide by one
    run_test("Division: 10 / 1", calc.divide(10, 1), 10.0)

    # Test Case 4.4: Divide zero
    run_test("Division: 0 / 5", calc.divide(0, 5), 0.0)

    # Test Case 4.5: Negative numbers
    run_test("Division: -20 / 4", calc.divide(-20, 4), -5.0)

    # Test Case 4.6: Two negative numbers
    run_test("Division: -20 / -4", calc.divide(-20, -4), 5.0)

    # Test Case 4.7: Division by zero - Error handling
    print("Division: 10 / 0 (Error Handling Test)")
    try:
        result = calc.divide(10, 0)
        print(f"✗ FAIL: Division by Zero Error Handling")
        print(f"  Expected: ValueError exception, Got: {result}\n")
        tests_run += 1
        tests_failed += 1
        failed_tests.append("Division by Zero Error Handling")
    except ValueError as e:
        if "Cannot divide by zero" in str(e):
            print(f"✓ PASS: Division by Zero Error Handling")
            print(f"  Expected: ValueError exception, Got: {e}\n")
            tests_run += 1
            tests_passed += 1
        else:
            print(f"✗ FAIL: Division by Zero Error Handling")
            print(f"  Expected: 'Cannot divide by zero' message, Got: {e}\n")
            tests_run += 1
            tests_failed += 1
            failed_tests.append("Division by Zero Error Handling")

    # Test Case 4.8: Another division by zero test
    print("Division: 0 / 0 (Error Handling Test)")
    try:
        result = calc.divide(0, 0)
        print(f"✗ FAIL: Division by Zero (0/0) Error Handling")
        print(f"  Expected: ValueError exception, Got: {result}\n")
        tests_run += 1
        tests_failed += 1
        failed_tests.append("Division by Zero (0/0) Error Handling")
    except ValueError as e:
        if "Cannot divide by zero" in str(e):
            print(f"✓ PASS: Division by Zero (0/0) Error Handling")
            print(f"  Expected: ValueError exception, Got: {e}\n")
            tests_run += 1
            tests_passed += 1
        else:
            print(f"✗ FAIL: Division by Zero (0/0) Error Handling")
            print(f"  Expected: 'Cannot divide by zero' message, Got: {e}\n")
            tests_run += 1
            tests_failed += 1
            failed_tests.append("Division by Zero (0/0) Error Handling")


    # =====================================================
    # POWER TESTS
    # =====================================================
    print("=" * 60)
    print("POWER TESTS")
    print("=" * 60 + "\n")

    # Test Case 5.1: Basic positive numbers
    run_test("Power: 2 ** 3", calc.power(2, 3), 8)

    # Test Case 5.2: Power of zero exponent
    run_test("Power: 5 ** 0", calc.power(5, 0), 1)

    # Test Case 5.3: Power of one
    run_test("Power: 5 ** 1", calc.power(5, 1), 5)

    # Test Case 5.4: Zero to power
    run_test("Power: 0 ** 5", calc.power(0, 5), 0)

    # Test Case 5.5: Negative exponent
    run_test("Power: 2 ** -2", calc.power(2, -2), 0.25)

    # Test Case 5.6: Negative base
    run_test("Power: -2 ** 3", calc.power(-2, 3), -8)

    # Test Case 5.7: Large exponent
    run_test("Power: 2 ** 10", calc.power(2, 10), 1024)

    # Test Case 5.8: Decimal base and exponent
    run_test("Power: 2.5 ** 2", calc.power(2.5, 2), 6.25)


    # =====================================================
    # TEST SUMMARY REPORT
    # =====================================================
    print("\n" + "=" * 60)
    print("AUTOMATED TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests Run: {tests_run}")
    print(f"Tests Passed: {tests_passed}")
    print(f"Tests Failed: {tests_failed}")
    
    if tests_run > 0:
        success_rate = (tests_passed / tests_run) * 100
        print(f"Success Rate: {success_rate:.1f}%")
    else:
        success_rate = 0
        print(f"Success Rate: 0.0%")

    if tests_failed > 0:
        print(f"\nFailed Tests:")
        for test in failed_tests:
            print(f"  - {test}")

    print("=" * 60)
    
    # Return results for the unified test runner
    results = {
        'total_tests': tests_run,
        'passed': tests_passed,
        'failed': tests_failed,
        'success_rate': success_rate,
        'failed_tests': failed_tests.copy()
    }
    
    return results


# Make sure this only runs when executed directly, not when imported
if __name__ == "__main__":
    # This will run when you execute test_calculator.py directly
    print("🧪 Running Automated Tests Directly...")
    results = run_automated_tests()
    print(f"\nDirect execution summary: {results['passed']}/{results['total_tests']} tests passed")
    
    # Exit with proper code for CI/CD
    if results['failed'] > 0:
        exit(1)
    else:
        exit(0)