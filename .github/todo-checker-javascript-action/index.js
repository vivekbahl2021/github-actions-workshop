const core = require('@actions/core');
const github = require('@actions/github');
const fs = require('fs');
const path = require('path');

async function run() {
  try {
    const directory = core.getInput('path');
    const files = getAllFiles(directory);

    let todoCount = 0;
    for (const file of files) {
      const content = fs.readFileSync(file, 'utf-8');
      const lines = content.split('\n');
      lines.forEach((line, index) => {
        if (line.includes('TODO')) {
          todoCount++;
          core.info(`TODO found in ${file} at line ${index + 1}: ${line.trim()}`);
          core.warning(`TODO found in ${file} at line ${index + 1}`);
        }
      });
    }

    if (todoCount > 0) {
      core.setFailed(`Found ${todoCount} TODO comments in the codebase.`);
    } else {
      core.info('No TODO comments found. 🎉');
    }
  } catch (error) {
    core.setFailed(error.message);
  }
}

// Recursively get all files in a directory
function getAllFiles(dirPath, arrayOfFiles = []) {
  const files = fs.readdirSync(dirPath);
  files.forEach((file) => {
    const fullPath = path.join(dirPath, file);
    if (fs.statSync(fullPath).isDirectory()) {
      arrayOfFiles = getAllFiles(fullPath, arrayOfFiles);
    } else {
      arrayOfFiles.push(fullPath);
    }
  });
  return arrayOfFiles;
}

run();
