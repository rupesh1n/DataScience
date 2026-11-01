"""
Isosceles Triangle Module

This module provides the IsoscelesTriangle class for calculations involving isosceles triangles.
An isosceles triangle has two sides of equal length.
"""

import math


class IsoscelesTriangle:
    """
    A class to represent an isosceles triangle.
    
    An isosceles triangle has two sides of equal length (the equal sides) 
    and one side of different length (the base).
    
    Attributes:
        equal_side (float): The length of the two equal sides.
        base (float): The length of the base (the different side).
        height (float): The height from the base to the opposite vertex (calculated).
    """
    
    def __init__(self, equal_side, base):
        """
        Initialize an IsoscelesTriangle with equal sides and base.
        
        Args:
            equal_side (float): The length of the two equal sides. Must be positive.
            base (float): The length of the base. Must be positive.
            
        Raises:
            ValueError: If equal_side or base is not positive, or if the sides 
                       don't form a valid triangle.
            
        Note:
            The triangle inequality theorem requires that the sum of any two sides 
            must be greater than the third side. For an isosceles triangle:
            2 × equal_side > base
            
        Example:
            >>> triangle = IsoscelesTriangle(5, 6)
            >>> triangle.equal_side
            5
            >>> triangle.base
            6
        """
        if equal_side <= 0 or base <= 0:
            raise ValueError("Equal side and base must be positive numbers")
        
        # Check triangle inequality: 2 * equal_side must be > base
        if 2 * equal_side <= base:
            raise ValueError("The given sides do not form a valid triangle")
        
        self.equal_side = equal_side
        self.base = base
        
        # Calculate height using Pythagorean theorem
        # Height splits the base into two equal parts
        self.height = math.sqrt(equal_side**2 - (base / 2)**2)
    
    def area(self):
        """
        Calculate the area of the isosceles triangle.
        
        The area can be calculated using:
        Area = (1/2) × base × height
        
        Where height is derived from the Pythagorean theorem:
        height = √(equal_side² - (base/2)²)
        
        Returns:
            float: The area of the triangle.
            
        Example:
            >>> triangle = IsoscelesTriangle(5, 6)
            >>> round(triangle.area(), 2)
            12.0
        """
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        """
        Calculate the perimeter of the isosceles triangle.
        
        The perimeter is the sum of all three sides:
        Perimeter = 2 × equal_side + base
        
        Returns:
            float: The perimeter of the triangle.
            
        Example:
            >>> triangle = IsoscelesTriangle(5, 6)
            >>> triangle.perimeter()
            16
        """
        return 2 * self.equal_side + self.base
    
    def __str__(self):
        """
        Return a string representation of the isosceles triangle.
        
        Returns:
            str: A formatted string describing the triangle.
        """
        return (f"Isosceles Triangle: equal_side={self.equal_side}, base={self.base}, "
                f"height={self.height:.2f}")
    
    def __repr__(self):
        """
        Return a detailed string representation for debugging.
        
        Returns:
            str: A string that can recreate the object.
        """
        return f"IsoscelesTriangle(equal_side={self.equal_side}, base={self.base})"
