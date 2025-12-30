# Echo REST API

A simple REST API built with FastAPI that echoes back request information including headers, request details, server IP, and server name.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the API

```bash
python echo_api.py
```

Or with uvicorn directly:
```bash
uvicorn echo_api:app --host 0.0.0.0 --port 5000 --reload
```

The server will start on `http://0.0.0.0:5000`

Interactive API documentation is available at `http://localhost:5000/docs`

## Usage

Make a GET request to the `/echo` endpoint:

```bash
curl http://localhost:5000/echo
```

Or with custom headers:

```bash
curl -H "X-Custom-Header: test" http://localhost:5000/echo?param1=value1
```

## Response Format

The API returns a JSON response with:
- `serverIP`: The server's IP address
- `serverName`: The server's hostname
- `headers`: All headers sent by the client
- `request`: Request details including method, URL, path, query parameters, etc.
