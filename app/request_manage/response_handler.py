import json


# Check answer types and compose the primary structure
def parse_response(response) -> dict:
    content_type = response.headers.get("Content-Type", "")

    if "application/json" in content_type:
        json_data =  response.json()
        data = json.dumps(json_data, indent=2, ensure_ascii=False)

    elif "text" in content_type or "html" in content_type:
        data = response.text

    else:
        data = response.content  # bytes

    parsed_answer = {
        "status_code": response.status_code,
        "headers": response.headers,
        "body": data,
        "time": int(response.elapsed.total_seconds() * 1000)
    }
    return parsed_answer


def parse_headers(headers):
    if not headers:
        return None
    headers = headers.strip()

    try:
        return json.loads(headers)

    except json.JSONDecodeError:

        key, value = headers.split(":", 1)
        return {key.strip(): value.strip()}


def parse_body(body):
    if not body:
        return None, None

    try:
        json_body = json.loads(body)
        return json_body, None

    except json.JSONDecodeError:

        return None, body
