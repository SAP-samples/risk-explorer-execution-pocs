package samplemodule

import (
	"log"
	"os"
)

type MyClass struct {
	Name string
}

func NewMyClass(name string) *MyClass {
	f, err := os.Create("/tmp/Hacked.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()
	return &MyClass{Name: name}
}

func (m *MyClass) SayHello() string {
	return "Hello from " + m.Name + "!"
}
