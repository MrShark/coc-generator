"""
Simple dice rolling utilities
"""

from random import randint


def roll(dice: str) -> int:
    """
    roll some dice

    Arguments:
        dice {str} -- What to roll on the format "3D6+3

    Returns:
        str -- a random roll
    """
    if "+" in dice:
        dice, addition = dice.split("+")
        addition = int(addition)
    else:
        addition = 0

    count, sides = [int(v) for v in dice.split("D")]

    val = 0
    for _ in range(count):
        val += randint(1, sides)
    return val + addition
