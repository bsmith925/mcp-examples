# MCP Git Server on Kubernetes

This project deploys the MCP Git server to a Kubernetes cluster.

## Important Note on MCP Server Architecture

After investigation, we've learned that the Model Context Protocol typically uses Unix sockets for direct communication between clients and servers, not HTTP/SSE as initially thought. This presents some challenges for running MCP servers in Kubernetes.

## Repository Handling

The MCP Git server has a flexible approach to handling Git repositories:

1. **Dynamic Repository Discovery**:
   - The server can use the client's "roots" capability to find Git repositories in the client's workspace
   - This allows the AI assistant to work with the repository the user currently has open

2. **Per-operation Repository Path**:
   - Each Git operation accepts a `repo_path` parameter
   - This allows working with any repository, regardless of how the server was started
   - Example: `git_status(repo_path="/path/to/specific/repo")`

3. **Command-line Repository**:
   - When starting the server, you can specify a default repository: `--repository /path/to/repo`
   - This provides a fallback if no repository is specified in a tool call

Our Kubernetes deployment creates a `/repos` directory but doesn't force a specific repository. The AI assistant will need to initialize repositories as needed or specify paths to existing repositories.

## Deployment Options

There are two main approaches for using MCP servers:

### Option 1: Local Development (Recommended)

For local development and personal use, install the MCP Git server directly:

```bash
pip install mcp-server-git
```

Then configure Claude Desktop to use it:

```json
{
  "mcpServers": {
    "git": {
      "command": "python",
      "args": ["-m", "mcp_server_git"]
    }
  }
}
```

You can optionally specify a default repository:

```json
{
  "mcpServers": {
    "git": {
      "command": "python",
      "args": ["-m", "mcp_server_git", "--repository", "/path/to/git/repo"]
    }
  }
}
```

### Option 2: Team Access via Custom Integration

For team-wide access, you'll need to:

1. Set up a proxy or RPC-style service that can communicate with the MCP server
2. Expose this service via HTTP/REST APIs with proper authentication
3. Create a custom MCP client that bridges between the HTTP API and the standard MCP client interface

Our Kubernetes deployment can serve as a starting point for this approach, but additional development would be needed.

## Hypothetical Cursor Integration

If Cursor were to support hosted MCP servers in the future, the configuration might look something like this:

```json
{
  "mcp": {
    "servers": {
      "git": {
        "url": "https://mcp-git.company.com",
        "authToken": "your-auth-token",
        "protocol": "sse"
      }
    }
  }
}
```

This would enable Cursor users to:

- Access centralized Git functionality from their editor
- Work with repositories without local Git installation
- Benefit from shared automation and standardized Git operations
- Use advanced Git features through the AI assistant

The MCP Git server would need a custom adapter to expose its functionality via HTTP/SSE, which is not currently part of the standard implementation.

## Kubernetes Deployment (Experimental)

The deployment in this directory is experimental and may require additional customization:

1. Make the deploy script executable:
   ```
   chmod +x deploy.sh
   ```

2. Run the deployment script:
   ```
   ./deploy.sh
   ```

This will:
- Build the Docker image
- Deploy to Kubernetes
- Show deployment information

## Docker Image

The Docker image includes:
- Python 3.11
- Git
- mcp-server-git package

The container is configured to:
- Mount a persistent volume at `/repos` for Git repositories
- Run the MCP Git server without forcing a specific repository
- Allow dynamic repository discovery and initialization through tool calls

## Using Git Tools

The MCP Git server provides several tools that can be called by the AI assistant:

1. `git_status`: Shows the working tree status
2. `git_diff_unstaged`: Shows changes in the working directory not yet staged
3. `git_diff_staged`: Shows changes that are staged for commit
4. `git_diff`: Shows differences between branches or commits
5. `git_commit`: Records changes to the repository
6. `git_add`: Adds file contents to the staging area
7. `git_reset`: Unstages all staged changes
8. `git_log`: Shows the commit logs
9. `git_create_branch`: Creates a new branch from an optional base branch
10. `git_checkout`: Switches branches
11. `git_show`: Shows the contents of a commit
12. `git_init`: Initializes a new Git repository

Each tool requires a `repo_path` parameter specifying which repository to operate on. For example:

```
git_init(repo_path="/repos/new-project")
git_status(repo_path="/repos/new-project")
```

## Next Steps

For effective team-wide access to MCP servers, consider:

1. Developing a custom HTTP API service that interfaces with the MCP server
2. Setting up proper authentication and authorization
3. Implementing client-side integration to bridge HTTP and MCP protocols
4. Exploring alternative deployment models like sidecar containers

## References

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP Git Server Repository](https://github.com/modelcontextprotocol/servers/tree/main/src/git)

## Prerequisites

- Docker
- Kubernetes cluster (local like Minikube, Docker Desktop, or k3s)
- kubectl configured to use your cluster
- Ingress controller installed (like NGINX Ingress)

## Checking the Deployment

Check that the pods are running:
```
kubectl get pods -l app=mcp-git-server
```

Check the service:
```
kubectl get svc mcp-git-service
```

Check the ingress:
```
kubectl get ingress mcp-git-ingress
```

## Troubleshooting

### Repository Issues

If you see `ERROR:mcp_server_git.server:/repos is not a valid Git repository`, you need to:

1. Use the `git_init` tool to create a repository first:
   ```
   git_init(repo_path="/repos/my-project")
   ```

2. Then specify this path in subsequent operations:
   ```
   git_status(repo_path="/repos/my-project")
   ```

The server doesn't assume a default repository but instead requires each operation to specify which repository to use.

## Client Configuration

### For Claude Desktop

Add this to your `claude_desktop_config.json` (typically in `~/.config/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "git": {
      "serverUrl": "http://mcp-git.local",
      "protocol": "sse"
    }
  }
}
```

### For Zed

Add to your Zed settings.json:

```json
"context_servers": {
  "mcp-server-git": {
    "url": "http://mcp-git.local"
  }
},
```

## Using the Server

Once configured, your AI assistant can access the Git server's capabilities:

1. Show repository status: `git_status`
2. View changes: `git_diff_unstaged` or `git_diff_staged`
3. Commit changes: `git_commit`
4. View commit history: `git_log`
5. And more...

## Troubleshooting

If you can't connect to the server:

1. Check that pods are running: `kubectl get pods`
2. Check ingress is configured: `kubectl get ingress`
3. Verify host entry: `cat /etc/hosts | grep mcp-git.local`
4. Test connectivity: `curl http://mcp-git.local` 