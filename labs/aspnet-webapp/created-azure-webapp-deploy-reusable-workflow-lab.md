# Creating a Reusable Workflow for Deploying an ASP.NET Web App to Azure Lab

## Objective

In this lab, you will learn how to create a reusable GitHub Actions workflow for deploying an ASP.NET Web App to Azure. This reusable workflow will allow you to standardize the deployment process across multiple workflows or projects by passing in parameters for the web app name and package path.

### Prerequisites

1. **Azure Subscription**: You need an Azure subscription where your web app will be deployed.
2. **Azure Service Principal**: A service principal is required to authenticate the workflow with Azure. Store the service principal in GitHub secrets for secure access.
3. **GitHub Repository**: A GitHub repository to store the workflow YAML files and use GitHub Actions.

---

### Step 1: Create the Reusable Workflow File

1. **Navigate to the `.github/workflows` directory** of your repository.
2. **Create a new file** named `reusable-workflow-azure-webapp-deploy.yml`.

3. **Define the reusable workflow**:
   Paste the following YAML content into the `reusable-workflow-azure-webapp-deploy.yml` file. This workflow is responsible for deploying the web app to Azure.

```yaml
name: Reusable Workflow Azure Web App Deploy

on:
  workflow_call:
    inputs:
      AZURE_WEBAPP_PACKAGE_PATH:
        required: true
        type: string
      AZURE_WEBAPP_NAME:
        required: true
        type: string
    secrets:
      AZURE_SERVICE_PRINCIPAL:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Download artifact from build job
        uses: actions/download-artifact@v4
        with:
          name: webapp
          path: ${{ inputs.AZURE_WEBAPP_PACKAGE_PATH }}

      - name: Azure Login
        uses: azure/login@v2
        with:
          creds: ${{ secrets.AZURE_SERVICE_PRINCIPAL }}

      - name: Deploy to Azure WebApp
        uses: azure/webapps-deploy@v2
        with:
          app-name: ${{ inputs.AZURE_WEBAPP_NAME }}
          package: ${{ inputs.AZURE_WEBAPP_PACKAGE_PATH }}
```

#### Breakdown of the workflow:

- **`workflow_call`**: This event allows other workflows to call this reusable workflow. It defines two required inputs:

  - `AZURE_WEBAPP_PACKAGE_PATH`: The path to the web app package that will be deployed.
  - `AZURE_WEBAPP_NAME`: The name of the Azure Web App where the package will be deployed.

  It also defines a required secret `AZURE_SERVICE_PRINCIPAL` for authentication with Azure.

- **`deploy` job**:
  - **`actions/download-artifact@v4`**: Downloads the build artifact (the web app package) from the previous job or workflow.
  - **`azure/login@v2`**: Logs in to Azure using the provided Service Principal.
  - **`azure/webapps-deploy@v2`**: Deploys the web app to Azure using the specified web app name and package.

### Step 2: Set Up Secrets for Authentication

To allow GitHub Actions to authenticate with Azure, you need to create an Azure Service Principal and store it as a GitHub secret.

1. **Create an Azure Service Principal**:

   - Follow the [official guide](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-service-principal-portal) to create a Service Principal in Azure.
   - The necessary information you need to save is:
     - **App ID** (Client ID)
     - **Tenant ID**
     - **Client Secret**

2. **Add the Service Principal as a GitHub Secret**:
   - In your GitHub repository, go to **Settings** > **Secrets and variables** > **Actions**.
   - Click **New repository secret** and name it `AZURE_SERVICE_PRINCIPAL`.
   - Paste the Azure Service Principal JSON in the format:
     ```json
     {
       "clientId": "<App-ID>",
       "clientSecret": "<Secret>",
       "tenantId": "<Tenant-ID>"
     }
     ```

### Step 3: Test the Reusable Workflow

At this stage, you have created a reusable workflow to deploy your ASP.NET Web App to Azure. You can now integrate this reusable workflow into your main workflow (to be covered in a future lab document).

### Step 4: Conclusion

In this lab, you successfully created a reusable workflow for deploying an ASP.NET Web App to Azure using GitHub Actions. This reusable workflow can now be called from any other workflow, allowing you to automate deployments across different projects.

### Next Steps

- In the next lab, we will integrate this reusable deployment workflow into your main CI/CD pipeline to build and deploy an ASP.NET Web App to Azure automatically.
