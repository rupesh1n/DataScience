# Triangle Geometry Package - Quick Start Guide

## Installation

1. **Navigate to the package directory**
   ```bash
   cd triangle-geometry
   ```

2. **Install the package**
   ```bash
   pip install -e .
   ```
   
   Or for a regular installation:
   ```bash
   pip install .
   ```

## Quick Test

Run the example file to see all features in action:
```bash
python example_usage.py
```

## Basic Usage

### Example 1: Right-Angled Triangle
```python
from triangle_geometry import RightTriangle

# Create a 3-4-5 right triangle
triangle = RightTriangle(3, 4)

print(f"Base: {triangle.base}")              # 3
print(f"Height: {triangle.height}")          # 4
print(f"Hypotenuse: {triangle.hypotenuse}")  # 5.0
print(f"Area: {triangle.area()}")            # 6.0
print(f"Perimeter: {triangle.perimeter()}")  # 12.0
```

### Example 2: Scalene Triangle
```python
from triangle_geometry import ScaleneTriangle

# Create a scalene triangle with sides 7, 8, 9
triangle = ScaleneTriangle(7, 8, 9)

print(f"Side A: {triangle.side_a}")          # 7
print(f"Side B: {triangle.side_b}")          # 8
print(f"Side C: {triangle.side_c}")          # 9
print(f"Area: {triangle.area():.2f}")        # 26.83
print(f"Perimeter: {triangle.perimeter()}")  # 24
```

### Example 3: Isosceles Triangle
```python
from triangle_geometry import IsoscelesTriangle

# Create an isosceles triangle with equal_side=5, base=6
triangle = IsoscelesTriangle(5, 6)

print(f"Equal Side: {triangle.equal_side}")  # 5
print(f"Base: {triangle.base}")              # 6
print(f"Height: {triangle.height}")          # 4.0
print(f"Area: {triangle.area()}")            # 12.0
print(f"Perimeter: {triangle.perimeter()}")  # 16
```

## Error Handling

The package validates all inputs:

```python
from triangle_geometry import RightTriangle, ScaleneTriangle

# This will raise ValueError: "Base and height must be positive numbers"
try:
    triangle = RightTriangle(-3, 4)
except ValueError as e:
    print(f"Error: {e}")

# This will raise ValueError: "The given sides do not form a valid triangle"
try:
    triangle = ScaleneTriangle(1, 2, 10)
except ValueError as e:
    print(f"Error: {e}")
```

## Running Tests

To run the unit tests:
```bash
# Install pytest first if needed
pip install pytest

# Run tests
pytest test_triangles.py -v
```

## Package Structure

```
triangle_geometry/
├── __init__.py              # Package initialization
├── right_triangle.py        # Right-angled triangle
├── scalene_triangle.py      # Scalene triangle
└── isosceles_triangle.py    # Isosceles triangle
```

## Key Features

✅ **Comprehensive PyDoc documentation** - Every class and method fully documented  
✅ **Input validation** - Automatic validation of triangle constraints  
✅ **Automatic calculations** - Hypotenuse and height calculated automatically  
✅ **Error handling** - Clear, descriptive error messages  
✅ **No external dependencies** - Uses only Python standard library  
✅ **Well tested** - 40+ unit tests covering all functionality  
✅ **Pythonic design** - Follows Python best practices and conventions  

## Documentation

For complete documentation, see:
- **README.md** - Full package documentation
- **PROJECT_STRUCTURE.md** - Detailed project structure explanation
- **example_usage.py** - Comprehensive examples
- **test_triangles.py** - Test cases showing all features

## Support

For issues or questions:
1. Check the README.md for detailed documentation
2. Review example_usage.py for usage patterns
3. Look at test_triangles.py for test examples
4. Submit issues on GitHub (when published)

---

**Created by a Python Expert with 10+ years of experience**
