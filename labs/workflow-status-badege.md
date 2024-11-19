# Display the workflow status badge

## Introduction

In this section, you will learn how to display the workflow status badge on the GitHub repository. The workflow status badge shows the status of the latest workflow run on the repository.

> Duration: 10-15 minutes

## 1. Ensure You Have a GitHub Actions Workflow

- If you already have a workflow configured, locate the workflow file (`.yml`) in your repository under the `.github/workflows/` directory.
- If you don’t have one, you can create a new workflow:

  1. Go to your repository on GitHub.
  2. Click the **"Actions"** tab.
  3. Choose a workflow template or create a new workflow file.
  4. Save the workflow. It will be stored in `.github/workflows/`.

---

## 2. **Get the Badge URL**

- To generate a badge for your workflow:

  1. Navigate to your repository on GitHub.
  2. Go to the **"Actions"** tab.
  3. Locate the specific workflow for which you want the badge.
  4. Click the **ellipsis (`...`) menu** on the workflow’s page and select **"Create status badge."**
  5. GitHub will provide you with a Markdown snippet. It will look like this:
     ```markdown
     ![Workflow Name](https://github.com/<OWNER>/<REPO>/actions/workflows/<WORKFLOW_FILE>.yml/badge.svg)
     ```
     Replace `<OWNER>`, `<REPO>`, and `<WORKFLOW_FILE>` with the relevant values from your repository.

---

## 3. **Add the Badge to Your README**

- Edit your repository’s `README.md` file:

  1. Open your repository on GitHub.
  2. Locate and click on the `README.md` file in the root directory.
  3. Click the pencil icon (**Edit this file**) in the top-right corner.
  4. Add the badge Markdown snippet where you want the badge to appear. For example:

     ```markdown
     # Project Name

     ![Build Status](https://github.com/<OWNER>/<REPO>/actions/workflows/<WORKFLOW_FILE>.yml/badge.svg)

     ## Description

     A brief description of the project goes here.
     ```

---

## 4. **Save and Commit Changes**

- After adding the badge, scroll to the bottom of the page.
- Add a commit message describing your change, e.g., `"Added GitHub Actions workflow status badge to README"`.
- Choose to commit directly to the `main` branch or create a new branch and open a pull request.
- Click **"Commit changes"** or **"Propose changes"**.

---

## 5. **Verify the Badge**

- Go back to the repository’s main page.
- The badge should now appear in your `README.md`, showing the current status of the workflow (e.g., "passing" or "failing").

---

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
