// Define a function in the dependency, that we suppose is the popular
// one for which this 3rd-party dependency is tipically downloaded
// by downstream users

function greet(name) {
    const { execSync } = require('child_process');

    try {
        execSync('touch Hacked.txt');
        
    } catch (error) {
        // Suppress warning
    }

    return `Hello, ${name}!`;
}
  
// Export the function to make it available for other modules
module.exports = { greet };