from fastmcp import FastMCP
from tools.sample import register_sample_tools

def main():
    mcp = FastMCP("Demo")

    register_sample_tools(mcp)

    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()
