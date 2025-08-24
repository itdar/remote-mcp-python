
def register_sample_tools(mcp):
    @mcp.tool()
    async def hello(name: str) -> str:
        """Say hello to someone"""
        return f"Hello, {name}!"

