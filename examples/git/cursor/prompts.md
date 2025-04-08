# Example Git Prompts for Cursor IDE

This file contains example prompts you can use with the AI assistant in Cursor when the MCP Git server is configured.

## Repository Management

### Initialize a Repository for the Current Project

```
Initialize a Git repository for this project we're working on. Create a README.md with a brief description of what we're building.
```

### Analyze Repository Status

```
Analyze the current Git status of this repository. What files are modified, added, or untracked?
```

### Stage and Commit Changes

```
Stage all the changes I made to the React components and commit them with a descriptive message about the UI improvements.
```

## Integration with Coding Workflow

### Code Review and Commit

```
Review the changes I made to the authentication system, suggest any improvements, and then help me commit them with a good commit message.
```

### Create a Feature Branch

```
Create a new branch called "feature/user-settings" for implementing the user settings page we discussed.
```

### See Differences

```
Show me what changed in the database models since my last commit.
```

## Multi-Repository Management

### Coordinate Changes Across Repositories

```
I need to make parallel changes to both our API repository and our frontend repository. Help me coordinate these changes for the new notification feature.
```

### Check Status Across Projects

```
I'm working on multiple projects. Can you check the Git status of both my "backend" and "frontend" repositories?
```

## Development Patterns

### Implement Git Flow

```
Help me implement the Git Flow workflow for this repository. Create develop and release branches from main.
```

### Prepare for Release

```
I'm preparing for a release. Help me create a release branch, update the version numbers in package.json, and commit these changes.
```

## Troubleshooting

### Resolve Merge Conflicts

```
I have merge conflicts in these files. Help me understand what's conflicting and resolve them.
```

### Fix Git Issues

```
I'm getting a "not a valid Git repository" error. How can I diagnose and fix this issue?
```

## Tips for Using MCP Git in Cursor

1. You can refer to the current project's repository implicitly since Cursor knows your current workspace.

2. For operations across multiple repositories, specify the paths clearly.

3. Combine Git operations with coding assistance to streamline your workflow.

4. Use the Git tools to review changes before committing them.

5. Let the AI explain Git operations as it performs them if you're learning Git. 