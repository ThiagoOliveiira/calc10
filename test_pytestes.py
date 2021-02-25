import pytest
from app import soma


@pytest.mark.parametrize('a,b,expected', [(5, 4, 9)], [-2, -4, 6])
def test_soma(a,b, expected):
    assert soma(a,b) == expected
