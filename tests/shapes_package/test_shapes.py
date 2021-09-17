from unittest import TestCase
from shapes_library.shapes_package.shapes_module import Circle
from shapes_library.shapes_package.shapes_module import Rectangle


class CircleTests(TestCase):
    """
    Contains all unit tests for the shapes_module.Circle class
    """

    def test_circle_area_returns_correct_result_with_valid_radius(self):
        """
        Tests that a Circle object with a radius > 0 returns the correct area
        """
        mock_radius = 5.0
        expected_area = 78.54
        mock_circle = Circle(radius=mock_radius)
        self.assertEqual(mock_circle.area(), expected_area)

    def test_circle_area_ValueError_with_negative_radius(self):
        """
        Tests that a Circle object with a negative radius raises a valueError
         """
        with self.assertRaises(ValueError):
            mock_circle = Circle(radius=-1.0)

    def test_instance_of_a_circle(self):
        """
         Test if  the Circle object has a float instance value.
        """
        mock_radius = 5.0
        mock_circle = Circle(radius=mock_radius)
        self.assertIsInstance(mock_circle.area(), float)

    def test_the_circle_area_is_not_none(self):
        """
        Tests if the circle object is not none.
        """
        mock_radius = 5.0
        mock_circle = Circle(radius=mock_radius)
        self.assertIsNotNone(mock_circle.area())


class RectangleTests(TestCase):
    """
    Contains all the unit tests for the shapes_module.Rectangle class
    """

    def test_rectangle_area_returns_correct_result_with_valid_height_and_width(self):
        """
        Tests that a Rectangle object with a height > 0 and a width > 0 returns the correct area
        """
        mock_height, mock_width = 10., 10.
        expected_area = 100.
        mock_rectangle = Rectangle(height=mock_height, width=mock_width)
        self.assertEqual(mock_rectangle.area(), expected_area)

    def test_rectangle_area_ValueError_with_negative_height_and_width(self):
        """
        Tests that a rectangle object with a negative height and width raises a valueError
         """
        with self.assertRaises(ValueError):
            mock_rectangle = Rectangle(height=-1.0, width=-1.0)

    def test_instance_of_a_rectangle_height_and_width(self):
        """
         Test if  the rectangle object has a float instance value.
        """
        mock_height, mock_width = 10., 10.
        mock_rectangle=Rectangle(height=mock_height, width=mock_width)
        self.assertIsInstance(mock_rectangle.area(), float)

    def test_the_rectangle_area_is_not_none(self):
        """
        Tests if the rectangle object is not none.
        """
        mock_height, mock_width = 10., 10.
        mock_rectangle=Rectangle(height=mock_height, width=mock_width)
        self.assertIsNotNone(mock_rectangle.area())