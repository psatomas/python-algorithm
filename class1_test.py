import pytest
from class1 import Person

def test_person_creation():
    p = Person("Alice", 30)
    assert p.name == "Alice"
    assert p.age == 30

def test_get_info():
    p = Person("Bob", 25)
    assert p.get_info() == ("Bob", 25)