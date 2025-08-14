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
