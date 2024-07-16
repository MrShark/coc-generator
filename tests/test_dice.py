"""Tests for the coc_gen.dice module"""

from random import randint

import pytest

from coc_gen.utils.dice import roll


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("1D1", 1),
        ("1D1+1", 2),
        ("4D1", 4),
        ("4D1+1", 5),
    ],
)
def test_one_sided_dice(test_input, expected):
    """Test that one sided dice work (they are non random)"""
    assert roll(test_input) == expected


NUM_ROLLS = 1000


def test_rolls():
    """Check that basic roles are within range"""
    for _ in range(NUM_ROLLS):
        count = randint(1, 5)
        sides = randint(3, 20)

        val = roll(f"{count}D{sides}")
        assert val >= count
        assert val <= count * sides
