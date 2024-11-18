# Environments, Variables and Secrets

## Introduction

In this lab, you will learn how to setup different environments in GitHub and how to use environment variables and secrets. You will also learn how to use those variables and secrets in your workflows.

## Create Environments

1. Go to your repository on GitHub
2. Click on `Settings` tab
3. Click on `Environments` on the left sidebar
4. Click on `New environment` button
5. Enter the environment name as `dev` and click on `Create environment` button
6. Repeat steps 4 and 5 to create `prod` environment

## Add Environment Variables

1. Go to your repository on GitHub
2. Click on `Settings` tab
3. Click on `Environments` on the left sidebar
4. Click on `dev` environment
5. Click on `Add environment variable` button
6. Enter the name as `ENVIRONMENT` and value as `dev` and click on `Add variable` button
7. Repeat steps 4 to 6 for `prod` environment with value as `prod`

## Add Environment Secrets

1. Go to your repository on GitHub
2. Click on `Settings` tab
3. Click on `Environments` on the left sidebar
4. Click on `dev` environment
5. Click on `Add environment secret` button
6. Enter the name as `SECRET` and value as `dev-secret` and click on `Add secret` button
7. Repeat steps 4 to 6 for `prod` environment with value as `prod-secret`

## Add Repository Variables

1. Go to your repository on GitHub
2. Click on `Settings` tab
3. Expand `Secrets and variables` on the left sidebar
4. Click on `Actions`
5. Click on `New repository variables` button
6. Enter the name as `REPOSITORY_VARIABLE` and value as `repository-variable` and click on `Add variable` button

## Use Environment Variables and Secrets in Workflows

1. Open the workflow file [environments-and-secrets.yml](/.github/workflows/environments-variables-and-secrets.yml)
2. Edit the file and copy the following YAML content at the end of the file:

   ```YAML
   env:
       ENVIRONMENT: ${{ github.event.inputs.environment }}
       SECRET: ${{ secrets.SECRET }}
   ```

3. Commit the changes into the `main` branch
4. Go to `Actions` and manually trigger the workflow by clicking on `Run Workflow` button
5. See the details of your running workflow

## References

- [Using environments for deployment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)
- [Encrypted secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Accessing your secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets#accessing-your-secrets)
