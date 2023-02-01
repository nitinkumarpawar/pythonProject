import pytest

from demo.demo_project.sample_2 import validate_age


def test_validate_age_valid_age():
    validate_age(18)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be negative"):
        validate_age(-1)