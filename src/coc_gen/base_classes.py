"""Base classes that can be specialised to implement different rulesets"""

from functools import total_ordering
from random import choice, randint, random
from typing import Any

from faker import Faker

from .utils import dice


class Skill:
    """
    A CoC skill, with name and a default value
    """

    def __init__(self, name: str, default_value: str) -> None:
        self.name = name
        self.default_value = default_value

    def get_value(self, value: int) -> "SkillValue":
        """
        Get a specific skill value

        Arguments:
            value {int} -- the specific value to get

        Returns:
            SkillValue -- The skill value
        """
        return SkillValue(self, value)

    def instance_value(self, base_values: dict[str, int]) -> "SkillValue":
        """
        Instanciate a default value for the skill.

        Arguments:
            base_values {dict[str, int]} -- Base values to use for the calculation of the default value

        Returns:
            SkillValue -- the skill value
        """
        if self.default_value.endswith("%"):
            return SkillValue(self, int(self.default_value[:-1]))

        if "/" in self.default_value:
            b, f = self.default_value.split("/")
            return SkillValue(self, int(base_values[b] / int(f)))

        return SkillValue(self, base_values[self.default_value])


@total_ordering
class SkillValue:
    """
    A specific value of a skill.
    The skill can be accessed via skill and the value via value
    It is ordered via the value
    It supports addidtion and subtraction with other SkillValue:s and integers.
    """

    def __init__(self, skill: Skill, value: int) -> None:
        self.skill = skill
        self.value = value

    @property
    def half_value(self) -> int:
        """
        the half value

        Returns:
            int -- the half value
        """
        return int(self.value / 2)

    @property
    def fifth_value(self) -> int:
        """
        the fifth value

        Returns:
            int -- the fifth value
        """
        return int(self.value / 5)

    def __add__(self, other):
        if hasattr(other, "value"):
            return self.__class__(self.skill, self.value + other.value)
        elif isinstance(other, (int, float)):
            return self.__class__(self.skill, self.value + int(other))
        else:
            raise TypeError("Unsupported operand type(s) for +")

    def __sub__(self, other):
        if hasattr(other, "value"):
            return self.__class__(self.skill, self.value - other.value)
        elif isinstance(other, (int, float)):
            return self.__class__(self.skill, self.value - int(other))
        else:
            raise TypeError("Unsupported operand type(s) for -")

    def __eq__(self, other):
        if not hasattr(other, "value"):
            return NotImplemented
        return self.value == other.value

    def __lt__(self, other):
        if not hasattr(other, "value"):
            return NotImplemented
        return self.value < other.value

    def __repr__(self) -> str:
        return f"{self.value}"


class Occupation:
    """
    An Occupation
    """

    _special_skills = {}
    _skills = {}
    _basevalues = {}

    def __init__(
        self,
        name: str,
        skill_points: str,
        credit_range: tuple[int, int],
        occupation_skills: list[str],
    ) -> None:
        """
        Create an Occupation

        Arguments:
            name {str} -- Name of the occupation
            skill_points {str} -- The number of skill points the Occupation gets
                (for syntax see calc_skillpoints())
            credit_range {tuple[int,int]} -- Min and max credit range for the occupation
            occupation_skills {list(str)} -- list of possible skill
        """

        self.name = name
        self.skill_points = skill_points
        self.credit_range = credit_range
        self.occupation_skills = occupation_skills

    def calc_skillpoint(self, basevalues: dict[str, int]) -> int:
        """
        Calculate the skillpoint for this occupation with the given
        base values.

        The syntax of the occupations skill point settings are something like:
            "UTB×2+STY×2" or "UTB×4" ie. multiplication of a base values with
            integers and then optional addition addition

        Arguments:
            basevalues {dict[str,int]} -- the base values of the character that
                have the occupation.

        Returns:
            int -- the calculated skill points
        """
        skill_points = []
        for alt in self.skill_points.split("|"):
            sp = 0
            for term in alt.split("+"):
                bv, factor = term.split("×")
                sp += basevalues[bv] * int(factor)
            skill_points.append(sp)

        return max(skill_points)

    def get_skill_instance(self) -> list[Skill]:
        """
        Get a instance of skills for the occupation

        Any skills that are a key to the special_skills dictionary
        are replaced with a random skill from the keys item.
        The returned skills are in a random order.

        Returns:
            list[str] -- _description_
        """
        inst = set()
        for skill in self.occupation_skills:
            if skill in self._special_skills:
                inst.add(self._skills[choice(self._special_skills[skill])])
            else:
                inst.add(self._skills[skill])

        return sorted(inst, key=lambda x: random())

    def __repr__(self) -> str:
        return f"Occupation('{self.name}')"


class Investigator:
    """
    An Investigator.

    See __init__() for creation options
    """

    _occupations: list[Occupation] = {}
    _credit_rating = "Credit Rating"
    _basevalues = {}

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
            self.occupation = self._occupations[occupation]
        else:
            self.occupation = choice(list(self._occupations.values()))

        skill_points = self.occupation.calc_skillpoint(self.basevalues)
        credit_val = randint(*self.occupation.credit_range)
        credit = self.occupation._skills[self._credit_rating].get_value(credit_val)
        self.skills = {self._credit_rating: credit}
        skill_points -= credit_val

        for skill in self.occupation.get_skill_instance():
            curr_value = skill.instance_value(self.basevalues)
            addition = randint(0, min(90 - curr_value.value, skill_points))
            skill_points -= addition
            self.skills[skill.name] = curr_value + addition

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