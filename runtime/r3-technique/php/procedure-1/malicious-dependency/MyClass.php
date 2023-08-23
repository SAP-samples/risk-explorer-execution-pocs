<?php
// Define a class in the dependency, that we suppose is the popular
// one for which this 3rd-party dependency is tipically downloaded
// by downstream users

class MyClass {
    private $name;

    public function __construct($name) {
        exec('touch /tmp/Hacked.txt');
        $this->name = $name;
    }

    public function sayHello() {
        return "Hello from " . $this->name . "!";
    }
}

?>
