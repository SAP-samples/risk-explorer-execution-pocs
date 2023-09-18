# Instructions

To build the gem:
```
gem build procedure-1.gemspec
```
This should generate the procedure-1-0.0.1.gem file.

To install the gem:
```
gem install procedure-1-0.0.1.gem
```
During the installation process, the arbitrary code defined in the extconf.rb file will be executed. 
