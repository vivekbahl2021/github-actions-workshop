# Display Environment Variables

## Introduction

In this lab, you will learn how to display environment variables in a Linux, MacOS and Windows operating system using GitHub Actions.

GitHub Actions allows you to display environment variables in the logs. This can be useful for debugging purposes or to understand the environment in which your code is running. Please note, these environment variables are not secure and should not be used to store sensitive information and they are case sensitive.

## Instructions

1. Create a new workflow file called `display-environment-variables.yml` in the `.github/workflows` directory.
2. Edit the file and copy the following YAML content:

   ```YAML
   name: Display Environment Variables

   on:
   workflow_dispatch:

   jobs:
   ubuntu:
       runs-on: ubuntu-latest
       steps:
       - name: Display Environment Variables
           run: printenv | sort
   mac:
       runs-on: macos-latest
       steps:
       - name: Display Environment Variables
           run: printenv | sort
   windows:
       runs-on: windows-latest
       steps:
       - name: Display Environment Variables
           run: printenv | sort
           shell: bash
   ```

3. Commit the workflow changes into the `main` branch.
4. Go to the repository on GitHub and navigate to the `Actions` tab.
5. Click on the `Display Environment Variables` workflow.
6. Click on the `Run workflow` dropdown and select the branch `main`.
7. Click the `Run workflow` button.
8. Click on the `Display Environment Variables` job to see the environment variables for the Linux, MacOS and Windows operating systems.
9. Review the environment variables displayed in the logs.
10. Note that there are few operating system specific environment variables that are displayed and some common environment variables that are displayed across all operating systems.

## Lab Solution

The complete solution is provided below.

```YAML
  name: Display Environment Variables

  on:
  workflow_dispatch:

  jobs:
  ubuntu:
      runs-on: ubuntu-latest
      steps:
      - name: Display Environment Variables
          run: printenv | sort
  mac:
      runs-on: macos-latest
      steps:
      - name: Display Environment Variables
          run: printenv | sort
  windows:
      runs-on: windows-latest
      steps:
      - name: Display Environment Variables
          run: printenv | sort
          shell: bash
```

Additionally, you can also use matrix strategy to run the same job across multiple operating systems. The matrix strategy allows you to run the same job across multiple operating systems in parallel. The matrix strategy is useful when you want to test your code across multiple operating systems.

```YAML
name: Display Environment Variables
on:
  workflow_dispatch:
jobs:
  display-environment-variables:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
    steps:
      - name: Display Environment Variables
        run: printenv | sort
```

## Summary

You have successfully created a workflow to display environment variables in a Linux, MacOS and Windows operating system using GitHub Actions. You have also learned how to use the matrix strategy to run the same job across multiple operating systems in parallel.

## References

- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions)
- [Using environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
- [Environment variables](https://docs.github.com/en/actions/reference/environment-variables)
- [Default environment variables](https://docs.github.com/en/codespaces/developing-in-a-codespace/default-environment-variables-for-your-codespace)
