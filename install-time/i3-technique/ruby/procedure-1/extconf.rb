require "mkmf"

# Insert your own arbitrary code here
system("echo 'Hello World!'")

# This line is needed to finish the extension configuration without errors,
# as we're not actually creating a native extension here.
create_makefile("")