# Manual Workflow

## Introduction

In this lab you will create a manual workflow that runs on a manual trigger. The workflow will echo a message to the console.

> Duration: 10-15 minutes

## Instructions

1. Navigate to the repository you created in the previous lab.

   ![Navigate to the Repository](../images/manual-workflow/1.png)

2. Navigate to `Actions` tab.

   ![Navigate to Actions](../images/manual-workflow/2.png)

3. Click on the `New workflow` button.

   ![New Workflow](../images/manual-workflow/3.png)

4. Select `Manual workflow` template and click on `Configure` button

   ![Select Manual Workflow](../images/manual-workflow/4.png)

5. This will open GitHub Action's workflow editor.

   ![Enter Workflow Name](../images/manual-workflow/5.png)

6. Enter the workflow name as `manual-workflow.yml` and add following content in the editor and click on `Commit changes` button.

   ```YAML
   name: Manual Workflow
   on:
    workflow_dispatch:
    push:
      paths:
      - '.github/workflows/manual-workflow.yml'
    jobs:
      run:
        runs-on: ubuntu-latest
        steps:
          - name: Hows GitHub Actions?
            run: echo "Awesome!!"
   ```

   ![Enter Workflow Name](../images/manual-workflow/6.png)

7. This will create a new file `.github/workflows/manual-workflow.yml` in your repository. Navigate to Actions tab and you will see the workflow in the list. Click on `Run workflow` button and select `main` branch and click on `Run workflow` button. This will trigger the workflow and you will see the workflow running.

   ![Commit Workflow](../images/manual-workflow/7.png)

8. Click on the workflow run to see the details of the workflow run.

   ![Run Workflow](../images/manual-workflow/8.png)

9. Click on the job to see the details of the job.

   ![Job Details](../images/manual-workflow/9.png)

## Solution

<details>
  <summary>manual-workflow.yml</summary>
  
```YAML
name: Manual Workflow
on:
  workflow_dispatch:
  push:
    paths:
      - '.github/workflows/manual-workflow.yml'
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Hows GitHub Actions?
        run: echo "Awesome!!"
```

</details>

## Conclusion

In this lab, you created a manual workflow that runs on a manual trigger. The workflow echoed a message to the console.

## Additional Resources

1. [GitHub Actions Documentation](https://docs.github.com/en/actions)
