import click
import json


def format_answer(parsed_answer: dict, output="full") -> None:
    """
    Pretty print HTTP response to console
    """
    if output == "full":

        # Status
        status_code = parsed_answer["status_code"]

        if 200 <= status_code < 300:
            click.echo(
                f"\n{click.style('Status:', bold=True)} {click.style(str(status_code), fg='green')}\n"
            )
        elif 400 <= status_code < 500:
            click.echo(
                f"\n{click.style('Status:', bold=True)} {click.style(str(status_code), fg='red')}\n"
            )
        else:
            click.echo(
                f"\n{click.style('Status:', bold=True)} {click.style(str(status_code), fg='yellow')}\n"
            )

        # Time
        time = parsed_answer["time"]
        if time <= 3000:
            click.echo(f"{click.style('Time:', bold=True)} {click.style(str(time), fg='green')} ms\n")
        elif 3000 < time < 8000:
            click.echo(f"{click.style('Time:', bold=True)} {click.style(str(time), fg='yellow')} ms\n")
        else:
            click.echo(f"{click.style('Time:', bold=True)} {click.style(str(time), fg='red')} ms\n")

        # Headers
        click.secho("Headers:", bold=True)
        click.echo("-" * 40)

        for key, value in parsed_answer["headers"].items():
            click.echo(f"{key}: {value}")

        # Body

        click.secho("\nBody:", bold=True)
        click.echo("-" * 40)
        click.echo(parsed_answer["body"])

    elif output == "status":
        # Status
        status_code = parsed_answer["status_code"]

        if 200 <= status_code < 300:
            click.echo(
                f"\n{click.style('Status:', bold=True)} {click.style(str(status_code), fg='green')}\n"
            )
        elif 400 <= status_code < 500:
            click.echo(
                f"\n{click.style('Status:', bold=True)} {click.style(str(status_code), fg='red')}\n"
            )
        else:
            click.echo(
                f"\n{click.style('Status:', bold=True)} {click.style(str(status_code), fg='yellow')}\n"
            )

    elif output == "time":

        time = parsed_answer["time"]
        if time <= 3000:
            click.echo(f"{click.style('Time:', bold=True)} {click.style(str(time), fg='green')} ms\n")
        elif 3000 < time < 8000:
            click.echo(f"{click.style('Time:', bold=True)} {click.style(str(time), fg='yellow')} ms\n")
        else:
            click.echo(f"{click.style('Time:', bold=True)} {click.style(str(time), fg='red')} ms\n")

    elif output == "body":
        click.secho("\nBody:", bold=True)
        click.echo("-" * 40)
        click.echo(parsed_answer["body"])
