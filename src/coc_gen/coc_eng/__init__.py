from coc_gen.base_classes import Investigator, Occupation
from coc_gen.coc_eng.occupations import occupations_20s_data, occupations_modern_data
from coc_gen.coc_eng.skills import skills_20s, skills_modern

basevalues = {
    "APP": ("3D6"),
    "CON": ("3D6"),
    "DEX": ("3D6"),
    "EDU": ("2D6+6"),
    "INT": ("2D6+6"),
    "POW": ("3D6"),
    "SIZ": ("2D6+6"),
    "STR": ("3D6"),
}

special_skills_20s = {
    "RANDOM": (list(skills_20s.keys())),
    "SOCIAL": (
        "Charm",
        "Fast Talk",
        "Intimidate",
        "Persuade",
    ),
    "CRAFT": (
        "Art and Craft (Carpentry)",
        "Art and Craft (Welding)",
        "Art and Craft (Plumbing)",
    ),
    "ART": ([s for s in skills_20s if s.startswith("Art and Craft ")]),
    "FIGHT": ([s for s in skills_20s if s.startswith("Fighting ")]),
    "FIREARM": ([s for s in skills_20s if s.startswith("Firearms ")]),
    "SCIENCE": ([s for s in skills_20s if s.startswith("Science ")]),
    "SURVIVE": ([s for s in skills_20s if s.startswith("Survival ")]),
    "PILOT": ([s for s in skills_20s if s.startswith("Pilot ")]),
}

special_skills_modern = {
    "RANDOM": (list(skills_modern.keys())),
    "SOCIAL": (
        "Charm",
        "Fast Talk",
        "Intimidate",
        "Persuade",
    ),
    "CRAFT": (
        "Art and Craft (Carpentry)",
        "Art and Craft (Welding)",
        "Art and Craft (Plumbing)",
    ),
    "ART": ([s for s in skills_modern if s.startswith("Art and Craft ")]),
    "FIGHT": ([s for s in skills_modern if s.startswith("Fighting ")]),
    "FIREARM": ([s for s in skills_modern if s.startswith("Firearms ")]),
    "SCIENCE": ([s for s in skills_modern if s.startswith("Science ")]),
    "SURVIVE": ([s for s in skills_modern if s.startswith("Survival ")]),
    "PILOT": ([s for s in skills_modern if s.startswith("Pilot ")]),
}


class TwentiesOccupation(Occupation):
    _skills = skills_20s
    _special_skills = special_skills_20s
    _basevalues = basevalues


occupations_20s = {}
for name, data in occupations_20s_data.items():
    occupations_20s[name] = TwentiesOccupation(
        name=name,
        skill_points=data["skill_points"],
        credit_range=data["credit_range"],
        occupation_skills=data["skills"],
    )


class TwentiesInvestigator(Investigator):
    """
    An Investigator in Call of Cathulu Sverige
    """

    _occupations = occupations_20s
    _basevalues = basevalues
    _credit_rating = "Credit Rating"


class ModernOccupation(Occupation):
    _skills = skills_modern
    _special_skills = special_skills_modern
    _basevalues = basevalues


occupations_modern = {}
for name, data in occupations_modern_data.items():
    occupations_modern[name] = ModernOccupation(
        name=name,
        skill_points=data["skill_points"],
        credit_range=data["credit_range"],
        occupation_skills=data["skills"],
    )


class ModernInvestigator(Investigator):
    """
    An Investigator in Call of Cathulu Sverige
    """

    _occupations = occupations_modern
    _basevalues = basevalues
    _credit_rating = "Credit Rating"


if __name__ == "__main__":
    for o in occupations_20s_data.values():
        for s in o["skills"]:
            if s not in skills_20s and s not in special_skills_20s:
                print(s)
    for o in occupations_modern_data.values():
        for s in o["skills"]:
            if s not in skills_modern and s not in special_skills_modern:
                print(s)
