<?php

// Include the malicious dependency file
require_once('../malicious-dependency/foo.php');

// Use the function from the dependency
$greeting = sayHello('PHP');
echo $greeting;
?>
