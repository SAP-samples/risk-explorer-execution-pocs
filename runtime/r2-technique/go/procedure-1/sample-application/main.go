package main

import (
	"fmt"

	"example.com/samplemodule"
)

func main() {
	// Use the imported function
	greeting := samplemodule.SayHello("Go")
	fmt.Println(greeting)
}
