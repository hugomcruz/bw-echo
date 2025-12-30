from fastapi import FastAPI, Request
from typing import Any, Dict, Optional
import socket
import os

app = FastAPI()

@app.get('/echo')
async def echo_get(request: Request):
    # Get server information
    server_name = socket.gethostname()
    server_ip = socket.gethostbyname(server_name)
    
    # Get request headers as a dictionary
    headers = dict(request.headers)
    
    # Get cluster information from environment variables
    cluster_info = {
        'country': os.getenv('CLUSTER_COUNTRY', 'XX'),
        'location': os.getenv('CLUSTER_LOCATION', 'Not provided'),
        'providedBy': os.getenv('CLUSTER_PROVIDED_BY', 'Not provided')
    }
    
    # Prepare response
    response_data = {
        'serverIP': server_ip,
        'serverName': server_name,
        'cluster': cluster_info,
        'headers': headers,
        'request': {
            'method': request.method,
            'url': str(request.url),
            'path': request.url.path,
            'query_string': request.url.query,
            'args': dict(request.query_params),
            'remote_addr': request.client.host if request.client else None,
            'scheme': request.url.scheme,
            'host': request.url.hostname
        }
    }
    
    return response_data

@app.put('/echo')
async def echo_put(request: Request, payload: Optional[Dict[str, Any]] = None):
    # Get server information
    server_name = socket.gethostname()
    server_ip = socket.gethostbyname(server_name)
    
    # Get request headers as a dictionary
    headers = dict(request.headers)
    
    # Get payload from request body
    try:
        body = await request.json()
    except:
        body = (await request.body()).decode('utf-8') if await request.body() else None
    
    # Get cluster information from environment variables
    cluster_info = {
        'country': os.getenv('CLUSTER_COUNTRY', 'CZ'),
        'location': os.getenv('CLUSTER_LOCATION', 'Datacenter Location'),
        'providedBy': os.getenv('CLUSTER_PROVIDED_BY', 'NCAL')
    }
    
    # Prepare response
    response_data = {
        'serverIP': server_ip,
        'serverName': server_name,
        'cluster': cluster_info,
        'headers': headers,
        'request': {
            'method': request.method,
            'url': str(request.url),
            'path': request.url.path,
            'query_string': request.url.query,
            'args': dict(request.query_params),
            'remote_addr': request.client.host if request.client else None,
            'scheme': request.url.scheme,
            'host': request.url.hostname
        },
        'payload': body
    }
    
    return response_data

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
