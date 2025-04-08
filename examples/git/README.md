# MCP Git Server Examples

This directory contains examples of using the MCP Git server in different configurations.

## Directory Structure

```
├── local/               # Examples of using the MCP Git server locally
│   ├── basic.py         # Basic usage with a single repository
│   └── multi_repo.py    # Working with multiple repositories
│
├── cursor/              # Example Cursor IDE integration (hypothetical)
│   ├── config.json      # Example Cursor configuration
│   └── prompts.md       # Example prompts to use with Cursor
│
├── claude/              # Claude Desktop integration examples
│   ├── config.json      # Claude Desktop configuration
│   └── commands.md      # Example commands to use with Claude
│
└── k8s/                 # Kubernetes deployment examples
    ├── mcp-git.yaml     # Simple combined K8s manifest
    └── usage.md         # Usage examples with K8s deployment
```

## Using These Examples

The examples demonstrate various ways to interact with the MCP Git server:

1. **Local Development**: Running the server directly on your machine
2. **Claude Desktop**: Configuring Claude Desktop to use the MCP Git server
3. **Cursor IDE**: Hypothetical integration with Cursor (if supported in the future)
4. **Kubernetes**: Deploying and using the server in a Kubernetes cluster

Each directory contains both configuration files and usage examples.

## Key Concepts Demonstrated

1. **Repository Handling**:
   - Working with multiple repositories
   - Creating new repositories with `git_init`
   - Specifying repository paths in operations

2. **MCP Tool Usage**:
   - Basic Git operations (status, add, commit)
   - Branch operations (create, checkout)
   - Viewing diffs and history

3. **Configuration**:
   - Different ways to configure clients
   - Environment setup for different scenarios

## Getting Started

Begin by exploring the local examples, which show basic Python scripts that interact with the MCP Git server:

```bash
python examples/git/local/basic.py
```

Then check out the configuration examples for Claude Desktop to set up your AI assistant with Git capabilities. 