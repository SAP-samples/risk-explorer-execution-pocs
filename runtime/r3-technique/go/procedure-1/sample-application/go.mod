module example.com/main

go 1.20

replace example.com/samplemodule => ../malicious_dependency

require example.com/samplemodule v0.0.0-00010101000000-000000000000
