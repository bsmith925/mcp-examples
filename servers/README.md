# MCP Servers

This directory is for custom MCP server implementations. Currently, we're using pre-built MCP servers from packages, but if we need to develop custom implementations, they will go here.

## Directory Structure

- `git/` - Reserved for a custom Git MCP server implementation (currently using the mcp-server-git package)
- Add additional directories for other custom MCP server implementations

## Creating a Custom MCP Server

To create a custom MCP server:

1. Create a new directory for your server type
2. Implement using the MCP SDK
3. Add appropriate documentation
4. Update the deployment configuration in the corresponding deployment directory

Example of a basic custom server using the MCP Python SDK:

```python
from mcp.server.fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP("Custom MCP Server")

@mcp.resource("custom://{name}")
def custom_resource(name: str) -> str:
    """Example custom resource"""
    return f"Custom resource: {name}"

@mcp.tool()
def custom_tool(parameter: str) -> str:
    """Example custom tool"""
    return f"Tool executed with parameter: {parameter}"

if __name__ == "__main__":
    mcp.run()
``` 