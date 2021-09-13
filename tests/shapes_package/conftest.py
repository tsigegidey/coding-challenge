import pytest


@pytest.fixture
def mock_radius():
    """
    Reusable input for Circle.area tests
    """
    return 5.


@pytest.fixture
def mock_height():
    """
    Reusable input for Rectangle.area tests
    """
    return 10.


@pytest.fixture
def mock_width():
    """
    Reusable input for Rectangle.area tests
    """
    return 10.
