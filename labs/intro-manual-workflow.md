# Manual Workflow Lab

## Introduction

In this lab you will create a manual workflow that runs on a manual trigger. The workflow will echo a message to the console.

> Duration: 10-15 minutes

## Instructions

1. Navigate to the repository you created in the previous lab. If you have not completed the previous lab, you can clone the repository from [here](./create-repository-using-template-repository.md).

2. Navigate to `Actions` tab.

3. Click on the `New workflow` button.

4. Select `Manual workflow` template and click on `Configure` button

5. This will open GitHub Action's workflow editor.

6. Enter the workflow name as `intro-manual-workflow.yml` and add following content in the editor and click on `Commit changes` button.

   ```YAML
   name: Intro - Manual Workflow

   on:
   workflow_dispatch:
   push:
      paths:
         - '.github/workflows/intro-manual-workflow.yml'
   jobs:
   run:
      runs-on: ubuntu-latest
      steps:
         - name: Hows GitHub Actions?
         run: echo "Awesome!!"
   ```

7. We have given `Intro - Manual Workflow` as the name of the workflow. The workflow runs on two events - `workflow_dispatch` and `push`. The `workflow_dispatch` event is a manual trigger event. The workflow runs on push event only if the file `.github/workflows/intro-manual-workflow.yml` is modified. The workflow runs on `ubuntu-latest` runner and has a single job `run`. The job has a single step that echos a message `Awesome!!`.

8. This will create a new file `.github/workflows/intro-manual-workflow.yml` in your repository.

9. Navigate to Actions tab and you will see the workflow in the list. If the workflow is not running, you can manually trigger the workflow.

10. Click on `Run workflow` button and select `main` branch and click on `Run workflow` button. This will trigger the workflow and you will see the workflow running.

11. Click on the workflow run to see the details of the workflow run.

12. Click on the job to see the details of the job.

13. Expand the `How GitHub Actions?` step to see the output of the step.

14. You will see the message `Awesome!!` in the output of the step.

## Summary

In this lab, you created a manual workflow that runs on a manual trigger. The workflow echoed a message to the console.

## Additional Resources

1. [GitHub Actions Documentation](https://docs.github.com/en/actions)
