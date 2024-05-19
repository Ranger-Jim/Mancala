const fs = require("fs");
const path = require("path");

// Function to fix markdown files
function fixMarkdown(filePath) {
  // Read the content of the file
  fs.readFile(filePath, "utf8", (err, data) => {
    if (err) {
      console.error(`Error reading file: ${filePath}`);
      return;
    }

    // Replace '{{' with '{\{'
    data = data.replace(/{{/g, "{\\{");

    // Replace '}}' with '}\}'
    data = data.replace(/}}/g, "}\\}");

    // Write the updated content back to the file
    fs.writeFile(filePath, data, "utf8", (err) => {
      if (err) {
        console.error(`Error writing to file: ${filePath}`);
        return;
      }
      console.log(`File updated: ${filePath}`);
    });
  });
}

// Function to process a directory recursively
function processDirectory(directoryPath) {
  // Read the contents of the directory
  fs.readdir(directoryPath, (err, files) => {
    if (err) {
      console.error(`Error reading directory: ${directoryPath}`);
      return;
    }

    // Iterate through each file in the directory
    files.forEach((file) => {
      // Get the full path of the file
      const filePath = path.join(directoryPath, file);

      // Check if the file is a directory
      fs.stat(filePath, (err, stats) => {
        if (err) {
          console.error(`Error reading file stats: ${filePath}`);
          return;
        }

        // If the file is a directory, recursively process it
        if (stats.isDirectory()) {
          processDirectory(filePath);
        } else {
          // If the file is a markdown file, fix it
          if (file.endsWith(".md")) {
            fixMarkdown(filePath);
          }
        }
      });
    });
  });
}

// Start processing from the root directory
const rootDir = "./";
processDirectory(rootDir);
