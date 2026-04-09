import requests
import json


# Determines the method and sends the request
def send_request(method: str, url: str, parsed_headers: str = None, parsed_body = None) -> dict :

    method = method.upper()

    if method == "GET":
        response = requests.get(url, headers=parsed_headers)

    elif method in ["POST", "PUT", "PATCH"]:
        response = requests.post(url, headers=parsed_headers, json=parsed_body)

    else:
        raise ValueError("Method must be GET, POST, PUT, PATCH, or DELETE")



    return response

