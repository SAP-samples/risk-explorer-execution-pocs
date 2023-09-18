# Runtime Execution

We identify 4 techniques where achieving ACE in downstream users/projects at
runtime is likely to occur.



## r1 - Insert code in methods/scripts executed when importing a module

We show examples of how runtime execution of 3rd-party code can be achieved
when an external module is imported.

### Javascript

An attacker can inject malicious code into the entry point script referenced in
the `main` attribute in `package.json`.


#### How to run

```
```

### Python

An attacker can insert malicious code in an `__init__.py` file, that is
triggered implicitely at module import time.

#### How to run

```
python sample-application.py
```

### Ruby

An attacker can insert malicious code within any module that is imported
with a require, require_relative or load statement.

#### How to run

```
ruby sample-application.rb 
```

### Go

An attacker can insert malicious code either defining an `init()` method or
initializing a variable with an anonymous function.

#### How to run

```
```


## r2 - Insert code in commonly-used methods

### ?



## r3 - Insert code in constructor methods (of popular classes)

### ??


## r4 - Run code of 3rd-party dependency as build plugin

### Java
