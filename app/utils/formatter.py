import click
import json


def format_answer(parsed_answer) -> None:
    """
    Pretty print HTTP response to console
    """

    # Status
    status_code = parsed_answer["status_code"]

    if 200 <=status_code < 300:
        click.secho(f"\nStatus: {status_code}", fg="green")
    elif 400 <= status_code < 500:
        click.secho(f"\nStatus: {status_code}", fg="red")
    else:
        click.secho(f"\nStatus: {status_code}", fg="yellow")

    # Time
    time = parsed_answer["time"]
    click.secho(f"Time: {time} ms\n")

    # Headers
    click.secho("Headers:", bold=True)
    click.echo("-" * 40)

    for key, value in parsed_answer["headers"].items():
        click.echo(f"{key}: {value}")

    # Body

    click.secho("\nBody:", bold=True)
    click.echo("-" * 40)
    click.echo(parsed_answer["body"])