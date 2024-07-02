"""Test of investigators"""

from coc_gen import investigator


def test_coc_char():
    """Very basic tests of investigator creation"""
    char = investigator.Investigator()

    assert isinstance(char.name, str)
    assert 15 <= char.STY <= 90
    assert 15 <= char.FYS <= 90
    assert 15 <= char.STO <= 90
    assert 15 <= char.SMI <= 90
    assert 15 <= char.KAR <= 90
    assert 15 <= char.INT <= 90
    assert 15 <= char.VST <= 90
    assert 15 <= char.UTB <= 90
