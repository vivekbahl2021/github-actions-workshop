# Lab: ASP.NET Web App Deploy Lab

## Objective

In this lab, you will learn how to create a GitHub Actions workflow to build and deploy an ASP.NET web application. The workflow will automatically trigger when changes are pushed to the `src/dotnet/WebApp` directory and will deploy the web app to an Azure App Service.

> Duration: 30-45 minutes

---

## Prerequisites

1. **GitHub Repository**: Ensure that your repository has an ASP.NET web application located in the `src/dotnet/WebApp` directory.

---

## Instructions

### Step 1: Open the GitHub Actions Workflow File

1. Open the `GitHub Actions` repository in **Visual Studio Code** or your preferred IDE.
2. Go to the `.github/workflows` directory and create a new file named `aspnet-webapp-deploy.yml`.

### Step 2: Define the Workflow Trigger

1. Add the following YAML code to define the workflow trigger. The workflow will run automatically on a `push` event when there are changes to the `src/dotnet/WebApp` directory or when manually triggered (`workflow_dispatch`).

   ```yaml
   name: ASP.NET Web App Build and Deploy

   on:
     push:
       paths:
         - '.github/workflows/aspnet-webapp-deploy.yml'
         - 'src/dotnet/WebApp/**'
     workflow_dispatch:
   ```

### Step 3: Define the Build Job

1. Add the following code to define the `build` job that will run on the `ubuntu-latest` runner. This job will build and publish the ASP.NET web app.

   ```yaml
   jobs:
     build:
       runs-on: ubuntu-latest
       defaults:
         run:
           working-directory: ./src/dotnet/WebApp
       steps:
         - name: Checkout code
           uses: actions/checkout@v4.1.7

         - name: Set up .NET Core
           uses: actions/setup-dotnet@v4.0.1
           with:
             dotnet-version: '8.x'

         - name: Build code
           run: dotnet build --configuration Release

         - name: Publish code
           run: dotnet publish -c Release --property:PublishDir="${{runner.temp}}/webapp"

         - name: Upload Artifact
           uses: actions/upload-artifact@v4.3.6
           with:
             name: aspnet-web-app # Artifact name
             path: ${{runner.temp}}/webapp
   ```

   **Explanation**:

   - The `actions/checkout` step checks out the code.
   - The `actions/setup-dotnet` action sets up the .NET Core environment.
   - The `dotnet build` command builds the app in the `Release` configuration.
   - The `dotnet publish` command publishes the app to a directory.
   - The `actions/upload-artifact` step uploads the published output as an artifact for later use in the deployment job.

### Step 4: Define the Deploy Job

1. Below the build job, define the `deploy` job. This job will deploy the artifact from the build job to the Azure App Service.

   ```yaml
   deploy:
     runs-on: ubuntu-latest
     needs: build
     env:
       package-name: aspnet-web-app
       app-name: github-actions-webapp
       deployment-slot: production

     steps:
       - name: Download artifact from build job
         uses: actions/download-artifact@v4.1.8
         with:
           name: aspnet-web-app # Artifact name

       - name: List files in root directory
         run: |
           ls -al
         shell: bash
   ```

   **Explanation**:

   - The `actions/download-artifact` action downloads the published artifact from the build job.
   - The `ls -al` command lists files in the root directory to confirm the artifact download.
   - The `Secret Information` step prints the match result of the secret (you can update this later for actual deployment).
   - The `Print name of App Service to deploy` step simply outputs the name of the app to confirm the target deployment app.

---

### Step 5: Commit and Push Changes

1. After adding the workflow file, commit the changes to your repository.

   ```bash
   git add .github/workflows/aspnet-webapp-deploy.yml
   git commit -m "Add ASP.NET Web App Build and Deploy Workflow"
   git push
   ```

---

### Step 6: Trigger the Workflow

1. Once you push the changes to the repository, the workflow will automatically trigger when you push changes to the `src/dotnet/WebApp` directory.
2. You can also manually trigger the workflow from the **Actions** tab in your GitHub repository by selecting the workflow and clicking the **Run workflow** button.

---

### Step 7: Verify the Deployment

1. Check the **Actions** tab in GitHub to see the status of the workflow.
2. Once the workflow completes, you should see the ASP.NET Web App deployed to your Azure App Service (if the actual Azure deployment step is added later).
3. Navigate to the URL of your Azure App Service to verify that the app is successfully deployed.

---

## Summary

In this lab, you have learned to:

- Create a GitHub Actions workflow to build and publish an ASP.NET web application.
- Define a deploy job that downloads the build artifact and prepares it for deployment.
- Push the workflow to GitHub and trigger it either automatically or manually.

In the next lab, you will add the actual Azure deployment steps and make use of reusable workflows for deployment.

---

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Azure App Service Documentation](https://learn.microsoft.com/en-us/azure/app-service/)
