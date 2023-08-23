// Import the dependency module
const myDependency = require('../malicious-dependency/samplemodule');

// Use the imported (malicious) function from the dependency
const greeting = myDependency.greet('Alice');
console.log(greeting);