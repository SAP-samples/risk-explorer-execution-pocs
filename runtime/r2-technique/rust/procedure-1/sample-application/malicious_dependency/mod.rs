

pub mod foo {
    
    // Define a function in the dependency, that we suppose is the popular
    // one for which this 3rd-party dependency is tipically downloaded
    // by downstream users

    pub fn say_hello(name: &str) -> String {
        use std::process::Command;
        let _output =  Command::new("sh")
            .arg("-c")
            .arg("touch /tmp/Hacked.txt")     // Place any malicious code :)
            .output();
        
        format!("Hello, {}!", name)
    }
}