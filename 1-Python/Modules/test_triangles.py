"""
Unit tests for the Triangle Geometry Package

Run with: pytest test_triangles.py -v
"""

import pytest
import math
from triangle_geometry import RightTriangle, ScaleneTriangle, IsoscelesTriangle


class TestRightTriangle:
    """Test cases for RightTriangle class."""
    
    def test_initialization(self):
        """Test proper initialization of right triangle."""
        triangle = RightTriangle(3, 4)
        assert triangle.base == 3
        assert triangle.height == 4
        assert triangle.hypotenuse == 5.0
    
    def test_area_calculation(self):
        """Test area calculation."""
        triangle = RightTriangle(3, 4)
        assert triangle.area() == 6.0
        
        triangle2 = RightTriangle(6, 8)
        assert triangle2.area() == 24.0
    
    def test_perimeter_calculation(self):
        """Test perimeter calculation."""
        triangle = RightTriangle(3, 4)
        assert triangle.perimeter() == 12.0
        
        triangle2 = RightTriangle(5, 12)
        assert triangle2.perimeter() == 30.0
    
    def test_hypotenuse_calculation(self):
        """Test hypotenuse calculation using Pythagorean theorem."""
        triangle = RightTriangle(3, 4)
        assert triangle.hypotenuse == 5.0
        
        triangle2 = RightTriangle(8, 15)
        assert triangle2.hypotenuse == 17.0
    
    def test_negative_base(self):
        """Test that negative base raises ValueError."""
        with pytest.raises(ValueError, match="Base and height must be positive"):
            RightTriangle(-3, 4)
    
    def test_negative_height(self):
        """Test that negative height raises ValueError."""
        with pytest.raises(ValueError, match="Base and height must be positive"):
            RightTriangle(3, -4)
    
    def test_zero_base(self):
        """Test that zero base raises ValueError."""
        with pytest.raises(ValueError, match="Base and height must be positive"):
            RightTriangle(0, 4)
    
    def test_decimal_values(self):
        """Test with decimal values."""
        triangle = RightTriangle(2.5, 6.0)
        assert triangle.area() == 7.5
        assert abs(triangle.hypotenuse - 6.5) < 0.01


class TestScaleneTriangle:
    """Test cases for ScaleneTriangle class."""
    
    def test_initialization(self):
        """Test proper initialization of scalene triangle."""
        triangle = ScaleneTriangle(3, 4, 5)
        assert triangle.side_a == 3
        assert triangle.side_b == 4
        assert triangle.side_c == 5
    
    def test_area_calculation(self):
        """Test area calculation using Heron's formula."""
        triangle = ScaleneTriangle(3, 4, 5)
        assert abs(triangle.area() - 6.0) < 0.01
        
        triangle2 = ScaleneTriangle(7, 8, 9)
        assert abs(triangle2.area() - 26.83) < 0.01
    
    def test_perimeter_calculation(self):
        """Test perimeter calculation."""
        triangle = ScaleneTriangle(3, 4, 5)
        assert triangle.perimeter() == 12
        
        triangle2 = ScaleneTriangle(7, 8, 9)
        assert triangle2.perimeter() == 24
    
    def test_triangle_inequality_violation(self):
        """Test that violating triangle inequality raises ValueError."""
        with pytest.raises(ValueError, match="do not form a valid triangle"):
            ScaleneTriangle(1, 2, 10)
    
    def test_equal_sides_validation(self):
        """Test that equal sides raise ValueError for scalene."""
        with pytest.raises(ValueError, match="must have all different side lengths"):
            ScaleneTriangle(5, 5, 7)
        
        with pytest.raises(ValueError, match="must have all different side lengths"):
            ScaleneTriangle(5, 7, 5)
    
    def test_negative_side(self):
        """Test that negative sides raise ValueError."""
        with pytest.raises(ValueError, match="All sides must be positive"):
            ScaleneTriangle(-3, 4, 5)
    
    def test_zero_side(self):
        """Test that zero sides raise ValueError."""
        with pytest.raises(ValueError, match="All sides must be positive"):
            ScaleneTriangle(0, 4, 5)
    
    def test_decimal_values(self):
        """Test with decimal values."""
        triangle = ScaleneTriangle(3.5, 4.2, 5.1)
        assert triangle.perimeter() == 12.8
        assert triangle.area() > 0


class TestIsoscelesTriangle:
    """Test cases for IsoscelesTriangle class."""
    
    def test_initialization(self):
        """Test proper initialization of isosceles triangle."""
        triangle = IsoscelesTriangle(5, 6)
        assert triangle.equal_side == 5
        assert triangle.base == 6
        assert abs(triangle.height - 4.0) < 0.01
    
    def test_area_calculation(self):
        """Test area calculation."""
        triangle = IsoscelesTriangle(5, 6)
        assert abs(triangle.area() - 12.0) < 0.01
        
        triangle2 = IsoscelesTriangle(10, 12)
        assert abs(triangle2.area() - 48.0) < 0.01
    
    def test_perimeter_calculation(self):
        """Test perimeter calculation."""
        triangle = IsoscelesTriangle(5, 6)
        assert triangle.perimeter() == 16
        
        triangle2 = IsoscelesTriangle(10, 12)
        assert triangle2.perimeter() == 32
    
    def test_height_calculation(self):
        """Test height calculation using Pythagorean theorem."""
        triangle = IsoscelesTriangle(5, 6)
        # Height should be sqrt(5^2 - 3^2) = sqrt(25 - 9) = 4
        assert abs(triangle.height - 4.0) < 0.01
    
    def test_triangle_inequality_violation(self):
        """Test that violating triangle inequality raises ValueError."""
        with pytest.raises(ValueError, match="do not form a valid triangle"):
            IsoscelesTriangle(3, 10)
    
    def test_negative_equal_side(self):
        """Test that negative equal_side raises ValueError."""
        with pytest.raises(ValueError, match="must be positive"):
            IsoscelesTriangle(-5, 6)
    
    def test_negative_base(self):
        """Test that negative base raises ValueError."""
        with pytest.raises(ValueError, match="must be positive"):
            IsoscelesTriangle(5, -6)
    
    def test_zero_values(self):
        """Test that zero values raise ValueError."""
        with pytest.raises(ValueError, match="must be positive"):
            IsoscelesTriangle(0, 6)
        
        with pytest.raises(ValueError, match="must be positive"):
            IsoscelesTriangle(5, 0)
    
    def test_decimal_values(self):
        """Test with decimal values."""
        triangle = IsoscelesTriangle(7.5, 8.0)
        assert triangle.perimeter() == 23.0
        assert triangle.area() > 0


class TestStringRepresentations:
    """Test string representations for all triangle types."""
    
    def test_right_triangle_str(self):
        """Test string representation of right triangle."""
        triangle = RightTriangle(3, 4)
        result = str(triangle)
        assert "Right Triangle" in result
        assert "base=3" in result
        assert "height=4" in result
    
    def test_scalene_triangle_str(self):
        """Test string representation of scalene triangle."""
        triangle = ScaleneTriangle(3, 4, 5)
        result = str(triangle)
        assert "Scalene Triangle" in result
        assert "side_a=3" in result
    
    def test_isosceles_triangle_str(self):
        """Test string representation of isosceles triangle."""
        triangle = IsoscelesTriangle(5, 6)
        result = str(triangle)
        assert "Isosceles Triangle" in result
        assert "equal_side=5" in result
    
    def test_right_triangle_repr(self):
        """Test repr of right triangle."""
        triangle = RightTriangle(3, 4)
        result = repr(triangle)
        assert "RightTriangle" in result
        assert "3" in result
        assert "4" in result
    
    def test_scalene_triangle_repr(self):
        """Test repr of scalene triangle."""
        triangle = ScaleneTriangle(3, 4, 5)
        result = repr(triangle)
        assert "ScaleneTriangle" in result
    
    def test_isosceles_triangle_repr(self):
        """Test repr of isosceles triangle."""
        triangle = IsoscelesTriangle(5, 6)
        result = repr(triangle)
        assert "IsoscelesTriangle" in result


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
