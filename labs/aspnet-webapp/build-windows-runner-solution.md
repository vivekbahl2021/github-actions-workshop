## ASP.NET Web App Build on Windows Runner Solution

```yaml
name: ASP.NET Web App Build on Windows Runner

on:
  push:
    paths:
      - '.github/workflows/aspnet-webapp-build-windows-runner.yml'
      - 'src/dotnet/WebApp/**'
  workflow_dispatch:

jobs:
  build:
    runs-on: windows-latest
    defaults:
      run:
        working-directory: ./src/dotnet/WebApp
    steps:
      - name: Checkout Code
        uses: actions/checkout@v4.1.7

      - name: Set up .NET Core
        uses: actions/setup-dotnet@v4.0.1
        with:
          dotnet-version: '8.x'

      - name: Build Code
        run: dotnet build --configuration Release

      - name: Publish Code
        run: dotnet publish -c Release --property:PublishDir="${{runner.temp}}/webapp"
```