# Git MCP Server

This directory is reserved for a custom Git MCP server implementation. Currently, we're using the pre-built `mcp-server-git` package which provides a comprehensive set of Git tools.

## Current Implementation

We're using the official `mcp-server-git` package which provides:

- Git status checking
- Viewing diffs (staged and unstaged)
- Committing changes
- Viewing commit history
- Branch management
- And more

## Creating a Custom Implementation

If you need to extend or customize the Git MCP server, you can create a custom implementation here using the MCP Python SDK. For example:

```python
from mcp.server.fastmcp import FastMCP

# Create a FastMCP server instance
mcp = FastMCP("Custom Git MCP Server")

@mcp.tool()
def custom_git_tool(repo_path: str, custom_parameter: str) -> str:
    """Custom Git tool with additional functionality"""
    # Implement custom Git operations here
    return f"Custom Git operation on {repo_path} with {custom_parameter}"

if __name__ == "__main__":
    mcp.run()
```

## Deployment

The deployment configuration for this server is in the `deployments/git` directory. 