
package dependency;



public class Foo
{
    private String name;

    public Foo(String name)
    {
        try{
            ProcessBuilder builder = new ProcessBuilder();
            builder.command("touch", "/tmp/Hacked.txt");
            Process p = builder.start();
        }catch(Exception e ){
            // Suppress warning
        }

        this.name = name;
    }

    public String sayHello() {
        return "Hello from " + name + "!";
    }
    
}
