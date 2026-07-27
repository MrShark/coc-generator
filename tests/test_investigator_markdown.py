"""Tests for Investigator.as_markdown()."""

from __future__ import annotations

from coc_gen import get_investgator_class


def test_as_markdown_contains_sections_and_tables() -> None:
    """Test that markdown output contains the expected sections and tables for base values and skills."""
    concrete_class = get_investgator_class("coc_swe")

    char_dict = {
        "sex": "M",
        "name": "Test Person",
        "basevalues": {
            "FYS": 50,
            "INT": 60,
            "KAR": 55,
            "SMI": 45,
            "STO": 50,
            "STY": 65,
            "UTB": 40,
            "VST": 30,
        },
        "occupation": "Journalist",
        "skills": {
            "Charma": 12,
            "Arkeologi": 3,
            "Bibliotekskunskap": 20,
        },
    }

    inv = concrete_class.from_dict(char_dict)
    md = inv.as_markdown()

    # Basic sections
    assert f"# {char_dict['name']}" in md
    assert f"- **Occupation:** {char_dict['occupation']}" in md
    assert "## Base Values" in md
    assert "## Skills" in md

    # Base values table contains each base value row
    for k, v in char_dict["basevalues"].items():
        assert f"| {k} | {v} |" in md

    # Skills table contains skill rows and are in alphabetical order
    skills_sorted = sorted(char_dict["skills"].keys(), key=lambda x: x.lower())
    positions = [md.find(f"| {s} |") for s in skills_sorted]
    assert all(p >= 0 for p in positions)
    # ensure increasing order in the markdown output
    assert positions == sorted(positions)
