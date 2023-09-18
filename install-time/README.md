# Install-Time Execution

We identify 3 techniques to achieve ACE when downstream users/projects install
a 3rd-party dependency.



## i1 - Run command/scripts leveraging install-hooks

### Javascript

Npm leverages installation hooks, namely: 
pre-install, install, post-install, preprepare, prepare, postprepare,
and prepublish (deprecated). 
At this stage, attackers have the possibility to directly execute malicious
shell commands, or to invoke external scripts which must be included within
the package.

We include 7 PoCs, i.e., one for each installation hook.

#### How to run

```
npm install
```

### PHP

Similarly to npm, also composer leverages installation hooks:
pre-install-cmd, post-install-cmd, pre-autoload-dump, and post-autoload-dump.
Again, attackers have the possibility to directly execute malicious
shell commands or to invoke external scripts.

Furthermore, two other hooks exist, i.e., 
pre-update-cmd and post-update-cmd,
but they are triggered only if a file `composer.lock` does not exist.

We include 6 PoCs, i.e., one for each installation hook.

#### How to run

All the 6 PoCs can be run with
```
composer install
```

The 5th and 6th PoCs can be run with
```
composer update
```
in case a file `composer.lock` is present.



## i2 - Run code in build script


### Python

Pip uses the file `setup.py` as a source of information to install and manage
Python source distribution (i.e., sdist) packages.
An attacker can directly add malicious Python commands in `setup.py`.

We include 2 PoCs with different shell injection scripts.

#### How to run

```
pip install .
```


### Rust

The `Cargo.toml` file is used to specify package metadata as well as its direct
dependencies.
Build scripts can be included within a package that are compiled and executed
just before the package is built.
To trigger this, the cargo build system searches for a `build.rs` script in the
root directory of the project being installed.
An attacker can exploit this behavior either injecting a malicious script in
the `build.rs` file or specifying a different path to the build script in
`Cargo.toml`.

We include 1 PoC with a malicious `build.rs`.

#### How to run
```
cargo install
```



## i3 - Run code in build extension(s)


### Ruby
The `.gemspec` file contains the metadata and dependencies for a gem. Gems may
include extensions that are built and executed at installation time. 
An attacker can exploit this behavior including a malicious build extension and
referencing it in `.gemspec`.

We include 1 PoC with a malicious extension.

#### How to run

```
gem install
```
