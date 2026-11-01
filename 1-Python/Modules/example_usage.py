"""
Example Usage of Triangle Geometry Package

This script demonstrates how to use all three triangle classes with various examples.
"""

from triangle_geometry import RightTriangle, ScaleneTriangle, IsoscelesTriangle


def demonstrate_right_triangle():
    """Demonstrate RightTriangle usage."""
    print("=" * 60)
    print("RIGHT-ANGLED TRIANGLE EXAMPLES")
    print("=" * 60)
    
    # Example 1: Classic 3-4-5 right triangle
    print("\nExample 1: Classic 3-4-5 triangle")
    rt1 = RightTriangle(3, 4)
    print(f"Triangle: {rt1}")
    print(f"Area: {rt1.area()}")
    print(f"Perimeter: {rt1.perimeter()}")
    
    # Example 2: Larger right triangle
    print("\nExample 2: Right triangle with base=6, height=8")
    rt2 = RightTriangle(6, 8)
    print(f"Triangle: {rt2}")
    print(f"Area: {rt2.area()}")
    print(f"Perimeter: {rt2.perimeter()}")
    
    # Example 3: Decimal values
    print("\nExample 3: Right triangle with decimal values")
    rt3 = RightTriangle(5.5, 7.2)
    print(f"Triangle: {rt3}")
    print(f"Area: {rt3.area():.2f}")
    print(f"Perimeter: {rt3.perimeter():.2f}")


def demonstrate_scalene_triangle():
    """Demonstrate ScaleneTriangle usage."""
    print("\n" + "=" * 60)
    print("SCALENE TRIANGLE EXAMPLES")
    print("=" * 60)
    
    # Example 1: Simple scalene triangle
    print("\nExample 1: Scalene triangle with sides 3, 4, 5")
    st1 = ScaleneTriangle(3, 4, 5)
    print(f"Triangle: {st1}")
    print(f"Area: {st1.area():.2f}")
    print(f"Perimeter: {st1.perimeter()}")
    
    # Example 2: Another scalene triangle
    print("\nExample 2: Scalene triangle with sides 7, 8, 9")
    st2 = ScaleneTriangle(7, 8, 9)
    print(f"Triangle: {st2}")
    print(f"Area: {st2.area():.2f}")
    print(f"Perimeter: {st2.perimeter()}")
    
    # Example 3: Decimal values
    print("\nExample 3: Scalene triangle with decimal values")
    st3 = ScaleneTriangle(5.5, 7.3, 8.9)
    print(f"Triangle: {st3}")
    print(f"Area: {st3.area():.2f}")
    print(f"Perimeter: {st3.perimeter():.2f}")


def demonstrate_isosceles_triangle():
    """Demonstrate IsoscelesTriangle usage."""
    print("\n" + "=" * 60)
    print("ISOSCELES TRIANGLE EXAMPLES")
    print("=" * 60)
    
    # Example 1: Isosceles triangle
    print("\nExample 1: Isosceles triangle with equal_side=5, base=6")
    it1 = IsoscelesTriangle(5, 6)
    print(f"Triangle: {it1}")
    print(f"Area: {it1.area():.2f}")
    print(f"Perimeter: {it1.perimeter()}")
    
    # Example 2: Another isosceles triangle
    print("\nExample 2: Isosceles triangle with equal_side=10, base=12")
    it2 = IsoscelesTriangle(10, 12)
    print(f"Triangle: {it2}")
    print(f"Area: {it2.area():.2f}")
    print(f"Perimeter: {it2.perimeter()}")
    
    # Example 3: Decimal values
    print("\nExample 3: Isosceles triangle with decimal values")
    it3 = IsoscelesTriangle(7.5, 8.2)
    print(f"Triangle: {it3}")
    print(f"Area: {it3.area():.2f}")
    print(f"Perimeter: {it3.perimeter():.2f}")


def demonstrate_error_handling():
    """Demonstrate error handling in triangle classes."""
    print("\n" + "=" * 60)
    print("ERROR HANDLING EXAMPLES")
    print("=" * 60)
    
    # Example 1: Invalid right triangle (negative values)
    print("\nExample 1: Attempting to create right triangle with negative base")
    try:
        rt = RightTriangle(-3, 4)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Example 2: Invalid scalene triangle (violates triangle inequality)
    print("\nExample 2: Attempting to create scalene triangle that violates triangle inequality")
    try:
        st = ScaleneTriangle(1, 2, 10)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Example 3: Invalid scalene triangle (equal sides)
    print("\nExample 3: Attempting to create scalene triangle with equal sides")
    try:
        st = ScaleneTriangle(5, 5, 7)
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Example 4: Invalid isosceles triangle
    print("\nExample 4: Attempting to create isosceles triangle with invalid dimensions")
    try:
        it = IsoscelesTriangle(3, 10)
    except ValueError as e:
        print(f"Error caught: {e}")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 60)
    print("TRIANGLE GEOMETRY PACKAGE - COMPREHENSIVE EXAMPLES")
    print("=" * 60)
    
    demonstrate_right_triangle()
    demonstrate_scalene_triangle()
    demonstrate_isosceles_triangle()
    demonstrate_error_handling()
    
    print("\n" + "=" * 60)
    print("ALL EXAMPLES COMPLETED SUCCESSFULLY!")
    print("=" * 60)


if __name__ == "__main__":
    main()
