# :wave: The Basics of GitHub 

## 🤓 Course overview and learning outcomes 

### Setting Up Your Workspace

### Creating a Branch for Your Work

1. **Open your Codespace:** Navigate to the course repository on GitHub and click the "Codespaces" button. This will open a cloud-based development environment.
2. **Create a New Branch:**
   * Open the terminal in your Codespace.
   * Use the following command to create a new branch with your student ID or name:

   ```
   git branch your_branch_name
   ```
   Replace `your_branch_name` with your desired branch name (e.g., `student123`, `john_doe`).

3. **Switch to Your Branch:**
   * Use the following command to switch to your newly created branch:

   ```
   git checkout your_branch_name
   ```

### Starting Your Work

Now that you have your own branch, you can start working on your Python exercises and projects. All changes you make will be isolated to this branch, allowing you to experiment without affecting the main course code.

**Important:** Remember to commit your changes regularly using the following commands:

```bash
git add .  # Add all changes to the staging area
git commit -m "Your commit message"  # Commit changes with a descriptive message
```

### Pushing Your Work to GitHub

Once you're finished with a set of changes, you can push your branch to the remote repository:

```bash
git push origin your_branch_name
```

This allows you to share your work with others and create pull requests if needed.

**Note:** For more advanced Git usage and collaboration, refer to the Git documentation or online tutorials.
 
**Additional Tips:**
* Use descriptive commit messages to track your changes effectively.
* Regularly push your work to avoid losing progress.
* Consider using a `.gitignore` file to exclude unnecessary files from being tracked by Git.

By following these steps, you'll have a dedicated workspace for your Python course, enabling you to work independently and efficiently.
