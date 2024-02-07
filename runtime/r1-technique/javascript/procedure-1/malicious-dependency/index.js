const { execSync } = require('child_process');

try {
    execSync("touch /tmp/Hacked.txt"); // Place any malicious code :)
    
} catch (error) {
    // Suppress warning
}