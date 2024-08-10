"""Test Skill related classes."""

# ruff: noqa: S101, PLR2004

from coc_gen.base_classes import Skill, SkillValue


def test_skill() -> None:
    """Test the Skill class."""
    skill = Skill("test", "10%")
    value = skill.instance_value({})

    assert skill.name == "test"
    assert value.skill == skill
    assert value.value == 10


def test_value_add() -> None:
    """Test the SkillValue class."""
    skill = Skill("test", "10%")
    value1 = SkillValue(skill, 10)
    value2 = SkillValue(skill, 15)

    assert (value1 + value2).value == 25
    assert (value1 + 2).value == 12
