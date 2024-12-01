data = [
    (
        "[Create Repository Using Template Repository](./labs/create-repository-using-template-repository.md)", 
        "N/A", 
        "N/A", 
        "N/A"
    ),
    (
        "",  # This row will be a blank row (no ID, no content)
        "",
        "",
        ""
    ),
    (
        "[Manual Workflow](./labs/intro-manual-workflow-lab.md)", 
        "[Start Here](./labs/intro-manual-workflow-starter.md)", 
        "[View Solution](./labs/intro-manual-workflow-solution.md)", 
        "[![Intro - Manual Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-manual-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-manual-workflow.yml)"
    ),
    (
        "[Simple Workflow](./labs/intro-simple-workflow-lab.md)", 
        "[Start Here](./labs/intro-simple-workflow-starter.md)", 
        "[View Solution](./labs/intro-simple-workflow-solution.md)", 
        "[![Intro - Simple Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-simple-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-simple-workflow.yml)"
    ),
    (
        "[Custom Workflow](./labs/intro-custom-workflow-lab.md)", 
        "[Start Here](./labs/intro-custom-workflow-starter.md)", 
        "[View Solution](./labs/intro-custom-workflow-solution.md)", 
        "[![Intro - Custom Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-custom-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-custom-workflow.yml)"
    ),
    (
        "[Scheduled Workflow](./labs/intro-scheduled-workflow-lab.md)", 
        "[Start Here](./labs/intro-scheduled-workflow-starter.md)", 
        "[View Solution](./labs/intro-scheduled-workflow-solution.md)", 
        "[![Intro - Scheduled Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-scheduled-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-scheduled-workflow.yml)"
    ),
    (
        "[YAML Syntax](./labs/intro-yaml-syntax-lab.md)", 
        "[Start Here](./labs/intro-yaml-syntax-starter.md)", 
        "[View Solution](./labs/intro-yaml-syntax-solution.md)", 
        "[![Intro - YAML Syntax](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-yaml-syntax.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-yaml-syntax.yml)"
    ),
    (
        "",  # This row will be a blank row (no ID, no content)
        "",
        "",
        ""
    ),
    (
        "[Disabling a Workflow](./labs/disabling-a-workflow-lab.md)", 
        "N/A", 
        "N/A", 
        "N/A"
    ),
    (
        "[Displaying Workflow Status Badge](./labs/displaying-workflow-status-badge-lab.md)", 
        "N/A", 
        "N/A", 
        "N/A"
    ),
    (
        "",  # This row will be a blank row (no ID, no content)
        "",
        "",
        ""
    ),
    (
        "[Environment Variables and Secrets](./labs/env-var-secrets-lab.md)", 
        "[Start Here](./labs/env-var-secrets-starter.md)", 
        "[View Solution](./labs/env-var-secrets-solution.md)", 
        "[![Environment Variables and Secrets](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-secrets.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-secrets.yml)"
    ),
    (
        "[Environment Variables Scope](./labs/env-var-scope-lab.md)", 
        "[Start Here](./labs/env-var-scope-starter.md)", 
        "[View Solution](./labs/env-var-scope-solution.md)", 
        "[![Environment Variables Scope](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-scope.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-scope.yml)"
    ),
    (
        "[Environment Variables List](./labs/env-var-list-lab.md)", 
        "[Start Here](./labs/env-var-list-starter.md)", 
        "[View Solution](./labs/env-var-list-solution.md)", 
        "[![Environment Variables List](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-list.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-list.yml)"
    ),
    (
        "",  # This row will be a blank row (no ID, no content)
        "",
        "",
        ""
    ),
        
]

# Generate the markdown table header with renamed 'Status' column
markdown_table = "| ID  | Lab                                                | Starter File                                     | Solution                                      | Workflow Status                                                                                      |\n"
markdown_table += "|-----|----------------------------------------------------|-------------------------------------------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------|\n"

# Initialize ID counter
current_id = 1

# Generate the rows with auto-incrementing IDs
for lab, starter_file, solution, status in data:
    # If the row is empty, leave the ID field blank and don't increment ID
    if lab == "" and starter_file == "" and solution == "" and status == "":
        markdown_table += "|     |            |            |            |            |\n"  # Blank row with empty columns
    else:
        markdown_table += f"| {current_id}   | {lab:<50} | {starter_file:<48} | {solution:<48} | {status:<100} |\n"
        current_id += 1  # Increment the ID only for non-blank rows

# File path where the markdown table will be saved
file_path = "workshop-labs.md"

# Save the generated table to the markdown file
with open(file_path, "w") as file:
    file.write(markdown_table)

print(f"Markdown table saved to {file_path}")
