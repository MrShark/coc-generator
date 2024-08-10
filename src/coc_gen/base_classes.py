"""Base classes that can be specialised to implement different rulesets."""

from __future__ import annotations

from functools import total_ordering
from random import choice, randint, random
from typing import ClassVar

from faker import Faker

from .utils import dice


class Skill:
    """A CoC skill, with name and a default value."""

    def __init__(self, name: str, default_value: str) -> None:
        """Create a Skill.

        Args:
            name (str): Name of the skill
            default_value (str): A string describing the default value of the skill.
                                 See instance_value() for format of the string
        """
        self.name = name
        self.default_value = default_value

    def get_value(self, value: int) -> SkillValue:
        """Get a specific skill value.

        Args:
            value (int) : the specific value to get

        Returns:
            SkillValue : The skill value

        """
        return SkillValue(self, value)

    def instance_value(self, base_values: dict[str, int]) -> SkillValue:
        """Instanciate a default value for the skill.

        Args:
            base_values (dict[str, int]) : Base values to use for the calculation of the default value

        Returns:
            SkillValue : The skill value

        """
        if self.default_value.endswith("%"):
            return SkillValue(self, int(self.default_value[:-1]))

        if "/" in self.default_value:
            b, f = self.default_value.split("/")
            return SkillValue(self, int(base_values[b] / int(f)))

        return SkillValue(self, base_values[self.default_value])


@total_ordering
class SkillValue:
    """A specific value of a skill.

    The skill can be accessed via skill and the value via value
    It is ordered via the value (also against integers)
    It supports addition and subtraction with other SkillValue:s and integers.
    """

    def __init__(self, skill: Skill, value: int) -> None:
        """Create a specific value for a skill.

        Args:
            skill (Skill): The skill
            value (int): The value
        """
        self.skill = skill
        self.value = value

    @property
    def half_value(self) -> int:
        """The half value.

        Returns:
            int : the half value

        """
        return int(self.value / 2)

    @property
    def fifth_value(self) -> int:
        """The fifth value.

        Returns:
            int : the fifth value

        """
        return int(self.value / 5)

    def __add__(self, other) -> SkillValue:  # noqa: ANN001, D105
        if hasattr(other, "value"):
            return self.__class__(self.skill, self.value + other.value)
        if isinstance(other, (int, float)):
            return self.__class__(self.skill, self.value + int(other))

        msg = "Unsupported operand type(s) for +"
        raise TypeError(msg)

    def __sub__(self, other) -> SkillValue:  # noqa: ANN001, D105
        if hasattr(other, "value"):
            return self.__class__(self.skill, self.value - other.value)
        if isinstance(other, (int, float)):
            return self.__class__(self.skill, self.value - int(other))

        msg = "Unsupported operand type(s) for -"
        raise TypeError(msg)

    def __eq__(self, other) -> bool:  # noqa: ANN001, D105
        if isinstance(other, (int, float)):
            return self.value == other
        if hasattr(other, "value"):
            return self.value == other.value
        return NotImplemented

    def __lt__(self, other) -> bool:  # noqa: ANN001, D105
        if isinstance(other, (int, float)):
            return self.value < other
        if hasattr(other, "value"):
            return self.value < other.value
        return NotImplemented

    def __repr__(self) -> str:  # noqa: D105
        return f"{self.value}"


class Occupation:
    """An Occupation."""

    _special_skills: ClassVar = {}
    _skills: ClassVar = {}
    _basevalues: ClassVar = {}

    def __init__(
        self,
        name: str,
        skill_points: str,
        credit_range: tuple[int, int],
        occupation_skills: list[str],
    ) -> None:
        """Create an Occupation.

        Args:
            name (str) : Name of the occupation
            skill_points (str) : The number of skill points the Occupation gets
                (for syntax see calc_skillpoints())
            credit_range (tuple[int,int]) : Min and max credit range for the occupation
            occupation_skills (list[str]) : list of possible skill

        """
        self.name = name
        self.skill_points = skill_points
        self.credit_range = credit_range
        self.occupation_skills = occupation_skills

    def calc_skillpoint(self, basevalues: dict[str, int]) -> int:
        """Calculate the skillpoint for this occupation with the given base values.

        The syntax of the occupations skill point settings are something like:
            "UTB×2+STY×2" or "UTB×4" ie. multiplication of a base values with
            integers and then optional addition addition

        Args:
            basevalues (dict[str,int]) : The base values of the character that
                have the occupation.

        Returns:
            int : the calculated skill points

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
        """Get a instance of skills for the occupation.

        Any skills that are a key to the special_skills dictionary
        are replaced with a random skill from the keys item.
        The returned skills are in a random order.

        Returns:
            list[str] : _description_

        """
        inst = set()
        for skill in self.occupation_skills:
            if skill in self._special_skills:
                inst.add(self._skills[choice(self._special_skills[skill])])
            else:
                inst.add(self._skills[skill])

        return sorted(inst, key=lambda x: random())  # noqa: ARG005

    def __repr__(self) -> str:  # noqa: D105
        return f"Occupation('{self.name}')"


class Investigator:
    """An Investigator.

    See __init__() for creation options
    """

    _occupations: ClassVar[list[Occupation]] = {}
    _skills: ClassVar = {}
    _credit_rating: ClassVar[str] = "Credit Rating"
    _basevalues: ClassVar = {}

    def __init__(  # noqa: C901, PLR0912, PLR0913
        self,
        locale: str | None = None,
        sex: str | None = None,
        name: str | None = None,
        basevalues: dict[str, int] | None = None,
        occupation: str | None = None,
        skills: dict[str, int] | None = None,
    ) -> None:
        """Create an Investigator.

        Args:
            locale (str, optional): The locale the Investigator is active in.
                Sent to Faker that is used to create their name.
                More info: https://faker.readthedocs.io/en/stable/#localization. Defaults to None.
            sex (str, optional): Sex of the Investigator, if None random. Defaults to None.
            name (str, optional): Name of the Investigator, if None random according to the locale. Defaults to None.
            basevalues (dict[str,int], optional): Basevalues of the Investigator, if None random. Defaults to None.
            occupation (str, optional): Occupation of the Investigator, if None random. Defaults to None.
            skills (dict[str,int], optional): _description_. Defaults to None.
        """
        self.fake = Faker(locale=locale)

        if sex in ("F", "M"):
            self.sex = sex
        else:
            self.sex = choice(("F", "M"))

        if name:
            self.name = name
        elif self.sex == "F":
            self.name = f"{self.fake.first_name_female()} {self.fake.last_name()}"
        else:
            self.name = f"{self.fake.first_name_male()} {self.fake.last_name()}"
            # TODO: this does not work in locales dont follow the first/last naming convention

        if basevalues is None:
            basevalues = {}
        self.basevalues = {}

        for val, roll in self._basevalues.items():
            self.basevalues[val] = basevalues.get(val, dice.roll(roll) * 5)

        if occupation:
            self.occupation = self._occupations[occupation]
        else:
            self.occupation = choice(list(self._occupations.values()))

        if not skills:
            skill_points = self.occupation.calc_skillpoint(self.basevalues)

            credit_val = randint(*self.occupation.credit_range)
            credit = self._skills[self._credit_rating].get_value(credit_val)
            self.skills = {self._credit_rating: credit}

            skill_points -= credit_val

            for skill in self.occupation.get_skill_instance():
                curr_value = skill.instance_value(self.basevalues)
                addition = randint(0, min(90 - curr_value.value, skill_points))
                skill_points -= addition
                self.skills[skill.name] = curr_value + addition

            while skill_points:
                skill = choice(list(self.skills.keys()))
                if self.skills[skill] < 100:  # noqa: PLR2004
                    self.skills[skill] += 1
                    skill_points -= 1
        else:
            self.skills = {}
            for skill, value in skills.items():
                self.skills[skill] = SkillValue(self._skills[skill], value)

    def __getattr__(self, name: str) -> int:  # noqa: D105
        if name in self.basevalues:
            return self.basevalues[name]
        raise AttributeError

    def __repr__(self) -> str:  # noqa: D105
        return f"""Investigator(
    name = '{self.name}',
    sex = '{self.sex}',
    basevalues = {self.basevalues},
    occupation = '{self.occupation.name}',
    skills = '{self.skills}',
)"""

    @property
    def as_dict(self) -> dict:
        """Return a dict that describes the investigator, sutable to use in from_dict().

        Returns:
            dict -- _description_
        """
        return {
            "sex": self.sex,
            "name": self.name,
            "basevalues": self.basevalues,
            "occupation": self.occupation.name,
            "skills": self.skills,
        }

    @classmethod
    def from_dict(cls, d: dict) -> Investigator:
        """Create an investigator from a dict in the format returned by as_dict().

        Args:
            d (dict) : The dict

        Returns:
            Investigator -- The investigator
        """
        return cls(
            sex=d["sex"],
            name=d["name"],
            basevalues=d["basevalues"],
            occupation=d["occupation"],
            skills=d["skills"],
        )
