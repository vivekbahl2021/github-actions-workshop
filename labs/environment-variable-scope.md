# Environment Variable Scope

## Introduction

In this lab, you will learn how to set environment variables at different scopes including workflow, job and step level. You will also learn how to access these environment variables in your workflow.

## Instructions

1. Create a new workflow file named `environment-variable-scope.yml` in the `.github/workflows` directory.
2. Define a new environment variable named `WORKFLOW_ENV_VAR` at the workflow level with the value `Workflow Environment Variable`.
3. Define a new environment variable named `JOB_ENV_VAR` at the job level with the value `Job Environment Variable`.
4. Define a new environment variable named `STEP_ENV_VAR` at the step level with the value `Step Environment Variable`.
5. Print the values of the environment variables `WORKFLOW_ENV_VAR`, `JOB_ENV_VAR` and `STEP_ENV_VAR` in the workflow.
6. Commit the changes to the `main` branch and observe the workflow run.

## Lab Solution

```yml
name: Environment Variables Scope

on:
  workflow_dispatch:

env:
  WORKFLOW_ENV_VAR: 'Workflow Environment Variable'

jobs:
  print:
    runs-on: ubuntu-latest

    env:
      JOB_ENV_VAR: 'Job Environment Variable'

    steps:
      - name: Display Environment Variables
        env:
          STEP_ENV_VAR: 'Step Environment Variable'
        run: |
          echo "WORKFLOW_ENV_VAR: $WORKFLOW_ENV_VAR"
          echo "JOB_ENV_VAR: $JOB_ENV_VAR"
          echo "STEP_ENV_VAR: $STEP_ENV_VAR"
```

## Summary

Congratulations! You have successfully set environment variables at different scopes and accessed them in your workflow.
