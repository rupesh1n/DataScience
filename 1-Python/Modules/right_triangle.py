"""
Right-Angled Triangle Module

This module provides the RightTriangle class for calculations involving right-angled triangles.
"""

import math


class RightTriangle:
    """
    A class to represent a right-angled triangle.
    
    Attributes:
        base (float): The base of the right triangle (one of the perpendicular sides).
        height (float): The height of the right triangle (the other perpendicular side).
        hypotenuse (float): The hypotenuse of the right triangle (calculated automatically).
    """
    
    def __init__(self, base, height):
        """
        Initialize a RightTriangle with base and height.
        
        Args:
            base (float): The base of the right triangle. Must be positive.
            height (float): The height of the right triangle. Must be positive.
            
        Raises:
            ValueError: If base or height is not positive.
            
        Example:
            >>> triangle = RightTriangle(3, 4)
            >>> triangle.base
            3
            >>> triangle.height
            4
        """
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        
        self.base = base
        self.height = height
        self.hypotenuse = math.sqrt(base**2 + height**2)
    
    def area(self):
        """
        Calculate the area of the right-angled triangle.
        
        The area of a right-angled triangle is calculated using the formula:
        Area = (1/2) × base × height
        
        Returns:
            float: The area of the triangle.
            
        Example:
            >>> triangle = RightTriangle(3, 4)
            >>> triangle.area()
            6.0
        """
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        """
        Calculate the perimeter of the right-angled triangle.
        
        The perimeter is the sum of all three sides:
        Perimeter = base + height + hypotenuse
        
        Returns:
            float: The perimeter of the triangle.
            
        Example:
            >>> triangle = RightTriangle(3, 4)
            >>> triangle.perimeter()
            12.0
        """
        return self.base + self.height + self.hypotenuse
    
    def __str__(self):
        """
        Return a string representation of the right triangle.
        
        Returns:
            str: A formatted string describing the triangle.
        """
        return (f"Right Triangle: base={self.base}, height={self.height}, "
                f"hypotenuse={self.hypotenuse:.2f}")
    
    def __repr__(self):
        """
        Return a detailed string representation for debugging.
        
        Returns:
            str: A string that can recreate the object.
        """
        return f"RightTriangle(base={self.base}, height={self.height})"
