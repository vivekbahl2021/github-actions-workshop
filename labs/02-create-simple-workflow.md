# Create Simple Workflow

In this lab, you will create a simple workflow that runs on every push to the repository. The workflow will echo a message to the console.

> Duration: 10-15 minutes

## 2.1 Create a new workflow

1. Navigate to the repository you created in the previous lab.

   ![Navigate to Repository](../images/2.1-navigate-to-repository.png)

2. Navigate to `Actions` tab.

   ![Navigate to Actions](../images/2.2-navigate-to-actions.png)

3. Click on the `New workflow` button.

   ![New Workflow](../images/2.3-click-on-new-workflow.png)

4. Select `Simple workflow` template and click on `Configure` button

   ![Select Simple Workflow](../images/2.4-select-simple-workflow.png)

5. Enter the workflow name as `simple-workflow.yml` and click on `Commit changes...` button

   ![Enter Workflow Name](../images/2.5-enter-workflow-name.png)

6. This will create a new file `.github/workflows/simple-workflow.yml` in your repository

   ![Workflow Created](../images/2.6-workflow-created.png)

7. Navigate to Actions tab and you will see the workflow in the list.

   ![Workflow List](../images/2.7-workflow-list.png)

8. Click on `Run workflow` button and select `main` branch and click on `Run workflow` button

   ![Run Workflow](../images/2.8-run-workflow.png)
