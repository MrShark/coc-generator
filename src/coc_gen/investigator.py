"""
Classes that represents an Investigator
"""

from random import choice, randint
from typing import Any

import click
from faker import Faker

from . import dice
from .data import occupations, skills


class Investigator:
    """
    An Investigator.

    See __init__() for creation options
    """

    _basevalues = {
        "STY": ("3D6"),
        "FYS": ("3D6"),
        "STO": ("2D6+6"),
        "SMI": ("3D6"),
        "KAR": ("3D6"),
        "INT": ("2D6+6"),
        "VST": ("3D6"),
        "UTB": ("2D6+6"),
    }

    def __init__(
        self, locale=None, sex=None, name=None, basevalues=None, occupation=None
    ) -> None:
        """
        Create an Investigator

        Keyword Arguments:
            locale {str} -- The locale the Investigator is active in.
                Sent to Faker that is used to create their name.
                More info: https://faker.readthedocs.io/en/stable/#localization  (default: {None})
            sex {"M"/"F"} -- Sex of the Investigator, if None random (default: {None})
            name {str} -- Name of the Investigator, if None random according to the locale (default: {None})
            basevalues {dict[str,int]} -- Basevalues of the Investigator, if None random (default: {None})
            occupation {str} -- Occupation of the Investigator, if None random (default: {None})
        """
        self.fake = Faker(locale=locale)

        if sex in ("F", "M"):
            self.sex = sex
        else:
            self.sex = choice(("F", "M"))

        if name:
            self.name = name
        else:
            if self.sex == "F":
                self.name = self.fake.name_female()
            else:
                self.name = self.fake.name_male()

        if basevalues is None:
            basevalues = {}
        self.basevalues = {}
        for val, roll in self._basevalues.items():
            self.basevalues[val] = basevalues.get(val, dice.roll(roll)) * 5

        if occupation:
            self.occupation = occupations.occupations[occupation]
        else:
            self.occupation = choice(list(occupations.occupations.values()))

        skill_points = self.occupation.calc_skillpoint(self.basevalues)
        credit = randint(*self.occupation.credit_range)
        self.skills = {"Levnadsstandard": credit}
        skill_points -= credit

        for skill in self.occupation.get_skill_instance():
            curr_value = skills.get_defult_value(skill, self.basevalues)
            addition = randint(0, min(90 - curr_value, skill_points))
            skill_points -= addition
            self.skills[skill] = curr_value + addition

        while skill_points:
            skill = choice(list(self.skills.keys()))
            self.skills[skill] += 1
            skill_points -= 1

    def __getattr__(self, name: str) -> Any:
        if name in self.basevalues:
            return self.basevalues[name]
        raise AttributeError()

    def __repr__(self) -> str:
        return f"""Investigator(
    name = '{self.name}',
    sex = '{self.sex}',
    basevalues = {self.basevalues},
    occupation = '{self.occupation.name}',
    skills = '{self.skills}',
)"""


@click.command()
@click.option("--locale", default=None, help="Where do the Investigator come from")
@click.option("--number", default=1, help="Number of investigators to generate.")
@click.option("--sex", default=None, help="The sex of the investigator.")
@click.option("--occupation", default=None, help="The occupation of the investigator.")
def cli(locale, number, sex, occupation):
    """Generate Call of Cthulhu investigators."""
    for _ in range(number):
        print(Investigator(locale=locale, sex=sex, occupation=occupation))
