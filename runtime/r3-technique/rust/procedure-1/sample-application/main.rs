// Import the dependency module
mod malicious_dependency;

use malicious_dependency::MyClass;

fn main() {
    // Instantiate an object
    let my_object = MyClass::new("Rust");
}