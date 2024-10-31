import pytest
from calculator import divide


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        divide(10, 0)


def test_divide():
    assert divide(10, 2) == 5