# Simple Workflow Lab

## Introduction

In this lab, you will use a `simple workflow` built-in template that triggers a workflow on every push to the repository. The workflow will echo a message to the console.

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

## Summary

In this lab, you created a simple workflow that runs on every push to the repository. The workflow echoed the messages to the console.

## Additional Resources

1. [GitHub Actions Documentation](https://docs.github.com/en/actions)
