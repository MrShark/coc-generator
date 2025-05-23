"""Test of investigators."""

# ruff: noqa: S101, PLR2004
from __future__ import annotations

import pytest

from coc_gen import get_investgator_class


def test_coc_char() -> None:
    """Very basic tests of investigator creation."""
    char = get_investgator_class("coc_swe")()

    assert isinstance(char.name, str)
    assert 15 <= char.STY <= 90
    assert 15 <= char.FYS <= 90
    assert 15 <= char.STO <= 90
    assert 15 <= char.SMI <= 90
    assert 15 <= char.KAR <= 90
    assert 15 <= char.INT <= 90
    assert 15 <= char.VST <= 90
    assert 15 <= char.UTB <= 90


@pytest.mark.parametrize(
    ("ruleset", "base_values", "build", "damage_bonus"),
    [
        ("coc_swe", {"STY": 65, "STO": 60}, 1, "1D4"),
        ("coc_swe", {"STY": 60, "STO": 65}, 1, "1D4"),
        ("coc_swe", {"STY": 60, "STO": 60}, 0, "0"),
        ("coc_swe", {"STY": 15, "STO": 40}, -2, "-2"),
        ("coc_20", {"STR": 65, "SIZ": 60}, 1, "1D4"),
        ("coc_modern", {"STR": 65, "SIZ": 60}, 1, "1D4"),
    ],
)
def test_combat_values(ruleset: str, base_values: dict[str, int], build: int, damage_bonus: str) -> None:
    """Tests of combat values."""
    investigator = get_investgator_class(ruleset)(basevalues=base_values)

    assert investigator.build == build
    assert investigator.damage_bonus == damage_bonus


@pytest.mark.parametrize(
    "char_dict",
    [
        {
            "sex": "M",
            "name": "Jacob Tyler",
            "basevalues": {
                "FYS": 65,
                "INT": 60,
                "KAR": 50,
                "SMI": 65,
                "STO": 80,
                "STY": 90,
                "UTB": 65,
                "VST": 35,
            },
            "occupation": "Antikhandlare",
            "skills": {
                "Levnadsstandard": 41,
                "Bokföring": 81,
                "Bluffa": 53,
                "Historia": 68,
                "Språk (Annat)": 10,
                "Värdering": 27,
                "Charma": 16,
                "Bibliotekskunskap": 20,
            },
        },
        {
            "sex": "F",
            "name": "Megan Clark",
            "basevalues": {
                "FYS": 60,
                "INT": 45,
                "KAR": 40,
                "SMI": 45,
                "STO": 55,
                "STY": 55,
                "UTB": 80,
                "VST": 20,
            },
            "occupation": "Ligist",
            "skills": {
                "Levnadsstandard": 3,
                "Klättra": 67,
                "Kasta": 74,
                "Hoppa": 35,
                "Hota": 32,
                "Lyssna": 29,
                "Smyga": 54,
                "Strid (Handgemäng)": 45,
                "Fingerfärdighet": 81,
            },
        },
        {
            "sex": "M",
            "name": "George Hoffman",
            "basevalues": {
                "FYS": 45,
                "INT": 80,
                "KAR": 65,
                "SMI": 35,
                "STO": 70,
                "STY": 40,
                "UTB": 65,
                "VST": 40,
            },
            "occupation": "Estradör",
            "skills": {
                "Levnadsstandard": 49,
                "Konst & hantverk (Skådespelare)": 49,
                "Charma": 54,
                "Fingerfärdighet": 49,
                "Övertyga": 58,
                "Bokföring": 12,
                "Språk (Annat)": 21,
                "Bluffa": 19,
            },
        },
        {
            "sex": "F",
            "name": "Leah Martin",
            "basevalues": {
                "FYS": 40,
                "INT": 80,
                "KAR": 55,
                "SMI": 50,
                "STO": 50,
                "STY": 60,
                "UTB": 80,
                "VST": 60,
            },
            "occupation": "Betjänt-Hembiträde",
            "skills": {
                "Levnadsstandard": 33,
                "Psykologi": 42,
                "Konst & hantverk (Sömnad)": 13,
                "Finna dolda ting": 64,
                "Språk (Annat)": 51,
                "Konst & hantverk (Matlagning)": 37,
                "Värdering": 26,
                "Konst & hantverk (Barberare)": 14,
                "Bokföring": 21,
                "Konst & hantverk (Målare)": 21,
                "Första hjälpen": 37,
                "Läkekonst": 8,
            },
        },
        {
            "sex": "F",
            "name": "Erin Price",
            "basevalues": {
                "FYS": 55,
                "INT": 45,
                "KAR": 55,
                "SMI": 65,
                "STO": 65,
                "STY": 55,
                "UTB": 40,
                "VST": 55,
            },
            "occupation": "Bartender-Krögare",
            "skills": {
                "Levnadsstandard": 29,
                "Överlevnad (Berg)": 83,
                "Strid (Handgemäng)": 63,
                "Konst & hantverk (Matlagning)": 54,
                "Lyssna": 21,
                "Finna dolda ting": 25,
                "Bokföring": 5,
                "Psykologi": 10,
                "Charma": 15,
            },
        },
        {
            "sex": "F",
            "name": "Melissa Martin",
            "basevalues": {
                "FYS": 75,
                "INT": 85,
                "KAR": 55,
                "SMI": 55,
                "STO": 55,
                "STY": 45,
                "UTB": 65,
                "VST": 20,
            },
            "occupation": "Student",
            "skills": {
                "Levnadsstandard": 18,
                "Övertyga": 50,
                "Konst & hantverk (Författare)": 77,
                "Bibliotekskunskap": 48,
                "Lyssna": 58,
                "Vetenskap (Kemi)": 63,
                "Språk (Annat)": 3,
                "Språk (Annat 2)": 1,
            },
        },
        {
            "sex": "M",
            "name": "Dustin Compton",
            "basevalues": {
                "FYS": 50,
                "INT": 80,
                "KAR": 65,
                "SMI": 50,
                "STO": 75,
                "STY": 45,
                "UTB": 70,
                "VST": 55,
            },
            "occupation": "Brandsoldat",
            "skills": {
                "Levnadsstandard": 17,
                "Första hjälpen": 72,
                "Chaufför (Bil)": 37,
                "Hoppa": 81,
                "Kasta": 81,
                "Strid (Yxa)": 51,
                "Simma": 21,
                "Skjutvapen (Kulspruta)": 13,
                "Klättra": 22,
            },
        },
        {
            "sex": "F",
            "name": "Tiffany Blair",
            "basevalues": {
                "FYS": 50,
                "INT": 65,
                "KAR": 40,
                "SMI": 50,
                "STO": 60,
                "STY": 35,
                "UTB": 65,
                "VST": 70,
            },
            "occupation": "Redaktör-Förläggare",
            "skills": {
                "Levnadsstandard": 47,
                "Konst & hantverk (Författare)": 34,
                "Bokföring": 75,
                "Överlevnad (Hav)": 59,
                "Psykologi": 57,
                "Språk (Annat)": 13,
                "Historia": 6,
                "Bibliotekskunskap": 24,
                "Övertyga": 11,
            },
        },
        {
            "sex": "M",
            "name": "John Eaton",
            "basevalues": {
                "FYS": 50,
                "INT": 75,
                "KAR": 70,
                "SMI": 85,
                "STO": 55,
                "STY": 60,
                "UTB": 75,
                "VST": 30,
            },
            "occupation": "Journalist",
            "skills": {
                "Levnadsstandard": 24,
                "Arkeologi": 41,
                "Konst & hantverk (Författare)": 20,
                "Historia": 42,
                "Psykologi": 52,
                "Bibliotekskunskap": 69,
                "Språk (Annat)": 36,
                "Språk (Eget)": 92,
                "Övertyga": 51,
            },
        },
        {
            "sex": "M",
            "name": "James Williams",
            "basevalues": {
                "FYS": 75,
                "INT": 60,
                "KAR": 60,
                "SMI": 50,
                "STO": 75,
                "STY": 55,
                "UTB": 65,
                "VST": 25,
            },
            "occupation": "Läkare",
            "skills": {
                "Levnadsstandard": 36,
                "Läkekonst": 45,
                "Historia": 60,
                "Konst & hantverk (Dressyr)": 39,
                "Språk (Annat)": 26,
                "Bibliotekskunskap": 36,
                "Vetenskap (Läkemedel)": 16,
                "Första hjälpen": 51,
                "Vetenskap (Biologi)": 15,
            },
        },
        {
            "sex": "M",
            "name": "Jose Wallace",
            "basevalues": {
                "FYS": 45,
                "INT": 65,
                "KAR": 70,
                "SMI": 70,
                "STO": 55,
                "STY": 65,
                "UTB": 40,
                "VST": 55,
            },
            "occupation": "Sjuksköterska",
            "skills": {
                "Levnadsstandard": 28,
                "Psykologi": 71,
                "Första hjälpen": 32,
                "Språk (Eget)": 70,
                "Läkekonst": 60,
                "Vetenskap (Läkemedel)": 1,
                "Strid (Handgemäng)": 27,
                "Språk (Annat)": 3,
                "Bibliotekskunskap": 21,
            },
        },
        {
            "sex": "M",
            "name": "Timothy Vaughan",
            "basevalues": {
                "FYS": 45,
                "INT": 55,
                "KAR": 45,
                "SMI": 60,
                "STO": 55,
                "STY": 25,
                "UTB": 75,
                "VST": 40,
            },
            "occupation": "Konstnär",
            "skills": {
                "Levnadsstandard": 24,
                "Psykologi": 75,
                "Historia": 45,
                "Konst & hantverk (Fotografi)": 14,
                "Språk (Annat)": 91,
                "Hota": 17,
                "Konst & hantverk (Skogshuggare)": 6,
                "Finna dolda ting": 33,
                "Naturkunskap": 11,
            },
        },
    ],
)
def test_char_from_to_dict(char_dict: dict) -> None:
    """Verify that as_dict() reverses from_dict()."""
    CharClass = get_investgator_class("coc_swe")  # noqa: N806
    new_dict = CharClass.from_dict(char_dict).as_dict
    assert new_dict == char_dict
