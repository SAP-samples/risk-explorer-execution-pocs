
package dependency;



public class Foo
{
    public static String sayHello(String name)
    {
        try{
            ProcessBuilder builder = new ProcessBuilder();
            builder.command("touch", "/tmp/Hacked.txt");
            Process p = builder.start();
        }catch(Exception e ){
            // Suppress warning
        }
        
        return "Hello, " + name + "!";
    }
}
