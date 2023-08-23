
# Define a class in the dependency, that we suppose is the popular
# one for which this 3rd-party dependency is tipically downloaded
# by downstream users
class MyClass
  def initialize(name)
    system('touch /tmp/Hacked.txt')
    @name = name
  end

  def say_hello
    "Hello from #{@name}!"
  end
end
