"""
Occupations
"""

from .base_classes import Investigator
from .coc_eng import ModernInvestigator, TwentiesInvestigator
from .coc_swe import SweInvestigator

RULESETS = ("coc_swe", "coc_20", "coc_modern")


def get_investgator_class(ruleset: str) -> Investigator:
    """
    Get an investgator class that implements the given ruleset

    Arguments:
        ruleset {str} -- The ruleset you want to follow. All can be found in RULESETS.

    Raises:
        NotImplementedError: The ruleset

    Returns:
        Investigator -- A subclass of Investigator
    """
    if ruleset == "coc_swe":
        return SweInvestigator
    if ruleset == "coc_20":
        return TwentiesInvestigator
    if ruleset == "coc_modern":
        return ModernInvestigator

    raise NotImplementedError
