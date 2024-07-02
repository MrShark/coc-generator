"""
Lists all skills and their base values
"""

skills = {
    "Antropologi": "1%",
    "Arkeologi": "1%",
    "Bibliotekskunskap": "20%",
    "Bluffa": "5%",
    "Bokföring": "5%",
    "Charma": "15%",
    "Chaufför (Bil)": "20%",
    "Chaufför (Droska)": "20%",
    "Chaufför (Lastbil)": "5%",
    "Chaufför (Motorcykel)": "5%",
    "Chaufför (Traktor)": "5%",
    "Cthulhumyten": "0%",
    "Ducka": "SMI/2",
    "Dyka": "1%",
    "Elektriker": "10%",
    "Fingerfärdighet": "10%",
    "Finna dolda ting": "25%",
    "Förklädnad": "5%",
    "Första hjälpen": "30%",
    "Historia": "5%",
    "Hoppa": "20%",
    "Hota": "15%",
    "Juridik": "5%",
    "Kasta": "20%",
    "Klättra": "20%",
    "Konst & hantverk (Barberare)": "5%",
    "Konst & hantverk (Dressyr)": "5%",
    "Konst & hantverk (Fotografi)": "5%",
    "Konst & hantverk (Förfalskning)": "5%",
    "Konst & hantverk (Författare)": "5%",
    "Konst & hantverk (Gruvarbete)": "5%",
    "Konst & hantverk (Matlagning)": "5%",
    "Konst & hantverk (Murare)": "5%",
    "Konst & hantverk (Målare)": "5%",
    "Konst & hantverk (Skogshuggare)": "5%",
    "Konst & hantverk (Skådespelare)": "5%",
    "Konst & hantverk (Snickare)": "5%",
    "Konst & hantverk (Sprängteknik)": "5%",
    "Konst & hantverk (Sömnad)": "5%",
    "Konst & hantverk (Tekniska Ritningar)": "5%",
    "Konst & hantverk (valfritt instrument)": "5%",
    "Levnadsstandard": "0%",
    "Lyssna": "20%",
    "Låssmed": "1%",
    "Läkekonst": "1%",
    "Läkemedel": "10%",
    "Maskinist": "1%",
    "Mekaniker": "10%",
    "Naturkunskap": "10%",
    "Navigera": "10%",
    "Ockultism": "5%",
    "Pilot - Propellerplan": "1%",
    "Pilot": "1%",
    "Psykoanalys": "1%",
    "Psykologi": "10%",
    "Rida": "5%",
    "Simma": "20%",
    "Skeppare": "1%",
    "Skjutvapen (Gevär)": "25%",
    "Skjutvapen (K-pist)": "15%",
    "Skjutvapen (Kulspruta)": "10%",
    "Skjutvapen (Pilbåge)": "15%",
    "Skjutvapen (Pistol)": "20%",
    "Skjutvapen (Spjut)": "20%",
    "Skjutvapen (Tyngre handeldvapen)": "10%",
    "Smyga": "20%",
    "Språk (Annat)": "1%",
    "Språk (Annat 2)": "1%",
    "Språk (Svenska)": "1%",
    "Språk (Eget)": "INT",
    "Språk (Luffarjargong)": "1%",
    "Spåra": "10%",
    "Strid (Eldkastare)": "10%",
    "Strid (Garott)": "15%",
    "Strid (Handgemäng)": "25%",
    "Strid (Piska)": "5%",
    "Strid (Slaga)": "10%",
    "Strid (Svärd)": "20%",
    "Strid (Sabel)": "20%",
    "Strid (Yxa)": "15%",
    "Vetenskap (Astronomi)": "1%",
    "Vetenskap (Biologi)": "1%",
    "Vetenskap (Botanik)": "1%",
    "Vetenskap (Fysik)": "1%",
    "Vetenskap (Geologi)": "1%",
    "Vetenskap (Ingenjörskonst)": "1%",
    "Vetenskap (Kemi)": "1%",
    "Vetenskap (Kriminalteknik)": "1%",
    "Vetenskap (Kryptografi)": "1%",
    "Vetenskap (Läkemedel)": "1%",
    "Vetenskap (Matematik)": "10%",
    "Vetenskap (Meteorologi)": "1%",
    "Vetenskap (Zoologi)": "1%",
    "Värdering": "5%",
    "Överlevnad (Arktis)": "10%",
    "Överlevnad (Berg)": "10%",
    "Överlevnad (Hav)": "10%",
    "Överlevnad (Regnskog)": "10%",
    "Överlevnad (Skog)": "10%",
    "Överlevnad (Stäpp)": "10%",
    "Överlevnad (Taiga)": "10%",
    "Överlevnad (Öken)": "10%",
    "Övertyga": "10%",
}


def get_defult_value(skill, base_values):
    """
    Get defult value for a skill.

    Arguments:
        skill {str} -- Name of the skill
        base_values {dict[str, int]} -- Base values to use for the calculation of the default value

    Returns:
        int -- the default value
    """
    default_val = skills[skill]
    if default_val.endswith("%"):
        return int(default_val[:-1])

    if "/" in default_val:
        b, f = default_val.split("/")
        return int(base_values[b] / int(f))

    return base_values[default_val]
