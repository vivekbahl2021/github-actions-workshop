# React Tic-Tac-Tow Build and Dockerize Workflow

## Introduction

In this lab, you will create a GitHub Actions workflow to build and dockerize a React Tic-Tac-Toe game. The workflow will be triggered manually and will run on a ubuntu-latest runner. The source code for the React Tic-Tac-Toe game is available in the `src/react/tic-tac-toe` directory.

> Duration: 45-60 minutes

## Instructions

1. Open `GitHub Actions Workshop` repository in Visual Studio Code.
1. Go to `.github/workflows` directory and create a new file named `react-tic-tac-toe-build-dockerize.yml`.
1. Add the following code to the `react-tic-tac-toe-build-dockerize.yml` file to trigger the workflow manually. Also add the path filter to trigger the workflow when changes are made to the workflow file or the React Tic-Tac-Toe source code.

   ```YAML
   name: React Tic-Tac-Toe Build and Dockerize
   on:
     workflow_dispatch:
     push:
      paths:
        - '.github/workflows/react-tic-tac-toe-build-dockerize.yml'
        - 'src/react/react-tic-tac-toe/**'
   ```

1. Setup Docker Hub credentials as secrets in the GitHub repository. Go to the GitHub repository and navigate to `Settings` -> `Secrets` and add the following secrets.

   - `DOCKER_USERNAME` - Docker Hub username
   - `DOCKER_PASSWORD` - Docker Hub password

1. Now set the environment variables for the Docker image and the context path. Add the following code to the `react-tic-tac-toe-build-dockerize.yml` file. Please note to change the `DOCKER_IMAGE` and `CONTEXT_PATH` values as per your repository.

   ```YAML
    env:
      DOCKER_IMAGE: prasadhonrao/react-tic-tac-toe
      CONTEXT_PATH: ./src/react/react-tic-tac-toe
   ```

1. Add following code to build the React Tic-Tac-Toe game.

   ```YAML
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - name: Checkout Code
           uses: actions/checkout@v4
           with:
             submodules: true # Fetch the submodules
         - name: Set up Node.js
           uses: actions/setup-node@v4
           with:
             node-version: '20'
         - name: Install dependencies
           run: npm ci
           working-directory: ${{ env.CONTEXT_PATH }}
   ```

1. Add the following code to build the docker image and push it to Docker Hub. Note that, dockerize job depends on the build job.

   ```YAML
    dockerize:
      runs-on: ubuntu-latest
      needs: build
      steps:
        - name: Checkout Code
          uses: actions/checkout@v4
          with:
            submodules: true # Ensure submodules are available for Docker build
        - name: Set up Docker Buildx
          uses: docker/setup-buildx-action@v2
        - name: Log in to Docker Hub
          uses: docker/login-action@v2
          with:
            username: ${{ secrets.DOCKER_USERNAME }}
            password: ${{ secrets.DOCKER_PASSWORD }}
        - name: Build and push Docker image
          run: |
            cd ${{ env.CONTEXT_PATH }}
            TAG=${{ github.sha }}
            docker build -t ${{ env.DOCKER_IMAGE }}:$TAG -t ${{ env.DOCKER_IMAGE }}:latest .
            docker push ${{ env.DOCKER_IMAGE }}:$TAG
            docker push ${{ env.DOCKER_IMAGE }}:latest

   ```

1. Commit the changes to the `main` branch and push the changes to the remote repository.

1. Navigate to the `Actions` tab in the GitHub repository to see the workflow running. Click on the `Run workflow` button and select the `main` branch to trigger the workflow manually.

1. Once the workflow is completed, navigate to the Docker Hub repository to see the docker image pushed.

## Workflow Code

The complete workflow code is shown below.

```YAML
  name: React Tic-Tac-Toe Build and Dockerize

  on:
    workflow_dispatch:
    push:
      paths:
        - '.github/workflows/react-tic-tac-toe-build-dockerize.yml'
        - 'src/react/react-tic-tac-toe/**'

  env:
    DOCKER_IMAGE: prasadhonrao/react-tic-tac-toe
    CONTEXT_PATH: ./src/react/react-tic-tac-toe

  jobs:
    build:
      runs-on: ubuntu-latest
      steps:
        - name: Checkout Code
          uses: actions/checkout@v4
          with:
            submodules: true # Fetch the submodules
        - name: Set up Node.js
          uses: actions/setup-node@v4
          with:
            node-version: '20'
        - name: Install dependencies
          run: npm ci
          working-directory: ${{ env.CONTEXT_PATH }}

    dockerize:
      runs-on: ubuntu-latest
      needs: build
      steps:
        - name: Checkout Code
          uses: actions/checkout@v4
          with:
            submodules: true # Ensure submodules are available for Docker build
        - name: Set up Docker Buildx
          uses: docker/setup-buildx-action@v2
        - name: Log in to Docker Hub
          uses: docker/login-action@v2
          with:
            username: ${{ secrets.DOCKER_USERNAME }}
            password: ${{ secrets.DOCKER_PASSWORD }}
        - name: Build and push Docker image
          run: |
            cd ${{ env.CONTEXT_PATH }}
            TAG=${{ github.sha }}
            docker build -t ${{ env.DOCKER_IMAGE }}:$TAG -t ${{ env.DOCKER_IMAGE }}:latest .
            docker push ${{ env.DOCKER_IMAGE }}:$TAG
            docker push ${{ env.DOCKER_IMAGE }}:latest

```

## Summary

In this lab, you created a GitHub Actions workflow to build and dockerize a React Tic-Tac-Toe game. The workflow was triggered manually and ran on a ubuntu-latest runner. The workflow built the React Tic-Tac-Toe game and dockerized it.

## Additional Resources

1. [GitHub Actions Documentation](https://docs.github.com/en/actions)
