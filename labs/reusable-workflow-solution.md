# Reusable Workflow Solution

## Reusable Echo Workflow

```yaml
name: Reusable Workflow Echo
on:
  workflow_call:
    inputs:
      my-input:
        required: true
        type: string
jobs:
  echo:
    runs-on: ubuntu-latest
    steps:
      - name: Echo input
        run: echo ${{ inputs.my-input }}
```

## Echo Caller Workflow

```yaml
name: Reusable Workflow Echo Caller

on:
  workflow_dispatch:
  push:
    paths:
      - '.github/workflows/reusable-workflow-echo-caller.yml'
jobs:
  call:
    uses: ./.github/workflows/reusable-workflow-echo.yml
    with:
      my-input: 'Hello, world!'
```
