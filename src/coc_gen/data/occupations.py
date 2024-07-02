"""
Occupations
"""

# TODO: Add support for non Swedish rule sets
# pylint: disable=too-many-lines
from random import choice, random

from . import skills

# A dict containing all Occupations, keys are the names
occupations = {}


class Occupation:
    """
    An Occupation
    """

    def __init__(self, name, skill_points, credit_range, occupation_skills) -> None:
        """
        Create an Occupation

        Arguments:
            name {str} -- Name of the occupation
            skill_points {str} -- The number of skill points the Occupation gets
                (for syntax see calc_skillpoints())
            credit_range {(int,int)} -- Min and max credit range for the occupation
            occupation_skills {tuple(str)} -- list of possible skill
        """

        self.name = name
        self.skill_points = skill_points
        self.credit_range = credit_range
        self.occupation_skills = occupation_skills

        occupations[name] = self

    def calc_skillpoint(self, basevalues):
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
        skill_points = 0
        for term in self.skill_points.split("+"):
            bv, factor = term.split("×")
            skill_points += basevalues[bv] * int(factor)
        return skill_points

    def get_skill_instance(self):
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
            if skill in special_skills:
                inst.add(choice(special_skills[skill]))
            else:
                inst.add(skill)

        return sorted(inst, key=lambda x: random())

    def __repr__(self) -> str:
        return f"Occupation('{self.name}')"


special_skills = {
    "RANDOM": (list(skills.skills.keys())),
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
    "SCIENCE": ([s for s in skills.skills if s.startswith("Vetenskap ")]),
    "ART": ([s for s in skills.skills if s.startswith("Konst & hantverk ")]),
    "DRIVER": ([s for s in skills.skills if s.startswith("Chaufför ")]),
    "SURVIVAL": ([s for s in skills.skills if s.startswith("Överlevnad ")]),
    "GUN": ([s for s in skills.skills if s.startswith("Skjutvapen ")]),
    "COMBAT": ([s for s in skills.skills if s.startswith("Strid ")]),
}


Occupation(
    "Agitator",
    "UTB×2+KAR×2",
    (8, 25),
    (
        "Bibliotekskunskap",
        "Charma",
        "Bluffa",
        "Konst & hantverk (Skådespelare)",
        "Psykologi",
        "Språk (Annat)",
        "Övertyga",
        "RANDOM",
    ),
)
Occupation(
    "Antikhandlare",
    "UTB×4",
    (30, 50),
    (
        "Bibliotekskunskap",
        "Bokföring",
        "Historia",
        "Språk (Annat)",
        "Språk (Annat)",
        "Värdering",
        "SOCIAL",
        "SOCIAL",
    ),
)
Occupation(
    "Arbetare",
    "UTB×2+STY×2",
    (8, 30),
    (
        "Finna dolda ting",
        "Klättra",
        "Lyssna",
        "Strid (Handgemäng)",
        "WORKER",
        "WORKER",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Arkeolog",
    "UTB×4",
    (10, 40),
    (
        "Arkeologi",
        "Bibliotekskunskap",
        "Historia",
        "Mekaniker",
        "Navigera",
        "Språk (Annat)",
        "Vetenskap (Fysik)",
        "Vetenskap (Geologi)",
        "Vetenskap (Kemi)",
        "Värdering",
    ),
)
Occupation(
    "Arkitekt",
    "UTB×4",
    (30, 70),
    (
        "Bibliotekskunskap",
        "Bokföring",
        "Konst & hantverk (Tekniska Ritningar)",
        "Juridik",
        "Psykologi",
        "Språk (Annat)",
        "Vetenskap (Matematik)",
        "Övertyga",
    ),
)
Occupation(
    "Bedragare",
    "UTB×4",
    (9, 60),
    (
        "Bibliotekskunskap",
        "Bluffa",
        "Bokföring",
        "Charma",
        "Juridik",
        "Konst & hantverk (Förfalskning)",
        "Språk (Annat)",
        "Värdering",
    ),
)
Occupation(
    "Betjänt/Hembiträde",
    "UTB×2+KAR×2",
    (9, 35),
    (
        "Bokföring",
        "Värdering",
        "Finna dolda ting",
        "Första hjälpen",
        "Konst & hantverk (Barberare)",
        "Konst & hantverk (Matlagning)",
        "Konst & hantverk (Sömnad)",
        "Språk (Annat)",
        "Psykologi",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Bibliotekarie",
    "UTB×4",
    (9, 35),
    (
        "Bibliotekskunskap",
        "Bokföring",
        "Språk (Annat)",
        "Språk (Eget)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Bokhållare",
    "UTB×4",
    (30, 60),
    (
        "Bibliotekskunskap",
        "Bokföring",
        "Finna dolda ting",
        "Juridik",
        "Lyssna",
        "Övertyga",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Brandsoldat",
    "UTB×2+SMI×2",
    (10, 25),
    (
        "Chaufför (Bil)",
        "Första hjälpen",
        "Hoppa",
        "Kasta",
        "Klättra",
        "Simma",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Bartender/Krögare",
    "UTB×2+KAR×2",
    (8, 30),
    (
        "Bokföring",
        "Finna dolda ting",
        "Konst & hantverk (Matlagning)",
        "Lyssna",
        "Psykologi",
        "Strid (Handgemäng)",
        "SOCIAL",
        "RANDOM",
    ),
)
Occupation(
    "Bokhandlare",
    "UTB×4",
    (20, 40),
    (
        "Bibliotekskunskap",
        "Bokföring",
        "Chaufför (Bil)",
        "Historia",
        "Språk (Annat)",
        "Språk (Eget)",
        "Värdering",
        "RANDOM",
    ),
)
Occupation(
    "Chaufför",
    "UTB×2+SMI×2",
    (8, 20),
    (
        "Chaufför (Bil)",
        "Chaufför (Droska)",
        "Chaufför (Lastbil)",
        "Chaufför (Motorcykel)",
        "Chaufför (Traktor)",
        "Elektriker",
        "Finna dolda ting",
        "Maskinist",
        "Mekaniker",
        "Navigera",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Cirkusartist",
    "UTB×2+SMI×2",
    (8, 20),
    (
        "Finna dolda ting",
        "Hoppa",
        "Ducka",
        "Kasta",
        "Klättra",
        "Simma",
        "Konst & hantverk (Skådespelare)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Daglönare",
    "UTB×2+STY×2",
    (0, 10),
    (
        "Chaufför (Bil)",
        "Chaufför (Lastbil)",
        "Hoppa",
        "Klättra",
        "Mekaniker",
        "Konst & hantverk (Sprängteknik)",
        "Strid (Handgemäng)",
        "Bluffa",
        "Hota",
        "RANDOM",
    ),
)
Occupation(
    "Dräng/Piga/Statare",
    "UTB×2+STY×2",
    (1, 9),
    (
        "Chaufför (Droska)",
        "Konst & hantverk (Dressyr)",
        "Hoppa",
        "Klättra",
        "Naturkunskap",
        "Smyga",
        "Spåra",
        "RANDOM",
    ),
)
Occupation(
    "Dykare",
    "UTB×2+STY×2",
    (8, 30),
    (
        "Dyka",
        "Första hjälpen",
        "Mekaniker",
        "Klättra",
        "Simma",
        "Konst & hantverk (Sprängteknik)",
        "Skeppare",
        "RANDOM",
    ),
)
Occupation(
    "Estradör",
    "UTB×2+KAR×2",
    (21, 60),
    (
        "Bluffa",
        "Bokföring",
        "Charma",
        "Konst & hantverk (Skådespelare)",
        "Språk (Annat)",
        "Övertyga",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Fabrikör",
    "UTB×4",
    (40, 90),
    (
        "Bokföring",
        "Juridik",
        "Psykologi",
        "Språk (Annat)",
        "SCIENCE",
        "RANDOM",
        "SOCIAL",
        "SOCIAL",
    ),
)
Occupation(
    "Fotograf",
    "UTB×4",
    (9, 30),
    (
        "Charma",
        "Konst & hantverk (Fotografi)",
        "ART",
        "Mekaniker",
        "Språk (Annat)",
        "Vetenskap (Kemi)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Författare",
    "UTB×4",
    (9, 40),
    (
        "Bibliotekskunskap",
        "Historia",
        "Konst & hantverk (Författare)",
        "Naturkunskap",
        "Ockultism",
        "Psykologi",
        "Språk (Annat)",
        "Språk (Eget)",
        "RANDOM",
    ),
)
Occupation(
    "Idrottare",
    "UTB×2+SMI×2",
    (9, 30),
    (
        "Hoppa",
        "Kasta",
        "Klättra",
        "Rida",
        "Simma",
        "Strid (Handgemäng)",
        "SOCIAL",
        "RANDOM",
    ),
)
Occupation(
    "Ingenjör",
    "UTB×4",
    (30, 90),
    (
        "Bibliotekskunskap",
        "Elektriker",
        "Mekaniker",
        "Språk (Annat)",
        "Vetenskap (Matematik)",
        "Vetenskap (Ingenjörskonst)",
        "SCIENCE",
        "RANDOM",
    ),
)
Occupation(
    "Journalist",
    "UTB×4",
    (9, 40),
    (
        "Bibliotekskunskap",
        "Historia",
        "Konst & hantverk (Författare)",
        "Psykologi",
        "Språk (Annat)",
        "Språk (Eget)",
        "Övertyga",
        "RANDOM",
    ),
)
Occupation(
    "Jurist",
    "UTB×4",
    (40, 90),
    (
        "Bibliotekskunskap",
        "Bokföring",
        "Historia",
        "Juridik",
        "Språk (Annat)",
        "Språk (Eget)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Konstkännare",
    "UTB×4",
    (30, 70),
    (
        "Bibliotekskunskap",
        "Finna dolda ting",
        "ART",
        "Språk (Annat)",
        "Språk (Annat)",
        "Värdering",
        "RANDOM",
    ),
)
Occupation(
    "Konstnär",
    "UTB×2+KAR×2",
    (9, 50),
    (
        "Finna dolda ting",
        "Historia",
        "Naturkunskap",
        "ART",
        "Psykologi",
        "Språk (Annat)",
        "SOCIAL",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Landsfiskal",
    "UTB×4",
    (20, 50),
    (
        "Bokföring",
        "Finna dolda ting",
        "Juridik",
        "Vetenskap (Kriminalteknik)",
        "Skjutvapen (Pistol)",
        "Strid (Handgemäng)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Lantbrukare",
    "UTB×4",
    (20, 70),
    (
        "Bokföring",
        "Finna dolda ting",
        "Juridik",
        "Vetenskap (Kriminalteknik)",
        "Skjutvapen (Pistol)",
        "Strid (Handgemäng)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Ligist",
    "UTB×2+STY×2",
    (0, 8),
    (
        "Fingerfärdighet",
        "Hoppa",
        "Hota",
        "Kasta",
        "Klättra",
        "Lyssna",
        "Smyga",
        "Strid (Handgemäng)",
    ),
)
Occupation(
    "Luffare",
    "UTB×2+SMI×2",
    (0, 8),
    (
        "Finna dolda ting",
        "Klättra",
        "Lyssna",
        "Naturkunskap",
        "Smyga",
        "Språk (Luffarjargong)",
        "SURVIVAL",
        "RANDOM",
    ),
)
Occupation(
    "Läkare",
    "UTB×4",
    (4, 90),
    (
        "Bibliotekskunskap",
        "Första hjälpen",
        "Läkekonst",
        "Språk (Annat)",
        "Vetenskap (Biologi)",
        "Vetenskap (Läkemedel)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Mekaniker",
    "UTB×2+SMI×2",
    (8, 30),
    (
        "Bokföring",
        "DRIVER",
        "Elektriker",
        "Maskinist",
        "Mekaniker",
        "Värdering",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Mentalvårdare",
    "UTB×4+STY×2",
    (10, 40),
    (
        "Finna dolda ting",
        "Första hjälpen",
        "Hota",
        "Lyssna",
        "Strid (Handgemäng)",
        "Psykologi",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Missionär",
    "UTB×4",
    (10, 30),
    (
        "Bibliotekskunskap",
        "Första hjälpen",
        "Konst & hantverk (Författare)",
        "Språk (Annat)",
        "Psykologi",
        "Övertyga",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Musiker",
    "UTB×2+KAR×2",
    (9, 30),
    (
        "Konst & hantverk (valfritt instrument)",
        "Lyssna",
        "Psykologi",
        "SOCIAL",
        "RANDOM",
        "RANDOM",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Nåjd",
    "UTB×2+VST×2",
    (5, 15),
    (
        "ART",
        "Naturkunskap",
        "Ockultism",
        "Smyga",
        "Spåra",
        "Språk (Svenska)",
        "Överlevnad (Arktis)",
        "RANDOM",
    ),
)
Occupation(
    "Officer",
    "UTB×4",
    (20, 70),
    (
        "Ducka",
        "Första hjälpen",
        "Psykologi",
        "Rida",
        "COMBAT",
        "GUN",
        "Övertyga",
        "RANDOM",
    ),
)
Occupation(
    "Pilot",
    "UTB×4",
    (15, 40),
    (
        "Elektriker",
        "Mekaniker",
        "Navigera",
        "Pilot",
        "Språk (Annat)",
        "Vetenskap (Meteorologi)",
        "RANDOM",
    ),
)
Occupation(
    "Polisdetektiv",
    "UTB×4",
    (20, 40),
    (
        "Bibliotekskunskap",
        "Bluffa",
        "Finna dolda ting",
        "Vetenskap (Kriminalteknik)",
        "Psykologi",
        "Skjutvapen (Pistol)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Poliskonstapel",
    "UTB×4",
    (10, 30),
    (
        "Chaufför (Bil)",
        "Finna dolda ting",
        "Vetenskap (Kriminalteknik)",
        "Skjutvapen (Pistol)",
        "Strid (Handgemäng)",
        "Strid (Sabel)",
        "Psykologi",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Polissyster",
    "UTB×4",
    (10, 30),
    (
        "Bokföring",
        "Charma",
        "Finna dolda ting",
        "Första hjälpen",
        "Vetenskap (Kriminalteknik)",
        "Psykologi",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Präst",
    "UTB×4",
    (9, 60),
    (
        "Bibliotekskunskap",
        "Bokföring",
        "Historia",
        "Lyssna",
        "Psykologi",
        "Språk (Annat)",
        "Övertyga",
        "RANDOM",
    ),
)
Occupation(
    "Psykolog",
    "UTB×4",
    (10, 40),
    (
        "Bibliotekskunskap",
        "Bokföring",
        "Lyssna",
        "Psykoanalys",
        "Psykologi",
        "Övertyga",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Redaktör/Förläggare",
    "UTB×4",
    (25, 60),
    (
        "Bibliotekskunskap",
        "Bokföring",
        "Historia",
        "Konst & hantverk (Författare)",
        "Psykologi",
        "Språk (Annat)",
        "Övertyga",
        "RANDOM",
    ),
)
Occupation(
    "Renskötare",
    "UTB×2+STY×2",
    (5, 15),
    (
        "Kasta",
        "ART",
        "Naturkunskap",
        "Språk (Svenska)",
        "Spåra",
        "Värdering",
        "Överlevnad (Arktis)",
        "RANDOM",
    ),
)
Occupation(
    "Revolutionär",
    "UTB×4",
    (9, 20),
    (
        "Bibliotekskunskap",
        "Bluffa",
        "Förklädnad",
        "Historia",
        "Hota",
        "Skjutvapen (Pistol)",
        "Övertyga",
        "RANDOM",
    ),
)
Occupation(
    "Samisk jägare",
    "UTB×2+FYS×2",
    (5, 15),
    (
        "ART",
        "Naturkunskap",
        "Skjutvapen (Gevär)",
        "Smyga",
        "Spåra",
        "Språk (Svenska)",
        "Överlevnad (Arktis)",
        "RANDOM",
    ),
)
Occupation(
    "Sekreterare",
    "UTB×4",
    (9, 20),
    (
        "Bibliotekskunskap",
        "Finna dolda ting",
        "Lyssna",
        "Psykologi",
        "Språk (Annat)",
        "Språk (Eget)",
        "SOCIAL",
        "RANDOM",
    ),
)
Occupation(
    "Sjuksköterska",
    "UTB×4",
    (10, 40),
    (
        "Bibliotekskunskap",
        "Första hjälpen",
        "Läkekonst",
        "Psykologi",
        "Språk (Annat)",
        "Vetenskap (Läkemedel)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Sjöman",
    "UTB×2+SMI×2",
    (9, 20),
    (
        "Hoppa",
        "Kasta",
        "Klättra",
        "Navigera",
        "Simma",
        "Skeppare",
        "Språk (Annat)",
        "RANDOM",
    ),
)
Occupation(
    "Teaterskådespelare",
    "UTB×2+KAR×2",
    (9, 40),
    (
        "Förklädnad",
        "Historia",
        "Konst & hantverk (Skådespelare)",
        "Psykologi",
        "Strid (Handgemäng)",
        "SOCIAL",
        "SOCIAL",
        "RANDOM",
    ),
)
Occupation(
    "Filmskådespelare",
    "UTB×2+KAR×2",
    (15, 80),
    (
        "Chaufför (Bil)",
        "Förklädnad",
        "Konst & hantverk (Skådespelare)",
        "Psykologi",
        "Strid (Handgemäng)",
        "SOCIAL",
        "SOCIAL",
        "RANDOM",
    ),
)
Occupation(
    "Soldat",
    "UTB×2+STY×2",
    (5, 15),
    (
        "Chaufför (Droska)",
        "Ducka",
        "Hoppa",
        "Klättra",
        "GUN",
        "GUN",
        "Smyga",
        "RANDOM",
    ),
)
Occupation(
    "Spiritist",
    "UTB×4",
    (10, 45),
    (
        "Bluffa",
        "Charma",
        "Fingerfärdighet",
        "Ockultism",
        "Konst & hantverk (Skådespelare)",
        "Övertyga",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Spritsmugglare",
    "UTB×4",
    (15, 60),
    (
        "Charma",
        "Mekaniker",
        "Navigera",
        "Simma",
        "Skeppare",
        "Språk (Annat)",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Student",
    "UTB×4",
    (8, 40),
    (
        "Bibliotekskunskap",
        "Konst & hantverk (Författare)",
        "Språk (Annat)",
        "Språk (Annat 2)",
        "SCIENCE",
        "Övertyga",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Universitetslärare",
    "UTB×4",
    (20, 80),
    (
        "Bibliotekskunskap",
        "Konst & hantverk (Författare)",
        "Språk (Annat)",
        "Språk (Annat 2)",
        "SCIENCE",
        "Övertyga",
        "RANDOM",
        "RANDOM",
    ),
)
Occupation(
    "Upptäcktsresande",
    "UTB×2+STY×2",
    (10, 50),
    (
        "Bibliotekskunskap",
        "Finna dolda ting",
        "Navigera",
        "Skjutvapen (Gevär)",
        "Språk (Annat)",
        "SCIENCE",
        "SURVIVAL",
        "RANDOM",
    ),
)
