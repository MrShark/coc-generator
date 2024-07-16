"""
Classes that represents an Investigator
"""

import click

from coc_gen import RULESETS, get_investgator_class


@click.command(context_settings={"show_default": True})
@click.option(
    "--ruleset",
    default="coc_swe",
    type=click.Choice(RULESETS, case_sensitive=False),
    help="What ruleset to use",
)
@click.option(
    "--locale",
    default=None,
    type=str,
    help="Where do the Investigator come from",
)
@click.option(
    "--number",
    default=1,
    type=int,
    help="Number of investigators to generate.",
)
@click.option(
    "--sex",
    default=None,
    type=str,
    help="The sex of the investigator.",
)
@click.option(
    "--occupation",
    default=None,
    type=str,
    help="The occupation of the investigator.",
)
def investigator(ruleset, locale, number, sex, occupation):
    """Generate Call of Cthulhu investigators."""
    investigater_class = get_investgator_class(ruleset)
    for _ in range(number):
        print(investigater_class(locale=locale, sex=sex, occupation=occupation))
