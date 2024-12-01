# ASP.NET Web App Download Artifact Lab

## Introduction

In this lab, you will learn how to upload and download artifact in GitHub Actions workflow. You will create a simple workflow that builds a .NET Core application and uploads the build artifact to GitHub. You will then extend the workflow to download the artifact and display the contents.

> Duration: 20-30 minutes

## Prerequisites

Create a new Web App by following the instructions in the [Create a Web App](./create-aspnet-webapp.md) lab.

## Instructions

1. Open Visual Studio Code and open the project directory.

2. Open the existing directory `.github/workflows` in the root of the project.

3. Create a new file named `webapp-build-upload-download-artifact.yml` and provide workflow name and event trigger information as shown below.

   ```yaml
   name: WebApp Build
   on:
     push:
       paths:
         - '.github/workflows/webapp-build-upload-download-artifact.yml'
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

5. Add a new step to upload the artifact.

   ```yaml
   - name: Upload artifact
     uses: actions/upload-artifact@v2
     with:
       name: webapp-artifact
   ```

6. Add a new job to download the artifact and display the contents.

   ```yaml
   download:
     runs-on: ubuntu-latest
     needs: build
     steps:
       - name: Download artifact from build job
         uses: actions/download-artifact@v4.1.8
         with:
           name: .net-web-app # Artifact name
       - name: List files in root directory
         run: |
           ls -al
         shell: bash
   ```

7. Commit the changes and push them to the repository.

8. Navigate to the "Actions" tab in your repository to view the workflow runs.

9. Click on the latest workflow run to view the details.

10. Click on the job to view the logs.

11. Verify that the workflow has built and published the application successfully, and the artifact has been uploaded and downloaded, and the contents are displayed.

## Summary

In this lab, you learned how to upload and download artifact in GitHub Actions workflow. You created a simple workflow that builds a .NET Core application and uploads the build artifact to GitHub. You then extended the workflow to download the artifact and display the contents.

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions: Artifact](https://docs.github.com/en/actions/guides/storing-workflow-data-as-artifacts)
