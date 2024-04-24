import pytest
from src.test_sample import TestSample

def test_abs_sum():
    result = TestSample.abs_sum(1,2)
    assert result == 3
    result = TestSample.abs_sum(1,-2)
    assert result == 3
    result = TestSample.abs_sum(-1,2)
    assert result == 3
    result = TestSample.abs_sum(-1,-2)
    assert result == 3