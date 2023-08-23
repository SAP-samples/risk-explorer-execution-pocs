package application;

import dependency.Foo;

public class Main {
    public static void main(String[] args) {
        // Use the imported method
        String greeting = Foo.sayHello("Java");
        System.out.println(greeting);
    }
}