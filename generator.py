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
        "[Manual Workflow](./labs/intro-manual-workflow.md)", 
        "[Start Here](./workflow-starter-files/intro-manual-workflow.md)", 
        "[View Solution](./workflow-solution-files/intro-manual-workflow.md)", 
        "[![Intro - Manual Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-manual-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-manual-workflow.yml)"
    ),
    (
        "[Simple Workflow](./labs/intro-simple-workflow.md)", 
        "[Start Here](./workflow-starter-files/intro-simple-workflow.md)", 
        "[View Solution](./workflow-solution-files/intro-simple-workflow.md)", 
        "[![Intro - Simple Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-simple-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-simple-workflow.yml)"
    ),
    (
        "[Custom Workflow](./labs/intro-custom-workflow.md)", 
        "[Start Here](./workflow-starter-files/intro-custom-workflow.md)", 
        "[View Solution](./workflow-solution-files/intro-custom-workflow.md)", 
        "[![Intro - Custom Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-custom-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-custom-workflow.yml)"
    ),
    (
        "[Scheduled Workflow](./labs/intro-scheduled-workflow.md)", 
        "[Start Here](./workflow-starter-files/intro-scheduled-workflow.md)", 
        "[View Solution](./workflow-solution-files/intro-scheduled-workflow.md)", 
        "[![Intro - Scheduled Workflow](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-scheduled-workflow.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-scheduled-workflow.yml)"
    ),
    (
        "[YAML Syntax](./labs/intro-yaml-syntax.md)", 
        "[Start Here](./workflow-starter-files/intro-yaml-syntax.md)", 
        "[View Solution](./workflow-solution-files/intro-yaml-syntax.md)", 
        "[![Intro - YAML Syntax](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-yaml-syntax.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/intro-yaml-syntax.yml)"
    ),
    (
        "",  # This row will be a blank row (no ID, no content)
        "",
        "",
        ""
    ),
    (
        "[Environment Variables and Secrets](./labs/env-var-secrets.md)", 
        "[Start Here](./workflow-starter-files/env-var-secrets.md)", 
        "[View Solution](./workflow-solution-files/env-var-secrets.md)", 
        "[![Environment Variables and Secrets](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-secrets.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-secrets.yml)"
    ),
    (
        "[Environment Variables Scope](./labs/env-var-scope.md)", 
        "[Start Here](./workflow-starter-files/env-var-scope.md)", 
        "[View Solution](./workflow-solution-files/env-var-scope.md)", 
        "[![Environment Variables Scope](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-scope.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-scope.yml)"
    ),
    (
        "[Environment Variables List](./labs/env-var-list.md)", 
        "[Start Here](./workflow-starter-files/env-var-list.md)", 
        "[View Solution](./workflow-solution-files/env-var-list.md)", 
        "[![Environment Variables List](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-list.yml/badge.svg)](https://github.com/prasadhonrao/github-actions-workshop/actions/workflows/env-var-list.yml)"
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
