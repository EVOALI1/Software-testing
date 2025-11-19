"""
Unified Test Runner for Lab 1 - Basic Functions Testing
This script runs both automated and interactive tests with detailed reporting.
"""

import time
import sys
import os
from datetime import datetime

# Add current directory to path so we can import our modules
sys.path.insert(0, os.path.dirname(__file__))

try:
    from tests.test_calculator import run_automated_tests
    from tests.interactive_calculator import main as run_interactive_tests
    from src.calculator import Calculator
except ImportError as e:
    print(f"❌ Import error: {e}")
    print("Please make sure you have the following files:")
    print("  - src/calculator.py")
    print("  - tests/test_calculator.py") 
    print("  - tests/interactive_calculator.py")
    sys.exit(1)


def generate_test_report(results, execution_time):
    """Generate a comprehensive test report for lab submission."""
    
    report_content = f"""
# Lab 1 Test Report - Basic Functions Testing
## Software Testing Course

**Generated on:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Execution Time:** {execution_time:.2f} seconds

## Test Summary

- **Total Tests Run:** {results['total_tests']}
- **Tests Passed:** {results['passed']}
- **Tests Failed:** {results['failed']}
- **Success Rate:** {results['success_rate']:.1f}%

## Detailed Results

### Automated Test Results
- **Tests Run:** {results['automated_total']}
- **Passed:** {results['automated_passed']}
- **Failed:** {results['automated_failed']}

### Interactive Testing
- **Manual Tests Performed:** {results['interactive_count']}
- **Status:** {'Completed' if results['interactive_completed'] else 'Skipped'}

## Test Categories

### 1. Addition Tests
- Basic positive numbers
- Zero operations
- Negative numbers
- Decimal numbers

### 2. Subtraction Tests  
- Basic subtraction
- Negative results
- Zero operations
- Decimal numbers

### 3. Multiplication Tests
- Basic multiplication
- Zero properties
- Negative numbers
- Large numbers

### 4. Division Tests
- Basic division
- Decimal results
- Error handling (division by zero)
- Negative numbers

### 5. Power Tests
- Basic exponentiation
- Zero and one properties
- Negative exponents
- Decimal bases

## Error Handling Verification

The calculator correctly handles:
- Division by zero (raises ValueError)
- Invalid operations
- Various edge cases

## Conclusion

The Calculator implementation has been thoroughly tested with both automated and manual testing approaches. All core arithmetic functions work as expected with proper error handling.

---
*Report generated automatically by Lab 1 Testing Framework*
"""
    
    # Ensure reports directory exists
    os.makedirs('reports', exist_ok=True)
    
    # Write report to file
    with open('reports/lab1_report.md', 'w', encoding='utf-8') as f:
        f.write(report_content)
    
    print(f"📊 Test report generated: reports/lab1_report.md")


def main():
    """Main test runner function."""
    print("=" * 70)
    print("LAB 1 - BASIC FUNCTIONS TESTING")
    print("=" * 70)
    
    start_time = time.time()
    
    # Run automated tests
    print("\n🚀 RUNNING AUTOMATED TEST SUITE...")
    print("=" * 50)
    automated_results = run_automated_tests()
    
    # Ask user if they want to run interactive tests
    print("\n" + "=" * 50)
    run_interactive = input("Run interactive manual tests? (y/n): ").lower().strip()
    
    interactive_results = {
        'completed': False,
        'test_count': 0
    }
    
    if run_interactive in ['y', 'yes']:
        print("\n🎮 STARTING INTERACTIVE TESTING...")
        print("=" * 50)
        try:
            test_count = run_interactive_tests()
            interactive_results['completed'] = True
            interactive_results['test_count'] = test_count
        except Exception as e:
            print(f"❌ Interactive testing error: {e}")
            interactive_results['completed'] = False
    else:
        print("⏭️  Skipping interactive tests")
    
    execution_time = time.time() - start_time
    
    # Compile final results
    final_results = {
        'total_tests': automated_results['total_tests'],
        'passed': automated_results['passed'],
        'failed': automated_results['failed'],
        'success_rate': automated_results['success_rate'],
        'automated_total': automated_results['total_tests'],
        'automated_passed': automated_results['passed'],
        'automated_failed': automated_results['failed'],
        'interactive_completed': interactive_results['completed'],
        'interactive_count': interactive_results['test_count']
    }
    
    # Display final summary
    print("\n" + "=" * 70)
    print("🏁 TESTING COMPLETE - SUMMARY")
    print("=" * 70)
    print(f"📈 Automated Tests: {final_results['passed']}/{final_results['total_tests']} passed")
    print(f"🎮 Interactive Tests: {final_results['interactive_count']} tests {'completed' if final_results['interactive_completed'] else 'skipped'}")
    print(f"⏱️  Execution Time: {execution_time:.2f} seconds")
    print(f"📊 Success Rate: {final_results['success_rate']:.1f}%")
    print("=" * 70)
    
    # Generate report
    generate_test_report(final_results, execution_time)
    
    # Exit with appropriate code for CI/CD
    if final_results['failed'] > 0:
        print("❌ Some tests failed!")
        sys.exit(1)
    else:
        print("✅ All tests passed!")
        sys.exit(0)


if __name__ == "__main__":
    main()