FROM python:3.11-slim

WORKDIR /app

# Install git and other dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install mcp-server-git
RUN pip install --no-cache-dir mcp-server-git

# Create repositories directory
RUN mkdir -p /repos

# Create volume mount point for git repositories
VOLUME /repos

# Run the MCP Git server without forcing a specific repository
# This allows the server to:
# 1. Discover repositories through the roots capability
# 2. Accept repository paths in tool calls
# 3. Use /repos as a location for creating repos if needed
ENTRYPOINT ["python", "-m", "mcp_server_git"] 