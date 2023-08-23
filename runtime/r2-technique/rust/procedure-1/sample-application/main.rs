// Import the dependency module
mod malicious_dependency;

use malicious_dependency::foo;

fn main() {
    // Use the imported function
    let greeting = foo::say_hello("Rust");
    println!("{}", greeting);
}