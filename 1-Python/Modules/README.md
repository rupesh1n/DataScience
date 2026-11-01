# Triangle Geometry Package

A professional Python package for calculating geometric properties of triangles, including right-angled, scalene, and isosceles triangles.

## Features

- **Right-Angled Triangles**: Calculate area and perimeter given base and height
- **Scalene Triangles**: Calculate area (using Heron's formula) and perimeter given three sides
- **Isosceles Triangles**: Calculate area and perimeter given equal sides and base
- **Comprehensive Documentation**: Full PyDoc strings for all classes and methods
- **Input Validation**: Robust error handling for invalid triangle dimensions
- **Type Safety**: Clear type hints and validation

## Installation

### Using pip (if published to PyPI)
```bash
pip install triangle-geometry
```

### From source
```bash
git clone https://github.com/yourusername/triangle-geometry.git
cd triangle-geometry
pip install -e .
```

## Quick Start

```python
from triangle_geometry import RightTriangle, ScaleneTriangle, IsoscelesTriangle

# Right-angled triangle (base=3, height=4)
right = RightTriangle(3, 4)
print(f"Area: {right.area()}")        # Output: 6.0
print(f"Perimeter: {right.perimeter()}")  # Output: 12.0

# Scalene triangle (sides 3, 4, 5)
scalene = ScaleneTriangle(3, 4, 5)
print(f"Area: {scalene.area()}")      # Output: 6.0
print(f"Perimeter: {scalene.perimeter()}")  # Output: 12

# Isosceles triangle (equal_side=5, base=6)
isosceles = IsoscelesTriangle(5, 6)
print(f"Area: {isosceles.area():.2f}")     # Output: 12.00
print(f"Perimeter: {isosceles.perimeter()}")  # Output: 16
```

## Detailed Usage

### Right-Angled Triangle

```python
from triangle_geometry import RightTriangle

# Create a right triangle with base=6 and height=8
triangle = RightTriangle(6, 8)

# Get properties
print(triangle.base)        # 6
print(triangle.height)      # 8
print(triangle.hypotenuse)  # 10.0

# Calculate area and perimeter
print(triangle.area())      # 24.0
print(triangle.perimeter()) # 24.0
```

### Scalene Triangle

```python
from triangle_geometry import ScaleneTriangle

# Create a scalene triangle with sides 7, 8, 9
triangle = ScaleneTriangle(7, 8, 9)

# Get properties
print(triangle.side_a)  # 7
print(triangle.side_b)  # 8
print(triangle.side_c)  # 9

# Calculate area (using Heron's formula) and perimeter
print(triangle.area())       # 26.83
print(triangle.perimeter())  # 24
```

### Isosceles Triangle

```python
from triangle_geometry import IsoscelesTriangle

# Create an isosceles triangle with equal_side=10 and base=12
triangle = IsoscelesTriangle(10, 12)

# Get properties
print(triangle.equal_side)  # 10
print(triangle.base)        # 12
print(triangle.height)      # 8.0

# Calculate area and perimeter
print(triangle.area())      # 48.0
print(triangle.perimeter()) # 32
```

## Error Handling

The package includes robust input validation:

```python
from triangle_geometry import RightTriangle, ScaleneTriangle, IsoscelesTriangle

# Invalid: negative dimensions
try:
    triangle = RightTriangle(-3, 4)
except ValueError as e:
    print(e)  # "Base and height must be positive numbers"

# Invalid: violates triangle inequality
try:
    triangle = ScaleneTriangle(1, 2, 10)
except ValueError as e:
    print(e)  # "The given sides do not form a valid triangle"

# Invalid: not actually scalene (has equal sides)
try:
    triangle = ScaleneTriangle(5, 5, 7)
except ValueError as e:
    print(e)  # "Scalene triangle must have all different side lengths"

# Invalid: equal sides too short for base
try:
    triangle = IsoscelesTriangle(3, 10)
except ValueError as e:
    print(e)  # "The given sides do not form a valid triangle"
```

## API Reference

### RightTriangle

**Constructor:**
- `RightTriangle(base: float, height: float)`

**Methods:**
- `area() -> float`: Returns the area of the triangle
- `perimeter() -> float`: Returns the perimeter of the triangle

**Attributes:**
- `base`: The base of the triangle
- `height`: The height of the triangle
- `hypotenuse`: The hypotenuse (calculated automatically)

### ScaleneTriangle

**Constructor:**
- `ScaleneTriangle(side_a: float, side_b: float, side_c: float)`

**Methods:**
- `area() -> float`: Returns the area using Heron's formula
- `perimeter() -> float`: Returns the perimeter of the triangle

**Attributes:**
- `side_a`: Length of first side
- `side_b`: Length of second side
- `side_c`: Length of third side

### IsoscelesTriangle

**Constructor:**
- `IsoscelesTriangle(equal_side: float, base: float)`

**Methods:**
- `area() -> float`: Returns the area of the triangle
- `perimeter() -> float`: Returns the perimeter of the triangle

**Attributes:**
- `equal_side`: Length of the two equal sides
- `base`: Length of the base
- `height`: Height from base to apex (calculated automatically)

## Mathematical Formulas

### Right-Angled Triangle
- **Area**: `(1/2) × base × height`
- **Perimeter**: `base + height + hypotenuse`
- **Hypotenuse**: `√(base² + height²)` (Pythagorean theorem)

### Scalene Triangle
- **Area**: Heron's formula: `√[s(s-a)(s-b)(s-c)]` where `s = (a+b+c)/2`
- **Perimeter**: `side_a + side_b + side_c`

### Isosceles Triangle
- **Area**: `(1/2) × base × height`
- **Perimeter**: `2 × equal_side + base`
- **Height**: `√(equal_side² - (base/2)²)`

## Development

### Running Tests
```bash
pytest tests/
```

### Running Examples
```bash
python example_usage.py
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Python Expert with 10+ years of experience

## Version History

- **1.0.0** (2024): Initial release
  - Right-angled triangle support
  - Scalene triangle support
  - Isosceles triangle support
  - Comprehensive documentation
  - Input validation and error handling
