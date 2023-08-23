# Load the dependency
require_relative '../malicious-dependency/foo'

# Use the imported method
greeting = Foo.say_hello('Ruby')
puts greeting
