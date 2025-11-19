"""
Calculator Module - Simple arithmetic operations
This module provides basic mathematical operations for testing purposes.
"""

class Calculator:
    """A simple calculator class for basic arithmetic operations."""
    
    def add(self, a, b):
        """
        Add two numbers.
        Args:
            a: First number
            b: Second number
        Returns:
            Sum of a and b
        """
        return a + b
    
    def subtract(self, a, b):
        """
        Subtract b from a.
        Args:
            a: First number (minuend)
            b: Second number (subtrahend)
        Returns:
            Difference of a and b
        """
        return a - b
    
    def multiply(self, a, b):
        """
        Multiply two numbers.
        Args:
            a: First number
            b: Second number
        Returns:
            Product of a and b
        """
        return a * b
    
    def divide(self, a, b):
        """
        Divide a by b.
        Args:
            a: Dividend
            b: Divisor
        Returns:
            Quotient of a and b
        Raises:
            ValueError: If b is zero (division by zero)
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        """
        Raise a to the power of b.
        Args:
            a: Base number
            b: Exponent
        Returns:
            a raised to the power of b
        """
        return a ** b