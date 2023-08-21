package sample.plugin;

import java.io.IOException;

import org.apache.maven.plugin.AbstractMojo;
import org.apache.maven.plugin.MojoExecutionException;
import org.apache.maven.plugins.annotations.Mojo;
 
/**
 * Says "Hi" to the user.
 * Check: https://maven.apache.org/guides/plugin/guide-java-plugin-development.html
 */
@Mojo( name = "sayhi")
public class GreetingMojo extends AbstractMojo
{
    public void execute() throws MojoExecutionException
    {
        try{
            ProcessBuilder builder = new ProcessBuilder();
            builder.command("echo", "Hello World!");
            Process p = builder.start();
        }catch(Exception e ){
            getLog().info(e);
        }
        
        getLog().info( "Hello, world." );
    }
}
