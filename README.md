# ReqPy

A console HTTP client — the part of Postman you actually use, without leaving the
terminal.

```bash
reqpy send GET https://api.github.com/users/klimanskiy1
```

## Install

```bash
git clone https://github.com/klimanskiy1/htpy-cli-app.git
cd htpy-cli-app
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -e .
```

`pip install -e .` registers the `reqpy` command in the active environment.

## Usage

```
reqpy send METHOD URL [options]
```

| Option | Short | Description |
| --- | --- | --- |
| `--headers` | `-H` | Headers as a JSON object, or a single `Key: value` pair |
| `--body` | `-B` | Request body as JSON |
| `--output` | `-o` | `full` (default), `status`, `body`, or `time` |

A URL without a scheme gets `http://` prepended, so `reqpy send GET example.com`
works.

### Examples

```bash
# Simplest form
reqpy send GET example.com

# Status code only — handy in scripts
reqpy send GET https://api.github.com -o status

# A single header, without JSON quoting
reqpy send GET https://api.github.com/user -H "Authorization: Bearer $TOKEN"

# Several headers
reqpy send GET https://api.example.com -H '{"Accept": "application/json", "X-Trace": "1"}'

# POST with a JSON body, printing just the response body
reqpy send POST https://httpbin.org/post -B '{"name": "test"}' -o body
```

### Output modes

| Mode | Prints |
| --- | --- |
| `full` | Status, headers, body and elapsed time |
| `status` | Status code |
| `body` | Response body — JSON is pretty-printed |
| `time` | Round-trip time in milliseconds |

JSON responses are indented and kept in their original encoding, so Cyrillic and
other non-ASCII text stays readable instead of turning into escape sequences.

## Status

Early version, and honest about it:

- **Methods** — `GET` and `POST` are implemented. `PUT` and `PATCH` are accepted
  but currently dispatched as `POST`; `DELETE` is not wired up yet.
- **Collections** — saving and replaying named requests is the next thing planned,
  not something that works today.
- **Tests** — the package is laid out for them; they are not written yet.

## Stack

Python · Click · Requests
