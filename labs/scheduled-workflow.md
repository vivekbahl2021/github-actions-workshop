# Scheduled Workflow

## Introduction

Scheduled workflows are workflows that are triggered on a schedule. You can use scheduled workflows to run tasks that you want to happen at specific times, such as sending reminders, cleaning up data, or syncing data between systems. In this lab, you will create a scheduled workflow that displays current date and time in the logs every 5 minutes.

## Instructions

1. Create a new workflow file named `scheduled-workflow.yml` in the `.github/workflows` directory of your repository.

2. Define the workflow to run on a schedule of every 5 minutes using following syntax:

   ```yaml
   schedule:
     - cron: '*/5 * * * *' # Every 5 minutes.
   ```

3. You can use `https://crontab.guru/` to generate cron expressions

4. Use the `jobs` keyword to define a job named `scheduled-job`.

5. Define the job to run on the latest version of the `ubuntu-latest` runner. In this case we will be displaying the current date and time in the logs every 5 minutes.

   ```yaml
   jobs:
     run:
       runs-on: ubuntu-latest
       steps:
         - name: Display current date and time
           run: echo "The current date and time is $(date)"
   ```

6. Commit the changes to the repository and observe the scheduled workflow running every 5 minutes.

## Lab Solution

The complete workflow code is shown below:

```YAML
  name: Scheduled Workflow

    on:
      workflow_dispatch:
      schedule:
        - cron: '*/5 * * * *' # Every 5 minutes. You can use https://crontab.guru/ to generate cron expressions
      push:
        paths:
          - '.github/workflows/scheduled-workflow.yml'
    jobs:
      execute:
        runs-on: ubuntu-latest
        steps:
          - name: Display current date and time
            run: echo "The current date and time is $(date)"

```

## Summary

Congratulations! You have successfully created a scheduled workflow that displays the current date and time in the logs every 5 minutes. You can use scheduled workflows to automate tasks that need to run on a schedule, such as sending reminders, cleaning up data, or syncing data between systems.

## Additional Resources

- [GitHub Actions Documentation - Scheduled Events](https://docs.github.com/en/actions/learn-github-actions/events-that-trigger-workflows#scheduled-events)
- [Events that trigger workflows](https://docs.github.com/en/actions/learn-github-actions/events-that-trigger-workflows)
