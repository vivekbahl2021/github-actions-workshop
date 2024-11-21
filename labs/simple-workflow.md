# Simple Workflow

## Introduction

In this lab, you will create a simple workflow that runs on every push to the repository. The workflow will echo a message to the console.

> Duration: 10-15 minutes

## Instructions

1. Navigate to the repository you created in the previous lab.

   ![Navigate to Repository](../images/simple-workflow/1.png)

2. Navigate to `Actions` tab.

   ![Navigate to Actions](../images/simple-workflow/2.png)

3. Click on the `New workflow` button.

   ![New Workflow](../images/simple-workflow/3.png)

4. Select `Simple workflow` template and click on `Configure` button

   ![Select Simple Workflow](../images/simple-workflow/4.png)

5. Enter the workflow name as `simple-workflow.yml` and click on `Commit changes...` button

   ![Enter Workflow Name](../images/simple-workflow/5.png)

6. This will create a new file `.github/workflows/simple-workflow.yml` in your repository

   ![Workflow Created](../images/simple-workflow/6.png)

7. Navigate to Actions tab and you will see the workflow in the list.

   ![Workflow List](../images/simple-workflow/7.png)

8. Click on `Run workflow` button and select `main` branch and click on `Run workflow` button

   ![Run Workflow](../images/simple-workflow/8.png)

9. This will trigger the workflow and you will see the workflow running. Click on the workflow run to see the details of the workflow run.

   ![Workflow Run](../images/simple-workflow/9.png)

## Solution

<details>
  <summary>simple-workflow.yml</summary>
  
```YAML

# This is a basic workflow to help you get started with Actions

name: Simple Workflow

# Controls when the workflow will run

on:

# Triggers the workflow on push or pull request events but only for the "main" branch

# push:

# branches: ['main']

# pull_request:

# branches: ['main']

# Allows you to run this workflow manually from the Actions tab

workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel

jobs:

# This workflow contains a single job called "build"

build: # The type of runner that the job will run on
runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v4

      # Runs a single command using the runners shell
      - name: Run a one-line script
        run: echo Hello, world!

      # Runs a set of commands using the runners shell
      - name: Run a multi-line script
        run: |
          echo Add other actions to build,
          echo test, and deploy your project.

```

</details>

## Summary

In this lab, you created a simple workflow that runs on every push to the repository. The workflow echoed a message to the console.

## Additional Resources

1. [GitHub Actions Documentation](https://docs.github.com/en/actions)
```
