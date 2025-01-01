# git_commands.py

# Basic Commands
print("""
git init                 # Initialize a new Git repository
git clone [url]          # Clone a repository into a new directory
git add [file]           # Add file(s) to the staging area
git status               # Show the status of the working directory and staging area
git commit -m "message"  # Commit changes with a message
git log                  # Show commit logs
git diff                 # Show changes between commits, commit and working tree, etc.
git show [commit]        # Show changes in a specific commit
""")

# Branching and Merging
print("""
git branch               # List all branches in the repository
git branch [name]        # Create a new branch
git checkout [branch]    # Switch to a specific branch
git checkout -b [name]   # Create and switch to a new branch
git merge [branch]       # Merge a branch into the current branch
git rebase [branch]      # Reapply commits on top of another branch
""")

# Remote Repositories
print("""
git remote -v            # Show remote repository URLs
git remote add [name] [url]  # Add a new remote repository
git fetch [remote]       # Download objects and refs from a remote repository
git pull                 # Fetch and merge changes from a remote repository
git push [remote] [branch]  # Push changes to a remote repository
""")

# Undoing Changes
print("""
git reset [file]         # Unstage a file without changing the working directory
git reset --soft [commit]  # Reset to a commit without discarding changes
git reset --hard [commit]  # Reset to a commit and discard all changes
git revert [commit]      # Create a new commit that undoes changes from a specific commit
""")

# Stashing
print("""
git stash                # Save changes for later and clean the working directory
git stash list           # List all stashes
git stash apply          # Reapply the most recent stash
git stash drop           # Remove a stash from the list
""")

# Tagging
print("""
git tag                  # List tags in the repository
git tag [name]           # Create a new tag
git tag -a [name] -m "message"  # Create an annotated tag
git push [remote] [tag]  # Push a tag to a remote repository
""")

# Collaboration
print("""
git pull --rebase        # Rebase instead of merging when pulling changes
git push --force         # Force push changes (use with caution)
git push --tags          # Push all tags to a remote repository
git cherry-pick [commit] # Apply changes from a specific commit
""")

# Configuration and Information
print("""
git config --list        # List all configuration settings
git config [key] [value] # Set a configuration setting
git config --global user.name "name"      # Set global username
git config --global user.email "email"    # Set global email
""")

# Advanced Commands
print("""
git archive [branch]     # Create an archive of files in a branch
git bisect start         # Start a binary search to find a bug
git bisect good [commit] # Mark a commit as good during bisect
git bisect bad [commit]  # Mark a commit as bad during bisect
git blame [file]         # Show who modified each line of a file
git clean -f             # Remove untracked files
git gc                   # Optimize the repository by cleaning unnecessary files
""")
