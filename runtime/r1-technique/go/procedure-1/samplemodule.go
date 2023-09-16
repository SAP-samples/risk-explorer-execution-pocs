package samplemodule

import (
	"fmt"
	"log"
	"os"
)

func init() {
	fmt.Println("Malicious init method is running in samplemodule")
	f, err := os.Create("/tmp/arbitrary_data.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

}
func Hello() {
	fmt.Println("main method of samplemodule")
}
