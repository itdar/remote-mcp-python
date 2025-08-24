import json
import httpx
from typing import Any, Dict
from ..dto.api_response import ApiResponse

def register_another_tools(mcp):
    @mcp.tool()
    async def fetch_api_data(url: str) -> Dict[str, Any]:
        """Fetch data from external API and parse JSON response body"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)

                if response.status_code == 200:
                    data = response.json()

                    # Extract body if exists, otherwise return full response
                    if isinstance(data, dict) and 'body' in data:
                        body_data = data['body']
                        if isinstance(body_data, str):
                            # If body is string, try to parse as JSON
                            try:
                                parsed_body = json.loads(body_data)
                                return ApiResponse(
                                    status="success",
                                    data=parsed_body,
                                    example="Parsed JSON from body field"
                                ).to_dict()
                            except json.JSONDecodeError:
                                return ApiResponse(
                                    status="success",
                                    data=body_data,
                                    example="Raw body content (not JSON)"
                                ).to_dict()
                        else:
                            return ApiResponse(
                                status="success",
                                data=body_data,
                                example="Direct body object"
                            ).to_dict()
                    else:
                        return ApiResponse(
                            status="success",
                            data=data,
                            example="Full API response"
                        ).to_dict()
                else:
                    return ApiResponse(
                        status="error",
                        error=f"HTTP {response.status_code}",
                        example="API request failed"
                    ).to_dict()
        except Exception as e:
            return ApiResponse(
                status="error",
                error=str(e),
                example="Exception occurred during API call"
            ).to_dict()
