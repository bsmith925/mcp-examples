#!/usr/bin/env python3
"""
Basic example of using the MCP Git server locally with a single repository.
"""
import asyncio
import os
import tempfile
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_example():
    """
    Run the basic Git repository example
    """
    print("MCP Git Server - Basic Example")
    print("==============================")
    
    # Create a temporary directory for our example repository
    with tempfile.TemporaryDirectory() as temp_dir:
        repo_path = Path(temp_dir) / "example-repo"
        repo_path.mkdir(exist_ok=True)
        
        print(f"Using repository path: {repo_path}")
        
        # Start the MCP Git server
        server_params = StdioServerParameters(
            command="python",
            args=["-m", "mcp_server_git"],
        )
        
        print("\nStarting MCP Git server...")
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize the connection
                await session.initialize()
                print("Connection initialized")
                
                # List available tools
                tools = await session.list_tools()
                print(f"\nAvailable tools: {[tool.name for tool in tools]}")
                
                # Initialize a Git repository
                print("\nInitializing Git repository...")
                result = await session.call_tool(
                    "git_init", 
                    arguments={"repo_path": str(repo_path)}
                )
                print(f"Result: {result[0].text}")
                
                # Create a sample file
                sample_file = repo_path / "README.md"
                with open(sample_file, "w") as f:
                    f.write("# Example Repository\n\nThis is a test repository for the MCP Git server example.")
                
                # Check status (should show untracked file)
                print("\nChecking repository status...")
                result = await session.call_tool(
                    "git_status", 
                    arguments={"repo_path": str(repo_path)}
                )
                print(f"Status:\n{result[0].text}")
                
                # Add the file
                print("\nAdding file to staging area...")
                result = await session.call_tool(
                    "git_add", 
                    arguments={"repo_path": str(repo_path), "files": ["README.md"]}
                )
                print(f"Result: {result[0].text}")
                
                # Check status again (should show staged file)
                print("\nChecking status after add...")
                result = await session.call_tool(
                    "git_status", 
                    arguments={"repo_path": str(repo_path)}
                )
                print(f"Status:\n{result[0].text}")
                
                # Commit the change
                print("\nCommitting changes...")
                result = await session.call_tool(
                    "git_commit", 
                    arguments={
                        "repo_path": str(repo_path), 
                        "message": "Initial commit"
                    }
                )
                print(f"Result: {result[0].text}")
                
                # Check log
                print("\nViewing commit history...")
                result = await session.call_tool(
                    "git_log", 
                    arguments={"repo_path": str(repo_path)}
                )
                print(f"Commit log:\n{result[0].text}")
                
                # Create a branch
                print("\nCreating a new branch...")
                result = await session.call_tool(
                    "git_create_branch", 
                    arguments={
                        "repo_path": str(repo_path), 
                        "branch_name": "feature-branch"
                    }
                )
                print(f"Result: {result[0].text}")
                
                # Checkout the branch
                print("\nSwitching to the new branch...")
                result = await session.call_tool(
                    "git_checkout", 
                    arguments={
                        "repo_path": str(repo_path), 
                        "branch_name": "feature-branch"
                    }
                )
                print(f"Result: {result[0].text}")
                
                print("\nExample completed successfully!")
                

if __name__ == "__main__":
    asyncio.run(run_example()) 