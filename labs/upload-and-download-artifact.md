# Upload and Download Artifact

## Introduction

In this lab, you will learn how to upload and download artifacts in GitHub Actions workflow. You will create a simple workflow that builds a .NET Core application and uploads the build artifact to GitHub. You will then extend the workflow to download the artifact and display the contents.

> Duration: 20-30 minutes

## Instructions

### Create .NET Core Web Application using Command Line

1. Open a command prompt and create a new directory for the project.

   ```bash
   mkdir WebApp
   cd WebApp
   ```

2. Create a new .NET Core Web application using the following command.

   ```bash
    dotnet new webapp
   ```

3. Run the application using the following command.

   ```bash
    dotnet run
   ```

4. Open a browser and navigate to `https://localhost:5001` to view the application. You should see the default .NET Core Web application. Please note port number may vary.

5. Stop the application by pressing `Ctrl+C` in the command prompt.

6. Commit the source code to the repository. For this lab, you can save the source code `src/dotnet` directory.

### Create GitHub Actions Workflow using Visual Studio Code

1. Open Visual Studio Code and open the project directory.

2. Open existing directory `.github/workflows` in the root of the project.

3. Create a new file named `upload-and-download-artifact.yml` and provide workflow name and event trigger information as shown below.

   ```yaml
   name: Upload and Download Artifact
   on:
     push:
       paths:
         - '.github/workflows/upload-download-artifact.yml'
         - 'src/dotnet/WebApp/**'
     workflow_dispatch:
   ```

4. Add a job to build and upload the .NET Core application. Note that we are providing `artifact name` and `path` to upload the artifact. We will refer to this artifact name and path in the download job.

   ```yaml
     jobs:
       upload:
         runs-on: windows-latest
         defaults:
           run:
             working-directory: ./src/dotnet/WebApp
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
             run: dotnet publish -c Release --property:PublishDir="${{env.DOTNET_ROOT}}\myapp"

           - name: Upload Artifact
             uses: actions/upload-artifact@v4.3.6
             with:
             name: .net-web-app # Artifact name
             path: ${{env.DOTNET_ROOT}}\myapp
   ```

5. Now add a job to download the artifact and display the contents.

   ```yaml
   download:
     runs-on: windows-latest
     steps:
       - name: Download Artifact
         uses: actions/download-artifact@v4.3.6
         with:
           name: .net-web-app # Artifact name

       - name: Display Artifact
         run: |
           Get-ChildItem -Path ${{ github.workspace }}\myapp -Recurse
   ```

6. Commit the changes to the repository.

### Run the Workflow

1. Go to the repository in GitHub and navigate to the `Actions` tab.

2. Click on the `Upload and Download Artifact` workflow and click on the `Run workflow` button.

3. Once the workflow is completed, click on the `Download Artifact` job to view the details.

4. You should see the contents of the artifact displayed in the logs.

5. You can also download the artifact by clicking on the `Download artifact` button.

6. Open the downloaded artifact and verify the contents.

## Conclusion

In this lab, you learned how to upload and download artifacts in GitHub Actions workflow. You created a simple workflow that builds a .NET Core application and uploads the build artifact to GitHub. You then extended the workflow to download the artifact and display the contents.

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions: Artifacts](https://docs.github.com/en/actions/guides/storing-workflow-data-as-artifacts)
