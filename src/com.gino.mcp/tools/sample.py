from fastmcp import FastMCP

mcp = FastMCP("test")

@mcp.tool()
async def hello(name: str) -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"