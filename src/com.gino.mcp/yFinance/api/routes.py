from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse

from ..handlers.default import (
    handle_initialize,
    handle_ping,
    handle_notification,
    create_error_response
)

app = FastAPI()


@app.post("/")
async def handle_mcp_request(request: Request):
    try:
        data = await request.json()

        method = data.get('method')
        params = data.get('params', {})
        request_id = data.get('id')

        # Route MCP methods to appropriate handlers
        if method == 'initialize':
            response = await handle_initialize(params, request_id)
            return JSONResponse(content=response)
        elif method == 'ping':
            response = await handle_ping(params, request_id)
            return JSONResponse(content=response)
        elif method.startswith('notifications/'):
            return await handle_notification(method)
        else:
            raise HTTPException(404, f"Method not found: {method}")

    except HTTPException:
        raise
    except Exception as e:
        error_response = create_error_response(
            -32603,
            f"Internal error: {e}",
            data.get('id') if 'data' in locals() else None
        )
        return JSONResponse(content=error_response, status_code=500)


@app.get("/favicon.ico")
async def favicon():
    return {}


@app.get("/health")
async def favicon():
    return "OK"
