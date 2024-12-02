# Python Upper App Unit Test

## Introduction

In this lab, you will create a GitHub Actions workflow to build and unit test a Python application. The workflow will be triggered manually and will run on a ubuntu-latest runner.

## Python Upper Application

The Python application is a simple console based application that converts the input string to uppercase. The source code for the Python application is available in the `src/python/upper_project` directory. It also contains the unit tests for the application.

> Duration: 30-45 minutes

## Instructions

1. Open `GitHub Actions Workshop` repository in Visual Studio Code.
1. Go to `.github/workflows` directory and create a new file named `python-upper-test.yml`.
1. Add the following code to the `python-upper-test.yml` file to trigger the workflow manually. Also add the path filter to trigger the workflow when changes are made to the workflow file or the Python application source code.

   ```YAML
   name: React Tic-Tac-Toe Build and Dockerize
   on:
     workflow_dispatch:
     push:
      paths:
        - '.github/workflows/python-upper-test.yml'
        - 'src/python/upper_project/**'
   ```

1. Add following code to build the React Tic-Tac-Toe game.

   ```YAML
    jobs:
      run:
        runs-on: ubuntu-latest
        steps:
          - name: Get all the files in current directory before checkout
            run: pwd && ls -al

          - name: Checkout Code
            uses: actions/checkout@v4

          - name: Get all the files in current directory after checkout
            run: pwd && ls -al

          - name: Print Python version
            run: python --version

          - name: Print pip version
            run: python -m pip --version

          - name: Upgrade pip
            run: python -m pip install --upgrade pip

          - name: Unit test
            run: python -m unittest discover tests
            working-directory: src/python/upper_project
   ```

1. Commit the changes to the `main` branch and push the changes to the remote repository.

1. Navigate to the `Actions` tab in the GitHub repository to see the workflow running. Click on the `Run workflow` button and select the `main` branch to trigger the workflow manually.

1. Once the workflow is completed, navigate to the Docker Hub repository to see the docker image pushed.

## Summary

In this lab, you created a GitHub Actions workflow to build and unit test a Python application. The workflow was triggered manually and ran on a ubuntu-latest runner.
