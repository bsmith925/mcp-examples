# Example Git Commands for Claude Desktop

This file contains example prompts you can use with Claude Desktop when the MCP Git server is configured.

## Basic Git Operations

### Initialize a New Repository

```
Please initialize a new Git repository in the directory ~/projects/new-project.
```

### Check Repository Status

```
What's the current status of my Git repository at ~/projects/my-project?
```

### Stage and Commit Changes

```
Please stage all my changes in the repository at ~/projects/my-project and commit them with the message "Update documentation and fix sidebar layout".
```

### View Commit History

```
Show me the last 5 commits in my Git repository at ~/projects/my-project.
```

## Branch Operations

### Create a New Branch

```
Create a new branch called "feature/user-auth" in my Git repository at ~/projects/my-project.
```

### Switch to a Branch

```
Switch to the branch "develop" in my Git repository at ~/projects/my-project.
```

### View Differences

```
Show me the differences between my current branch and main in the repository at ~/projects/my-project.
```

## Working with Multiple Repositories

### Compare Status Across Repositories

```
Compare the status of my repositories at ~/projects/frontend and ~/projects/backend.
```

### Create Branches in Multiple Repositories

```
Create a branch called "release/v1.2.0" in both my repositories at ~/projects/api and ~/projects/client.
```

## Advanced Operations

### Show a Specific Commit

```
Show me the details of commit ba3c1d4 in my repository at ~/projects/my-project.
```

### Initialize and Set Up a New Project

```
Help me set up a new Git repository for a React project at ~/projects/new-react-app. Initialize the repository, create a README.md file, and make the first commit.
```

### Analyze and Explain Changes

```
Analyze the current uncommitted changes in my repository at ~/projects/my-project and explain what's been modified.
```

## Tips for Using MCP Git Server with Claude

1. **Always specify the repository path** in your requests.
   
2. **Initialize repositories before using them** if they don't exist already.
   
3. **Use relative paths** from your home directory (~/projects/...) for better readability.
   
4. **Be specific about branch names** when working with branches.
   
5. **Combine multiple Git operations** in a single request for complex tasks. 