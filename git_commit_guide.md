# Git Manual Commit Process - Step by Step Guide

## Step 1: Check Current Status

See what files have been modified, added, or are untracked.

```bash
git status
```

**What you'll see:**
- `modified:` — files you changed
- `untracked:` — new files git doesn't know about yet
- `staged:` — files ready to be committed

---

## Step 2: Review Changes (Optional but Recommended)

See exactly what changed in your files before committing.

```bash
# See all changes
git diff

# See changes in a specific file
git diff filename.py

# See changes in staged files only
git diff --staged
```

---

## Step 3: Stage Files for Commit

Choose which files you want to include in the commit.

```bash
# Stage a single file
git add filename.py

# Stage multiple specific files
git add file1.py file2.py file3.py

# Stage all files in current directory
git add .

# Stage all Python files
git add *.py

# Stage a specific folder
git add folder_name/

# Unstage a file (if you added by mistake)
git reset filename.py
```

---

## Step 4: Verify Staged Files

Confirm the right files are staged before committing.

```bash
git status
```

Staged files appear under **"Changes to be committed"** in green.

---

## Step 5: Create the Commit

Commit with a meaningful message describing what you did.

```bash
git commit -m "your commit message here"
```

**Commit Message Examples:**

```bash
# Practice work
git commit -m "practicing numpy array operations"

# Bug fix
git commit -m "fixing missing value handling in data cleaning"

# New feature/assignment
git commit -m "adding sql joins assignment"

# Revision
git commit -m "revising linear regression model"

# Multiple files together
git commit -m "adding seaborn plots and matplotlib practice"
```

---

## Step 6: Verify the Commit

Check that the commit was created successfully.

```bash
# See recent commits
git log --oneline

# See detailed last commit
git log -1

# See last commit with changes
git log -1 -p
```

---

## Step 7: Push to Remote (GitHub)

Send your commits to the remote repository.

```bash
# Push to current branch
git push

# Push and set upstream (first time for new branch)
git push -u origin branch-name

# Push to main/master
git push origin master
```

---

## Common Scenarios

### Scenario 1: Modified an existing file
```bash
git status                          # see what changed
git add filename.py                 # stage it
git commit -m "updated decision tree notebook"  # commit
git push                            # push
```

### Scenario 2: Created new files
```bash
git status                          # see untracked files
git add new_file.py                 # stage new file
git commit -m "adding knn practice" # commit
git push                            # push
```

### Scenario 3: Multiple related files
```bash
git status
git add 20_ml/3_KNN_algorithm.ipynb 20_ml/3_ex.md
git commit -m "adding knn algorithm and gini index notes"
git push
```

### Scenario 4: Want to commit everything
```bash
git status
git add .
git commit -m "adding all practice work for ml module"
git push
```

### Scenario 5: Made a mistake in commit message
```bash
# Fix the last commit message (before pushing)
git commit --amend -m "corrected commit message"
```

### Scenario 6: Forgot to add a file to the last commit
```bash
git add forgotten_file.py
git commit --amend --no-edit
```

---

## Quick Reference Commands

| Action | Command |
|---|---|
| Check status | `git status` |
| See changes | `git diff` |
| Stage file | `git add filename` |
| Stage all | `git add .` |
| Unstage file | `git reset filename` |
| Commit | `git commit -m "message"` |
| Push | `git push` |
| View log | `git log --oneline` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Undo last commit (lose changes) | `git reset --hard HEAD~1` |

---

## Typical Workflow Summary

```
git status          →  1. See what changed
git add .           →  2. Stage files
git status          →  3. Verify staging
git commit -m "msg" →  4. Commit
git push            →  5. Push to GitHub
```
