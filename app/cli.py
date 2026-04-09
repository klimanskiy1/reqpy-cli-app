import click
from app.request_manage.request_flow import get_sort_answer


@click.group()
def main():
    pass

@main.command()
@click.argument("method")
@click.argument("url")
@click.option("--headers", default=None, help="Request headers in JSON format")
@click.option("--body", default=None, help="Request body in JSON format")
def send(method: str, url: str, headers: str, body:str):
    """
    Send HTTP request
    Example: reqpy send GET https://www.google.com
    """
    get_sort_answer(method, url, headers, body)

