"""
Triangle Geometry Package

A comprehensive package for calculating properties of different types of triangles.
Supports right-angled, scalene, and isosceles triangles.

Author: Python Expert
Version: 1.0.0
"""

from .right_triangle import RightTriangle
from .scalene_triangle import ScaleneTriangle
from .isosceles_triangle import IsoscelesTriangle

__all__ = ['RightTriangle', 'ScaleneTriangle', 'IsoscelesTriangle']
__version__ = '1.0.0'
