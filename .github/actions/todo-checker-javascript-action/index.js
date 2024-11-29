const core = require('@actions/core');
const fs = require('fs');
const path = require('path');

async function getAllFiles(dirPath) {
  let files = await fs.promises.readdir(dirPath, { withFileTypes: true });
  let filePaths = [];
  for (const file of files) {
    const filePath = path.join(dirPath, file.name);
    if (file.isDirectory()) {
      // Recursively scan subdirectories
      filePaths = filePaths.concat(await getAllFiles(filePath));
    } else {
      filePaths.push(filePath);
    }
  }
  return filePaths;
}

async function findTodosInFiles(files) {
  const todoPattern = /\/\/\s*TODO:.*/g; // Pattern to find TODO comments
  let todosFound = false;

  for (const file of files) {
    const content = await fs.promises.readFile(file, 'utf-8');
    const matches = content.match(todoPattern);
    if (matches) {
      todosFound = true;
      core.info(`TODOs found in ${file}:`);
      matches.forEach((todo) => core.info(`  - ${todo.trim()}`));
    }
  }

  if (!todosFound) {
    core.info('No TODO comments found!');
  }
}

async function run() {
  try {
    const srcFolder = core.getInput('src-folder') || './src';
    core.info(`Scanning folder: ${srcFolder}`);

    const allFiles = await getAllFiles(srcFolder);
    core.info(`Found ${allFiles.length} files.`);

    await findTodosInFiles(allFiles);
  } catch (error) {
    core.setFailed(error.message);
  }
}

run();
