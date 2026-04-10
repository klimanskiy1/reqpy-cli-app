from app.request_manage.request_sender import send_request
from app.request_manage.r_handler import parse_response, parse_headers, parse_body, http_check
from app.utils.formatter import format_answer


# Calls two functions and get result
def get_sort_answer(method: str, url: str, headers: str = None, body: str = None, output: str = "full") -> None:
    """Calls the data parsing functions and the request sending function in turn."""

    url_after_http_check = http_check(url)  # Checks for HTTP at the beginning

    parsed_headers = parse_headers(headers)  # Parse headers in correct format

    parsed_body = parse_body(body)  # Parse body in correct format

    # Sends a request and receives a response
    response = send_request(method, url_after_http_check, parsed_headers=parsed_headers, parsed_body=parsed_body)

    # Parse response
    parsed_answer = parse_response(response)

    # A beautifully formatted answer
    format_answer(parsed_answer, output)



