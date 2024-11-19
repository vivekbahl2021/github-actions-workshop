# Display Workflow Status Badge

## Introduction

In this section, you will learn how to display the workflow status badge on the GitHub repository. The workflow status badge shows the status of the latest workflow run on the repository.

> Duration: 10-15 minutes

## Instructions

1. Go to your repository on GitHub.
1. Click the **"Actions"** tab.
1. Choose a workflow template or create a new workflow file.
1. Save the workflow. It will be stored in `.github/workflows/`.
1. Go to the **"Actions"** tab.
1. Locate the specific workflow for which you want the badge.
1. Click the **ellipsis (`...`) menu** on the workflow’s page and select **"Create status badge."**
1. GitHub will provide you with a Markdown snippet. It will look like this:

   ```markdown
   ![Workflow Name](https://github.com/<OWNER>/<REPO>/actions/workflows/<WORKFLOW_FILE>.yml/badge.svg)
   ```

1. Replace `<OWNER>`, `<REPO>`, and `<WORKFLOW_FILE>` with the relevant values from your repository.
1. Locate and click on the `README.md` file in the root directory.
1. Click the pencil icon (**Edit this file**) in the top-right corner.
1. Add the badge Markdown snippet where you want the badge to appear. For example:

   ```markdown
   # Project Name

   ![Build Status](https://github.com/<OWNER>/<REPO>/actions/workflows/<WORKFLOW_FILE>.yml/badge.svg)

   ## Description

   A brief description of the project goes here.
   ```

1. After adding the badge, scroll to the bottom of the page.
1. Add a commit message describing your change, e.g., `"Added GitHub Actions workflow status badge to README"`.
1. Choose to commit directly to the `main` branch or create a new branch and open a pull request.
1. Click **"Commit changes"** or **"Propose changes"**.

1. Go back to the repository’s main page.
1. The badge should now appear in your `README.md`, showing the current status of the workflow (e.g., "passing" or "failing").

## Example Badge

```markdown
# GitHub Actions Workshop

[![Simple Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/simple-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/simple-workflow.yml)

## About

GitHub Actions Workshop is designed to help you get started with GitHub Actions and learn how to use them to automate your software development workflow.
```

Here’s an example of what a workflow badge might look like in a `README.md`:

[![Simple Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/simple-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/simple-workflow.yml)

The badge will automatically update whenever the workflow runs, showing the latest status.

## Conclusion

Congratulations! You have successfully added a workflow status badge to your GitHub repository. The badge will help you and others quickly see the status of the latest workflow run on the repository.

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Creating a status badge for your workflow](https://docs.github.com/en/actions/managing-workflow-runs/adding-a-workflow-status-badge)
