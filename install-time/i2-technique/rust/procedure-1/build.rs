// fn main() {
//     println!("Executing code at install time!");

//     // Add your install-time code here

//     // For example, let's create a file during installation
//     std::fs::write("Hacked_rust.txt", "This file was created during installation")
//         .expect("Failed to create file");
// }

use std::process::Command;

fn main() {
    let output =  Command::new("sh")
            .arg("-c")
            .arg("echo 'Hello World!'")     // Place any malicious code :)
            .output();
       
}
