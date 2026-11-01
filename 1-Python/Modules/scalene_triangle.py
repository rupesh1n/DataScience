"""
Scalene Triangle Module

This module provides the ScaleneTriangle class for calculations involving scalene triangles.
A scalene triangle has all three sides of different lengths.
"""

import math


class ScaleneTriangle:
    """
    A class to represent a scalene triangle.
    
    A scalene triangle has all three sides of different lengths.
    
    Attributes:
        side_a (float): The length of the first side.
        side_b (float): The length of the second side.
        side_c (float): The length of the third side.
    """
    
    def __init__(self, side_a, side_b, side_c):
        """
        Initialize a ScaleneTriangle with three sides.
        
        Args:
            side_a (float): The length of the first side. Must be positive.
            side_b (float): The length of the second side. Must be positive.
            side_c (float): The length of the third side. Must be positive.
            
        Raises:
            ValueError: If any side is not positive or if the sides don't form a valid triangle.
            
        Note:
            The triangle inequality theorem states that the sum of any two sides 
            must be greater than the third side.
            
        Example:
            >>> triangle = ScaleneTriangle(3, 4, 5)
            >>> triangle.side_a
            3
        """
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("All sides must be positive numbers")
        
        # Check triangle inequality theorem
        if (side_a + side_b <= side_c or 
            side_a + side_c <= side_b or 
            side_b + side_c <= side_a):
            raise ValueError("The given sides do not form a valid triangle")
        
        # Verify it's actually scalene (all sides different)
        if side_a == side_b or side_b == side_c or side_a == side_c:
            raise ValueError("Scalene triangle must have all different side lengths")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def area(self):
        """
        Calculate the area of the scalene triangle using Heron's formula.
        
        Heron's formula:
        1. Calculate semi-perimeter: s = (a + b + c) / 2
        2. Calculate area: Area = √[s(s-a)(s-b)(s-c)]
        
        Returns:
            float: The area of the triangle.
            
        Example:
            >>> triangle = ScaleneTriangle(3, 4, 5)
            >>> triangle.area()
            6.0
        """
        s = self.perimeter() / 2  # semi-perimeter
        area = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return area
    
    def perimeter(self):
        """
        Calculate the perimeter of the scalene triangle.
        
        The perimeter is the sum of all three sides:
        Perimeter = side_a + side_b + side_c
        
        Returns:
            float: The perimeter of the triangle.
            
        Example:
            >>> triangle = ScaleneTriangle(3, 4, 5)
            >>> triangle.perimeter()
            12
        """
        return self.side_a + self.side_b + self.side_c
    
    def __str__(self):
        """
        Return a string representation of the scalene triangle.
        
        Returns:
            str: A formatted string describing the triangle.
        """
        return (f"Scalene Triangle: side_a={self.side_a}, side_b={self.side_b}, "
                f"side_c={self.side_c}")
    
    def __repr__(self):
        """
        Return a detailed string representation for debugging.
        
        Returns:
            str: A string that can recreate the object.
        """
        return (f"ScaleneTriangle(side_a={self.side_a}, side_b={self.side_b}, "
                f"side_c={self.side_c})")
