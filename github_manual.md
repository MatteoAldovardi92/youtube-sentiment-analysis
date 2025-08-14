# GitHub Usage Manual

This guide provides a quick reference for using Git and GitHub, with a focus on the common issues encountered during the setup of this project.

## 1. Configuring Your Git Identity

Before you start working on a project, it's important to tell Git who you are. This information will be attached to all your commits.

**Set your username and email:**
```bash
git config --global user.name "YourGitHubUsername"
git config --global user.email "your.email@example.com"
```
*   **Why?** This ensures your commits are correctly attributed to your GitHub account.
*   **Note:** The `--global` flag sets this information for all your Git projects on your computer.

## 2. Starting a New Project

To start tracking a project with Git, you need to initialize a repository.

**Initialize a repository:**
```bash
git init
```
*   **What it does:** This command creates a hidden `.git` directory in your project folder, where Git stores all the project history and configuration.

## 3. Ignoring Files with `.gitignore`

You don't want to save every file to your repository. The `.gitignore` file tells Git which files and folders to ignore.

**Example `.gitignore` for a Python project:**
```
# Virtual Environment
venv/

# Python cache
__pycache__/
*.pyc

# IDE files
.idea/
.vscode/
```
*   **Why?** This keeps your repository clean and avoids tracking large, unnecessary files like virtual environments or system-specific files.

## 4. Saving Your Work: Staging and Committing

Saving changes in Git is a two-step process: staging and committing.

**1. Stage your changes:**
```bash
git add .
```
*   **What it does:** This command adds all the new or modified files to the "staging area". The staging area is a list of changes you want to include in your next commit. You can also add specific files instead of all of them (e.g., `git add filename.py`).

**2. Commit your changes:**
```bash
git commit -m "A descriptive message about your changes"
```
*   **What it does:** This command saves the staged changes to your project's history. The `-m` flag allows you to provide a commit message directly from the command line.

## 5. Connecting to GitHub

To push your code to GitHub, you need to connect your local repository to a remote repository on GitHub.

**Add a remote repository:**
```bash
git remote add origin https://github.com/YourGitHubUsername/your-repository-name.git
```
*   **Important:** This command must be on a **single line**. Be careful when copying and pasting to avoid adding extra spaces or newlines.
*   `origin` is the default name for the remote repository.

## 6. Pushing Your Code to GitHub

Once your local repository is connected to the remote, you can push your commits.

**Push your code:**
```bash
git push -u origin main
```
*   **What it does:** This command uploads your commits to the `main` branch of the `origin` remote repository on GitHub.
*   The `-u` flag sets the upstream branch, so in the future, you can just run `git push`.

## 7. Troubleshooting Remotes

Sometimes, you might make a mistake when adding a remote.

**Check your remotes:**
```bash
git remote -v
```
*   **What it does:** This command lists all the remote repositories you have configured.

**Fixing a wrong remote:**
If you added a remote with the wrong URL, you can remove it and add it again correctly.
```bash
# 1. Remove the incorrect remote
git remote remove origin

# 2. Add the remote again with the correct URL
git remote add origin https://github.com/YourGitHubUsername/your-repository-name.git
```

## 8. Opening Your Project in Google Colab

Once your project is on GitHub, you can easily open it in Google Colab.

1.  Go to [https://colab.research.google.com/](https://colab.research.google.com/).
2.  Click on `File` > `Open notebook`.
3.  Select the `GitHub` tab.
4.  Enter your GitHub repository URL and press Enter.
5.  Click on the notebook file (`.ipynb` or `.py`) you want to open.

## 9. Troubleshooting Push Issues (403 Forbidden)

Encountering a `403 Forbidden` error when pushing to GitHub often indicates an authentication problem. This usually happens when Git tries to use outdated or incorrect credentials.

### Common Causes and Solutions:

1.  **Cached Old Credentials (macOS Keychain):**
    If you've recently changed your GitHub username or password/PAT, your system might be trying to use old, cached credentials.

    **Solution:** Clear the cached credentials from your macOS Keychain.
    *   Open `Keychain Access.app` (Applications > Utilities).
    *   Search for `github.com`.
    *   Delete any entries related to `github.com` (typically of kind "Internet Password").
    *   Try pushing again. Git will then prompt you for new credentials.

2.  **Incorrect or Expired Personal Access Token (PAT):**
    GitHub now primarily uses Personal Access Tokens (PATs) for command-line authentication instead of your account password. A `403` error can occur if your PAT is incorrect, has expired, or lacks the necessary permissions.

    **Solution:**
    *   **Verify your PAT:**
        *   Ensure you copied the PAT correctly (no extra spaces or typos).
        *   Check its expiration date on GitHub ([https://github.com/settings/tokens](https://github.com/settings/tokens)).
        *   Verify its permissions (scopes). For pushing, it needs at least the `repo` scope (for classic tokens) or `contents:write` (for fine-grained tokens).
    *   **Generate a new PAT:** If in doubt, generate a brand new PAT on GitHub ([https://github.com/settings/tokens/new](https://github.com/settings/tokens/new)) with the correct scopes and try again.

3.  **"Password" Prompt vs. PAT:**
    When Git prompts for a "Password," it's expecting your **Personal Access Token (PAT)**, not your actual GitHub account password.

    **Solution:** When you see the "Password" prompt, paste your PAT there.

By addressing these points, you should be able to resolve most `403 Forbidden` errors during Git pushes.