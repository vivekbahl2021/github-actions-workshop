# WebApp Build

## Introduction

In this lab, you will learn how to build a web application using GitHub Actions. You will create a workflow that builds the application. You will also learn how to use the `actions/setup-dotnet` action to set up the .NET Core SDK.

> Duration: 15-20 minutes

## Prerequisites

Create a new Web App by following the instructions in the [Create a Web App](./create-webapp.md) lab.

## Instructions

1. Open Visual Studio Code and open the project directory.

2. Open the existing directory `.github/workflows` in the root of the project.

3. Create a new file named `webapp-build.yml` and provide workflow name and event trigger information as shown below.

   ```yaml
   name: WebApp Build
   on:
     push:
       paths:
         - '.github/workflows/webapp-build.yml'
         - 'src/dotnet/WebApp/**'
     workflow_dispatch:
   ```

4. Add a job to build the .NET Core application. Note that we are using the `actions/setup-dotnet` action to set up the .NET Core SDK.

   ```yaml
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - name: checkout code
           uses: actions/checkout@v4.1.7

         - name: Set up .NET Core
           uses: actions/setup-dotnet@v4.0.1
           with:
           dotnet-version: '8.x'

         - name: Build code
           run: dotnet build --configuration Release

         - name: Publish code
           run: dotnet publish -c Release --property:PublishDir="${{runner.temp}}/webapp"
   ```

5. Commit the changes and push them to the repository.

6. Navigate to the "Actions" tab in your repository to view the workflow runs.

7. Click on the latest workflow run to view the details.

8. Click on the job to view the logs.

9. Verify that the workflow has built and published the application successfully.

## Summary

In this lab, you learned how to build a web application using GitHub Actions. You created a workflow that builds the application and used the `actions/setup-dotnet` action to set up the .NET Core SDK.
