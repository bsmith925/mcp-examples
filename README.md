# MCP Servers for Teams

This project explores deployment configurations and custom implementations for Model Context Protocol (MCP) servers for team usage.

## Understanding MCP Architecture

The Model Context Protocol (MCP) is designed for local communication between AI assistants and server tools. After investigation, we've learned:

1. MCP servers typically use Unix sockets or stdio for communication
2. They're primarily designed for local use, not HTTP/REST APIs
3. Team-wide access requires additional integration work
4. MCP servers can work with multiple contexts/resources based on client requests

## Project Structure

```
.
├── deployments/         # Kubernetes deployment configurations (experimental)
│   └── git/             # Git MCP server deployment
│       ├── Dockerfile
│       ├── k8s-deployment.yaml
│       ├── k8s-ingress.yaml
│       ├── deploy.sh
│       └── README.md
│
└── servers/             # Custom MCP server implementations
    ├── git/             # Git MCP server custom implementation (if needed)
    │   └── README.md
    └── README.md
```

## Recommended Approaches

### Local Development (Simple)

For individual use:

1. Install MCP servers directly:
   ```bash
   pip install mcp-server-git
   ```

2. Configure in Claude Desktop:
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

The MCP Git server can work with multiple repositories by:
- Discovering Git repositories in the client's workspace
- Accepting repository paths in tool operations
- Creating new repositories when needed

### Team-Wide Access (Advanced)

For team access, consider:

1. **Custom Integration Service**:
   - Develop a service that interfaces with MCP servers
   - Expose functionality via REST APIs with auth
   - Create client adapters for AI assistants

2. **Container-Per-User**:
   - Deploy MCP servers as containers with user-specific volumes
   - Use authentication to route requests to user containers

3. **Sidecar Pattern**:
   - Run MCP servers as sidecars in user application pods
   - Share Unix sockets within the pod

## Hypothetical Integration with Cursor

While Cursor doesn't currently support hosted MCP servers, if it did in the future, configuration might look like this:

### Via Settings JSON

```json
{
  "mcp": {
    "servers": {
      "git": {
        "url": "https://mcp-git.company.com",
        "authToken": "${MCP_AUTH_TOKEN}",
        "protocol": "sse"
      },
      "database": {
        "url": "https://mcp-db.company.com", 
        "authToken": "${MCP_DB_AUTH_TOKEN}",
        "protocol": "sse"
      }
    }
  }
}
```

### Via Environment Variables

```
CURSOR_MCP_GIT_URL=https://mcp-git.company.com
CURSOR_MCP_GIT_AUTH_TOKEN=your-auth-token
CURSOR_MCP_GIT_PROTOCOL=sse
```

### Benefits for Cursor Users

Team-wide MCP servers would enable:

1. **Consistent Tool Access**: All team members access the same tools with identical configurations
2. **Access Control**: Centralized permissions and authentication
3. **Resource Sharing**: Share computation resources for expensive operations
4. **Custom Tooling**: Team-specific tools that integrate with internal systems
5. **Version Control**: Centralized updates to tools and functionality

## Experimental Kubernetes Deployment

Our Kubernetes deployment is experimental and demonstrates containerizing MCP servers. It may require additional development for practical use:

```bash
cd deployments/git
chmod +x deploy.sh
./deploy.sh
```

## Understanding MCP Git Server Capabilities

The Git MCP server is more flexible than initially thought:

1. **Multi-Repository Support**:
   - Can work with any number of repositories
   - Repositories can be discovered from client workspace
   - Each operation specifies which repository to use

2. **Tool Operations**:
   - All Git operations require a `repo_path` parameter
   - Example: `git_status(repo_path="/path/to/repo")`
   - This allows working with multiple repositories in the same session

3. **Repository Discovery**:
   - Can automatically find Git repositories in client workspace
   - Uses MCP "roots" capability to locate repositories
   - Allows the AI to work with the repository the user has open

## Adding New MCP Servers

To add a new MCP server:

1. Create a new directory in `deployments/` for your server type
2. Copy and modify the Dockerfile, Kubernetes manifests, and deployment script
3. If creating a custom implementation, add it to the `servers/` directory

## Troubleshooting

### Common Issues

#### "Not a valid Git repository" Error

**Problem**: `ERROR:mcp_server_git.server:/repos is not a valid Git repository`

**Solution**: The Git MCP server requires specifying a valid Git repository for each operation. There are two approaches:

1. Use the `git_init` tool to create a repository first:
   ```
   git_init(repo_path="/path/to/new/repo")
   ```

2. Then specify this path in subsequent operations:
   ```
   git_status(repo_path="/path/to/new/repo")
   ```

Unlike our initial implementation, the server doesn't force or assume a default repository. Each operation must explicitly specify which repository to use.

#### Communication Issues

If you're experiencing connectivity problems:

1. Check that the MCP server is running: `kubectl get pods` or `ps aux | grep mcp_server_git`
2. Verify your client configuration points to the correct path or URL
3. Ensure you have appropriate permissions for the repository directory

## Next Steps

We recommend:

1. Exploring custom implementation of MCP servers that can work in a team environment
2. Investigating WebSocket or gRPC protocols for network communication
3. Developing authentication and authorization layers
4. Creating client adapters that can interface with network-accessible MCP servers

## References

- [Model Context Protocol](https://modelcontextprotocol.io)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Git Server](https://github.com/modelcontextprotocol/servers/tree/main/src/git)
