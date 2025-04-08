#!/bin/bash
set -e

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Building Docker image for MCP Git server..."
docker build -t mcp-git:latest .

echo "Deploying to Kubernetes..."
kubectl apply -f k8s-deployment.yaml
kubectl apply -f k8s-ingress.yaml

echo "Waiting for deployment to be ready..."
kubectl rollout status deployment/mcp-git-server

# Get the pod name
POD_NAME=$(kubectl get pods -l app=mcp-git-server -o jsonpath="{.items[0].metadata.name}")
echo "MCP Git server deployed in pod: $POD_NAME"

echo
echo "NOTE: MCP servers in Kubernetes require a different configuration approach."
echo "Based on the official documentation, MCP servers typically use Unix sockets for communication."
echo
echo "There are two recommended approaches for using this server:"
echo
echo "1. Local development - use the mcp-server-git package directly:"
echo "   - Install locally: pip install mcp-server-git"
echo "   - Configure Claude Desktop:"
echo '{
  "mcpServers": {
    "git": {
      "command": "python",
      "args": ["-m", "mcp_server_git", "--repository", "/path/to/git/repo"]
    }
  }
}'
echo
echo "2. For team-wide usage, consider deploying as a shared service with proper authentication"
echo "   and use the appropriate client configuration for your specific deployment strategy."
echo
echo "See the README.md for more information on configuration options."
echo "For a comprehensive architecture overview, see ../architecture.md" 