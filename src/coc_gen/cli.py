"""Command line interface."""

import click

from coc_gen import RULESETS, get_investgator_class


@click.command(context_settings={"show_default": True})
@click.option(
    "--ruleset",
    default="coc_swe",
    type=click.Choice(RULESETS, case_sensitive=False),
    help="What ruleset to use.",
)
@click.option(
    "--locale",
    default=None,
    type=str,
    help="Where do the Investigator come from.",
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
def investigator(
    ruleset: str,
    locale: str,
    number: int,
    sex: str,
    occupation: str,
) -> None:
    """Generate Call of Cthulhu investigators.

    Args:
        ruleset (str): What ruleset to use.
        locale (str): Where do the Investigator come from.
        number (int): Number of investigators to generate.
        sex (str): The sec of the investigator.
        occupation (str): The occupation of the investigator.
    """
    investigater_class = get_investgator_class(ruleset)
    for _ in range(number):
        print(investigater_class(locale=locale, sex=sex, occupation=occupation))  # noqa: T201
