from fastapi import HTTPException
from fastapi.responses import JSONResponse

async def handle_initialize(params: dict, request_id: str) -> dict:
    result = {
        "protocolVersion": "2025-08-16",
        "capabilities": {
            "tools": {
                "listChanged": True
            }
        },
        "serverInfo": {
            "name": "fastmcp-http-server",
            "version": "1.0.0"
        }
    }
    return {
        "jsonrpc": "2.0",
        "result": result,
        "id": request_id
    }

async def handle_ping(params: dict, request_id: str) -> dict:
    return {
        "jsonrpc": "2.0",
        "result": {},
        "id": request_id
    }

async def handle_notification(method: str) -> JSONResponse:
    return JSONResponse(content=None, status_code=204)

def create_error_response(error_code: int, message: str, request_id: str = None) -> dict:
    return {
        "jsonrpc": "2.0",
        "error": {"code": error_code, "message": message},
        "id": request_id
    }
