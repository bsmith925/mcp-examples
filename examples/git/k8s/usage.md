# MCP Git Server on Kubernetes - Usage Guide

This document explains how to deploy and use the MCP Git server on a Kubernetes cluster.

## Deployment

### Prerequisites

- A running Kubernetes cluster
- kubectl configured to use your cluster
- An Ingress controller (such as NGINX Ingress)
- Storage provisioner for PersistentVolumeClaims

### Deployment Steps

1. Build the MCP Git server Docker image:

```bash
# From the project root
cd deployments/git
docker build -t mcp-git:latest .
```

2. Apply the Kubernetes manifests:

```bash
kubectl apply -f examples/git/k8s/mcp-git.yaml
```

3. Check the deployment status:

```bash
kubectl get all -n mcp-servers
```

4. Set up local DNS resolution for testing:

```bash
# Add to /etc/hosts
echo "127.0.0.1 mcp-git.local" | sudo tee -a /etc/hosts
```

## Repository Management

The MCP Git server deployed on Kubernetes stores Git repositories in a persistent volume mounted at `/repos` inside the container. 

### Creating Repositories

When using the MCP Git server, you'll need to initialize repositories in this volume:

```
git_init(repo_path="/repos/project-name")
```

### Working with Multiple Repositories

You can create and manage multiple repositories in the `/repos` directory:

```
git_init(repo_path="/repos/project1")
git_init(repo_path="/repos/project2")
```

Each operation requires specifying which repository to use:

```
git_status(repo_path="/repos/project1")
```

## Accessing the Server

### From Claude Desktop

Add this to your Claude Desktop configuration:

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

### From Cursor (Hypothetical)

Add this to your Cursor configuration:

```json
{
  "experimental": {
    "mcp": {
      "servers": {
        "git": {
          "url": "http://mcp-git.local",
          "protocol": "sse"
        }
      }
    }
  }
}
```

## Example Interactions

Here are some example requests you can make to your AI assistant:

### Initialize a Repository

```
Create a new Git repository called "backend-api" on the MCP Git server. Add a README.md file and make an initial commit.
```

### Check Status

```
What's the status of the "frontend" repository on the MCP Git server?
```

### Create a Branch and Commit Changes

```
On the MCP Git server, create a new branch called "feature/auth" in the "backend-api" repository. Then create a file called auth.py with a basic authentication function.
```

## Troubleshooting

### Pod Not Starting

If the pod doesn't start, check the logs:

```bash
kubectl logs -n mcp-servers deployment/mcp-git-server
```

### Cannot Access via Hostname

If you can't access the server via the hostname:

1. Verify ingress is properly configured:
   ```bash
   kubectl get ingress -n mcp-servers
   ```

2. Check that your DNS or hosts file is configured correctly:
   ```bash
   ping mcp-git.local
   ```

### Repository Not Found

If you get "not a valid Git repository" errors, ensure you've initialized the repository:

```
git_init(repo_path="/repos/your-project")
```

## Production Considerations

For production use, consider:

1. **Authentication**: Add authentication to protect your repositories
2. **HTTPS**: Configure TLS for secure communication
3. **Backup**: Set up regular backups of the persistent volume
4. **Multi-user support**: Consider one repository volume per user
5. **Resource limits**: Set appropriate CPU and memory limits 