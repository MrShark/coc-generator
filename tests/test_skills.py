from coc_gen.base_classes import Skill, SkillValue


def test_skill():
    skill = Skill("test", "10%")
    value = skill.instance_value({})

    assert skill.name == "test"
    assert value.skill == skill
    assert value.value == 10


def test_value_add():
    skill = Skill("test", "10%")
    value1 = SkillValue(skill, 10)
    value2 = SkillValue(skill, 15)

    assert (value1 + value2).value == 25
    assert (value1 + 2).value == 12
