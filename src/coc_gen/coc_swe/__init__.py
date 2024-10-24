"""Ruleset for Call of ­Cthulhu Sverige."""

from coc_gen.base_classes import Investigator, Occupation

from .occupations import occupations_data
from .skills import skills

basevalues = {
    "FYS": ("3D6"),
    "INT": ("2D6+6"),
    "KAR": ("3D6"),
    "SMI": ("3D6"),
    "STO": ("2D6+6"),
    "STY": ("3D6"),
    "UTB": ("2D6+6"),
    "VST": ("3D6"),
}

special_skills = {
    "RANDOM": (list(skills.keys())),
    "SOCIAL": (
        "Hota",
        "Charma",
        "Övertyga",
        "Bluffa",
    ),
    "WORKER": (
        "Elektriker",
        "Konst & hantverk (Gruvarbete)",
        "Konst & hantverk (Murare)",
        "Konst & hantverk (Målare)",
        "Konst & hantverk (Snickare)",
        "Konst & hantverk (Skogshuggare)",
        "Maskinist",
        "Mekaniker",
        "Naturkunskap",
        "Överlevnad (Skog)",
    ),
    "SCIENCE": ([s for s in skills if s.startswith("Vetenskap ")]),
    "ART": ([s for s in skills if s.startswith("Konst & hantverk ")]),
    "DRIVER": ([s for s in skills if s.startswith("Chaufför ")]),
    "SURVIVAL": ([s for s in skills if s.startswith("Överlevnad ")]),
    "GUN": ([s for s in skills if s.startswith("Skjutvapen ")]),
    "COMBAT": ([s for s in skills if s.startswith("Strid ")]),
}


class SweOccupation(Occupation):
    """An Occupation."""

    _skills = skills
    _special_skills = special_skills
    _basevalues = basevalues


occupations = {}
for name, data in occupations_data.items():
    occupations[name] = SweOccupation(
        name=name,
        skill_points=data["skill_points"],
        credit_range=data["credit_range"],
        occupation_skills=data["skills"],
    )


class SweInvestigator(Investigator):
    """An Investigator in Call of Cathulu Sverige."""

    _occupations = occupations
    _skills = skills
    _basevalues = basevalues
    _credit_rating = "Levnadsstandard"
    _combat_base = ("STY", "STO")
