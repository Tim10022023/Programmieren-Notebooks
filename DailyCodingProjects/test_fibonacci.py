import pytest

from fibonacci import fibonacci_of

def test_fibonacci_of_zero():
    assert fibonacci_of(0) == 0

def test_fibonacci_of_one():
    assert fibonacci_of(1) == 1

def test_fibonacci_of_two():
    assert fibonacci_of(2) == 1

def test_fibonacci_of_three():
    assert fibonacci_of(3) == 2

def test_fibonacci_of_ten():
    assert fibonacci_of(10) == 55
