## Composite Action: Print Message and Current Time

**Directory structure**:

```bash
.github/
└── actions/
    └── print-message-and-time-composite-action/
        ├── action.yml
```

### `action.yml` (Composite Action Definition)

```yaml
name: "Print Message and Time"
description: "Prints a custom message and the current date/time"
author: "Your Name"
inputs:
  message:
    description: "The message to print"
    required: true
    default: "Hello, GitHub Actions!"
outputs:
  timestamp:
    description: "The current date and time"
runs:
  using: "composite"
  steps:
    # Step 1: Print the input message
    - name: Print the message
      run: echo "Message: ${{ inputs.message }}"

    # Step 2: Capture and output the current time
    - name: Get current timestamp
      id: current_time
      run: echo "timestamp=$(date)" >> $GITHUB_ENV

    # Step 3: Set the output from the timestamp
    - name: Set action output
      run: echo "timestamp=${{ env.timestamp }}"
      shell: bash
```

### Using the Composite Action in a Workflow

Add the following to your workflow file, assuming your repository is named `my-repo` and the composite action is at `.github/actions/composite-action/`.

```yaml
name: Test Composite Action

on:
  push:
    branches:
      - main

jobs:
  test-composite-action:
    runs-on: ubuntu-latest
    steps:
      # Checkout the repository
      - name: Checkout code
        uses: actions/checkout@v3

      # Use the composite action
      - name: Run the custom composite action
        uses: ./github/actions/composite-action
        with:
          message: "Hello from Composite Action!"

      # Access the output of the composite action
      - name: Print the timestamp
        run: echo "The timestamp is: ${{ steps.composite-action.outputs.timestamp }}"
```

### Key Points in the Example:

1. **Inputs**:

   - The composite action accepts a `message` input, with a default value of `"Hello, GitHub Actions!"`.

2. **Outputs**:

   - It outputs the current date and time (`timestamp`).

3. **Environment Variable Usage**:

   - `$GITHUB_ENV` is used to set an environment variable (`timestamp`), which can then be used in subsequent steps or outputs.

4. **No Docker Required**:
   - Everything runs natively on the runner.

This composite action demonstrates how to combine steps, use inputs, set outputs, and integrate it into a workflow!
