from app.request_manage.request_sender import send_request
from app.request_manage.response_handler import parse_response, parse_headers, parse_body
from app.utils.formatter import format_answer


# Calls two functions and get result
def get_sort_answer(method: str, url: str, headers: str = None, body: str = None, output: str = "full") -> None:

    parsed_headers = parse_headers(headers)

    parsed_body = parse_body(body)

    response = send_request(method, url, parsed_headers=parsed_headers, parsed_body=parse_body)

    parsed_answer = parse_response(response)

    format_answer(parsed_answer, output)



