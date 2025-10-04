# conftest.py
import pytest

@pytest.fixture
def sample_items():
    return [
        {"price": 10.0, "qty": 2},  # para probar errores, colocar -10.0 y -2
        {"price": 5.5, "qty": 1},
    ]

@pytest.fixture
def storage():
    return []
