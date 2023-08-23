# Define a class in the dependency, that we suppose is the popular
# one for which this 3rd-party dependency is tipically downloaded
# by downstream users

class MyClass:
    def __init__(self,name):
        import os; os.system("touch Hacked.txt")     # Place any malicious code :)
        self.name = name

    def say_hello(self):
        
        return f"Hello, {self.name}!"