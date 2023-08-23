module Foo
    # Define a function in the dependency, that we suppose is the popular
    # one for which this 3rd-party dependency is tipically downloaded
    # by downstream users
    def self.say_hello(name)
      system('touch Hacked.txt')
      "Hello, #{name}!"
    end
  end