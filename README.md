# Risk Explorer - Execution Proof-of-Concepts
<!-- Please include descriptive title -->

<!--- Register repository https://api.reuse.software/register, then add REUSE badge:
[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/REPO-NAME)](https://api.reuse.software/info/github.com/SAP-samples/REPO-NAME)
-->
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE.txt)
[![REUSE status](https://api.reuse.software/badge/github.com/SAP-samples/risk-explorer-execution-pocs)](https://api.reuse.software/info/github.com/SAP-samples/risk-explorer-execution-pocs)



## Description
<!-- Please include SEO-friendly description -->

To conduct a successful OSS supply chain attack, an attacker is required to:

1. Create a malicious package that is available to downstream users.
2. Get the victim to install/download the malicious artifact.
3. Get the victim to run the malicious code.

In our previous work, we presented a [taxonomy](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a167/1He7XSTyRKE) that describes how attackers can inject malicious code into OSS components (for an interactive view, you can visit the [Risk Explorer](https://sap.github.io/risk-explorer-for-software-supply-chains/)). 
This taxonomy comprehensively covers the first two requirements listed above.

In this project, we enhance this description by providing runnable examples for multiple ecosystems, explaining *how a 3rd-party dependency can trigger execution in downstream projects*, ultimately resulting in OSS supply chain attacks. 
For further details, you can refer to our paper (description to be added later).

In general, 3rd-party dependencies can achieve Arbitrary Code Execution (ACE) in two stages of their lifecycle:

- **Install time**: When downstream users/projects install a 3rd-party dependency using popular package managers (e.g., npm, composer, pip).
- **Runtime**: When downstream users/projects actually use (and invoke) the code of the 3rd-party dependency.

This project covers the following programming languages and their respective (reference) package managers:

- Python (pip)
- JavaScript (npm)
- Ruby (gem)
- PHP (composer)
- Rust (cargo)
- Go (go)
- Java (mvn)

This release aims to support fellow researchers in devising protective measures against such threats. We believe it may also assist penetration testers in evaluating whether the offensive techniques explored in this work can be replicated within their organizations.


### Project Structure

The project is structured as follows:

- **`install-time`**: This folder contains examples related to the "tactic" of achieving Arbitrary Code Execution during the installation of a 3rd-party dependency. It is further divided into subfolders, each representing different techniques explained in the paper:
  - **`i1-technique`** (*Run command/scripts leveraging install-hooks*): This subfolder contains "practices" (i.e., implementations) for the following programming languages:
    - `javascript` (npm): Includes 7 examples
    - `php` (composer): Includes 6 examples
  - **`i2-technique`** (*Run code in build script*): 
    - `python` (pip): Includes 2 examples
    - `rust` (cargo): Includes 1 example
  - **`i3-technique`** (*Run code in build extension(s)*):
    - `ruby` (gem): Includes 1 example

- **`runtime`**: This folder contains examples related to the "tactic" of achieving Arbitrary Code Execution during the runtime of a 3rd-party dependency. It is also divided into subfolders, each representing different techniques explained in the paper:
  - **`r1-technique`** (*Insert code in methods/scripts executed when importing a module*): This contains "practices" (i.e., implementations) for the following programming languages:
    - `javascript`: Includes 1 example
    - `python`: Includes 1 example
    - `ruby`: Includes 1 example
    - `go`: Includes 1 example
  - **`r2-technique`** (*Insert code in commonly-used methods*): This contains "practices" (i.e., implementations) for the following programming languages:
    - `go`: Includes 1 example
    - `java`: Includes 1 example
    - `javascript`: Includes 1 example
    - `php`: Includes 1 example
    - `python`: Includes 1 example
    - `ruby`: Includes 1 example
    - `rust`: Includes 1 example
  - **`r3-technique`** (*Insert code in constructor methods (of popular classes)*): This contains "practices" (i.e., implementations) for the following programming languages:
    - `go`: Includes 1 example
    - `java`: Includes 1 example
    - `javascript`: Includes 1 example
    - `php`: Includes 1 example
    - `python`: Includes 1 example
    - `ruby`: Includes 1 example
    - `rust`: Includes 1 example
  - **`r4-technique`** (*Run code of 3rd-party dependency as build plugin*): As this technique is mostly specific to Java, there is only one subfolder:
    - `java`: Includes 1 example




## Requirements and Usage

To execute the provided examples, it is essential to ensure that your system has the following programming languages and their associated package managers installed:

- Python with `pip`
- JavaScript with `npm`
- Ruby with `gem`
- PHP with `composer`
- Rust with `cargo`
- Go with `go`
- Java with `mvn`



## How to obtain support
[Create an issue](https://github.com/SAP-samples/<repository-name>/issues) in this repository if you find a bug or have questions about the content.
 
For additional support, [ask a question in SAP Community](https://answers.sap.com/questions/ask.html).

## Contributing
If you wish to contribute code, offer fixes or improvements, please send a pull request. Due to legal reasons, contributors will be asked to accept a DCO when they create the first pull request to this project. This happens in an automated fashion during the submission process. SAP uses [the standard DCO text of the Linux Foundation](https://developercertificate.org/).

## License
Copyright (c) 2023 SAP SE or an SAP affiliate company. All rights reserved. This project is licensed under the Apache Software License, version 2.0 except as noted otherwise in the [LICENSE](LICENSE) file.
