# WebApp Build, Upload and Download Artifacts for Multiple OS

## Introduction

In this lab, you will learn how to create a GitHub Actions workflow that uploads and downloads artifacts on multiple operating systems. You will create a workflow that builds a .NET Core application and uploads the build artifacts for Windows, Ubuntu, and macOS. You will then create a workflow that downloads the artifacts and displays the contents of the artifacts.

> Duration: 30-45 minutes

## Prerequisites

Create a new Web App by following the instructions in the [Create a Web App](./create-webapp.md) lab.

## Instructions

### Create a Workflow using Visual Studio Code

1. Open Visual Studio Code and open the project directory.

2. Open the existing directory `.github/workflows` in the root of the project.

3. Create a new file named `upload-and-download-artifact-multiple-os.yml` and provide workflow name and event trigger information as shown below.

   ```yaml
   name: Upload and Download Artifact on Multiple Operating Systems
   on:
     push:
       paths:
         - '.github/workflows/upload-and-download-artifact-multiple-os.yml'
         - 'src/dotnet/WebApp/**'
     workflow_dispatch:
   ```

4. Add a job to build and upload the .NET Core application for Windows, Ubuntu, and macOS. Note that we are providing `artifact name` and `path` to upload the artifact. We will refer to this artifact name and path in the download job.

   ```yaml
   jobs:
    upload:
        strategy:
        matrix:
            os: [ubuntu-latest, windows-latest, macos-latest]
        runs-on: ${{ matrix.os }}
        defaults:
        run:
            working-directory: ./src/dotnet/WebApp
            shell: bash # Use Bash shell for all steps
        steps:
        - name: checkout code
            uses: actions/checkout@v4.1.7

        - name: Set up .NET Core
            uses: actions/setup-dotnet@v4.0.1
            with:
            dotnet-version: '8.x'

        - name: Build code
            run: dotnet build --configuration Release

        - name: Publish Code
            run: |
            # Set the publish directory based on OS
            if [[ "$RUNNER_OS" == "Windows" ]]; then
                PUBLISH_DIR="${{ runner.temp }}\\webapp"
            else
                PUBLISH_DIR="${{ runner.temp }}/webapp"
            fi

            # Publish the application
            echo "Publishing to $PUBLISH_DIR"
            mkdir -p "$PUBLISH_DIR"
            dotnet publish -c Release --output "$PUBLISH_DIR"

            # Verify contents
            echo "Contents of $PUBLISH_DIR:"
            ls "$PUBLISH_DIR"

        - name: Upload Artifact
            uses: actions/upload-artifact@v4.3.6
            with:
            name: '.net-web-app-${{ runner.os }}'
            path: ${{ runner.temp }}/webapp
   ```

5. Now add a job to download the artifact and display the contents.

   ```yaml
   download:
     strategy:
       matrix:
         os: [ubuntu-latest, windows-latest, macos-latest]
     runs-on: ${{ matrix.os }}
     needs: upload
     defaults:
       run:
         shell: bash # Consistent shell for all OSes
     steps:
       - name: Download Artifact
         uses: actions/download-artifact@v4.1.8
         with:
           name: '.net-web-app-${{ runner.os }}'

       - name: List downloaded files
         run: |
           echo "Listing files in the downloaded directory:"
           ls -R $GITHUB_WORKSPACE
   ```

6. Save the file and commit the changes to the `main` branch.

7. Go to the repository in GitHub and click on the `Actions` tab.

8. Click on the `Upload and Download Artifact on Multiple Operating Systems` workflow and click on the `Run workflow` button.

9. Once the workflow is complete, notice that the artifacts are uploaded and downloaded for Windows, Ubuntu, and macOS.

10. Click on the `Download Artifact` job to view the details.

## Summary

In this lab, you learned how to create a GitHub Actions workflow that uploads and downloads artifacts on multiple operating systems. You created a workflow that builds a .NET Core application and uploads the build artifacts for Windows, Ubuntu, and macOS. You then created a workflow that downloads the artifacts and displays the contents of the artifacts.

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions: Upload Artifact](https://docs.github.com/en/actions/guides/storing-workflow-data-as-artifacts)
- [GitHub Actions: Download Artifact](https://docs.github.com/en/actions/guides/downloading-workflow-artifacts)
