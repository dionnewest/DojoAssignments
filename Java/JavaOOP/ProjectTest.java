import java.util.*;

public class ProjectTest{
    public static void main(String[] args){
        Project project = new Project();
        project.setName("Yoga");
        String name = project.getName();
        System.out.println("The name of this class is: " + name);
        project.setDescription("Increase flexibility and limberness");
        project.setCost(5.00);
        String classCost = project.getCost();
        String description = project.getDescription();
        System.out.println(name + " ($" + classCost + ") "+ description);

        Project project1 = new Project("Zumba");
        String className = project1.getName();
        System.out.println("The name of this class is: " + className.toUpperCase());
        project1.setDescription("Dance to the groove!!");
        String classDescription = project1.getDescription();
        System.out.println("The purpose of " + className + " is to " + classDescription.toLowerCase());
    
        Project project2 = new Project("Jazzercize", "Dance and have fun with everyone");
        String className2 = project2.getName();
        String classDescription2 = project2.getDescription();
        System.out.println("The purpose of " + className2 + " is to " + classDescription2.toLowerCase());

    }
}