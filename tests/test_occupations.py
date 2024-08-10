"""Test for occupations."""

# ruff: noqa: S101, PLR2004
from __future__ import annotations

import pytest
from coc_gen.base_classes import Occupation


@pytest.mark.parametrize(
    ("formula", "baseval", "expected"),
    [
        ("UTB×2+KAR×2", {"UTB": 10, "KAR": 30}, 80),
        ("UTB×2", {"UTB": 10, "KAR": 30}, 20),
        ("UTB×1+KAR×3", {"UTB": 10, "KAR": 30}, 100),
        ("UTB×2+KAR×2+SMI×2", {"SMI": 20, "UTB": 10, "KAR": 30}, 120),
        ("UTB×2", {"UTB": 100, "KAR": 30}, 200),
    ],
)
def test_skillpoints(formula: str, baseval: dict[str, int], expected: int) -> None:
    """Test generation of skill points."""
    assert Occupation("test", formula, (1, 2), []).calc_skillpoint(baseval) == expected
