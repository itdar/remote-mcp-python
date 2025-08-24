import sys, os
from fastmcp import FastMCP

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tools.sample import register_sample_tools


def main():
    mcp = FastMCP("Demo")

    register_sample_tools(mcp)

    mcp.run(host="0.0.0.0",
            port=8080,
            transport="streamable-http"
    )


if __name__ == "__main__":
    main()
