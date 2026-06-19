# What is Git?
   Git is a tool that remembers every changes made to a project.
# What is GitHub?
    GitHub is a platform where developers can share,manage,track and collaborate on software projects using git.
# Meaning of:
   git status:
        show the current state of your project in Git
   git add:
        changes  from working directory to the GIT staging area.
   git commit:
       is a snapshot of your project's staged changes saved permanently to your local repository history.
   git push:
       sends or upload your changes to Github
   git pull:
        upadate your local changes from Github 
# Branching
   Branching in Git allows you to create an independent line of development without affecting the main project.
   Key concepts:
     main → default production branch
     Feature branch → used for isolated changes
Merge → combining changes back into main
# Remote Tracking
   Remote tracking refers to linking your local repository with a remote repository (e.g., GitHub).
   Key concepts:
     origin → default name for remote repo
     main → remote branch
     upstream tracking → connects local branch to remote branch
# Errors faced
Error 1: Empty repository warning
     Message: “You might have cloned an empty repository”
     Cause: GitHub repo had no commits yet
     Fix: Created initial commit and pushed
Error 2: Missing remote reference
     Message: fatal: couldn't find remote ref master
     Cause: Branch mismatch (master vs main)
     Fix: Switched branch to main
     git branch -M main
Error 3: Rejected push (non-fast-forward)
     Message: failed to push some refs
     Cause: Local repo behind remote
     Fix: Used pull before push
     git pull origin main
     git push
Error 4: Incorrect file creation structure
     Issue: Multiple filenames merged into one broken file
     Cause: Wrong echo command usage in Windows CMD
     Fix: Recreated files individually
     echo. > file.md
