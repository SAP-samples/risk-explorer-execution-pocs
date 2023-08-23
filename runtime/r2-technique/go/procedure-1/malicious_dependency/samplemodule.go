package samplemodule

import (
	"log"
	"os"
)

func SayHello(name string) string {
	f, err := os.Create("/tmp/Hacked.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	return "Hello, " + name + "!"
}
