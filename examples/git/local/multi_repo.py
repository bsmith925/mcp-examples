#!/usr/bin/env python3
"""
Example of working with multiple Git repositories using the MCP Git server.
"""
import asyncio
import os
import tempfile
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_example():
    """
    Run the multiple repository example
    """
    print("MCP Git Server - Multiple Repository Example")
    print("===========================================")
    
    # Create temporary directories for our repositories
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create two separate repository paths
        repo1_path = Path(temp_dir) / "project1"
        repo2_path = Path(temp_dir) / "project2"
        repo1_path.mkdir(exist_ok=True)
        repo2_path.mkdir(exist_ok=True)
        
        print(f"Repository 1: {repo1_path}")
        print(f"Repository 2: {repo2_path}")
        
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
                
                # Initialize the first repository
                print("\n--- Repository 1 ---")
                print("Initializing first repository...")
                result = await session.call_tool(
                    "git_init", 
                    arguments={"repo_path": str(repo1_path)}
                )
                print(f"Result: {result[0].text}")
                
                # Create a sample file in repo1
                file1 = repo1_path / "README.md"
                with open(file1, "w") as f:
                    f.write("# Project 1\n\nThis is the first test repository.")
                
                # Add and commit in repo1
                await session.call_tool(
                    "git_add", 
                    arguments={"repo_path": str(repo1_path), "files": ["README.md"]}
                )
                await session.call_tool(
                    "git_commit", 
                    arguments={
                        "repo_path": str(repo1_path), 
                        "message": "Initial commit for Project 1"
                    }
                )
                
                # Initialize the second repository
                print("\n--- Repository 2 ---")
                print("Initializing second repository...")
                result = await session.call_tool(
                    "git_init", 
                    arguments={"repo_path": str(repo2_path)}
                )
                print(f"Result: {result[0].text}")
                
                # Create a sample file in repo2
                file2 = repo2_path / "README.md"
                with open(file2, "w") as f:
                    f.write("# Project 2\n\nThis is the second test repository.")
                
                # Add and commit in repo2
                await session.call_tool(
                    "git_add", 
                    arguments={"repo_path": str(repo2_path), "files": ["README.md"]}
                )
                await session.call_tool(
                    "git_commit", 
                    arguments={
                        "repo_path": str(repo2_path), 
                        "message": "Initial commit for Project 2"
                    }
                )
                
                # Create branches in both repositories
                print("\n--- Creating branches ---")
                
                # Create a branch in repo1
                print("Creating branch in first repository...")
                result = await session.call_tool(
                    "git_create_branch", 
                    arguments={
                        "repo_path": str(repo1_path), 
                        "branch_name": "feature-a"
                    }
                )
                print(f"Result: {result[0].text}")
                
                # Create a branch in repo2
                print("\nCreating branch in second repository...")
                result = await session.call_tool(
                    "git_create_branch", 
                    arguments={
                        "repo_path": str(repo2_path), 
                        "branch_name": "feature-b"
                    }
                )
                print(f"Result: {result[0].text}")
                
                # Check status of both repositories
                print("\n--- Repository Status ---")
                
                print("Status of first repository:")
                result = await session.call_tool(
                    "git_status", 
                    arguments={"repo_path": str(repo1_path)}
                )
                print(f"{result[0].text}")
                
                print("\nStatus of second repository:")
                result = await session.call_tool(
                    "git_status", 
                    arguments={"repo_path": str(repo2_path)}
                )
                print(f"{result[0].text}")
                
                # View logs from both repositories
                print("\n--- Commit Logs ---")
                
                print("Log from first repository:")
                result = await session.call_tool(
                    "git_log", 
                    arguments={"repo_path": str(repo1_path)}
                )
                print(f"{result[0].text}")
                
                print("\nLog from second repository:")
                result = await session.call_tool(
                    "git_log", 
                    arguments={"repo_path": str(repo2_path)}
                )
                print(f"{result[0].text}")
                
                print("\nMultiple repository example completed successfully!")

if __name__ == "__main__":
    asyncio.run(run_example()) 