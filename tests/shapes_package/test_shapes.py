import math
import pytest
from numpy import isclose
from shapes_library.shapes_package.shapes_module import Circle
from shapes_library.shapes_package.shapes_module import Rectangle


def test_circle_area_returns_correct_result_with_valid_radius(mock_radius):
    """
    Tests that a Circle object with a radius > 0 returns the correct area
    """
    expected_area = math.pi * mock_radius ** 2
    mock_circle = Circle(radius=mock_radius)
    assert isclose(mock_circle.area(), expected_area)

def test_rectangle_area_returns_correct_result_with_valid_height_and_width():
    """
    Tests that a Rectangle object with a height > 0 and a width > 0 returns the correct area
    """
    assert False
