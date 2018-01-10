import java.util.*;

public class Project{
    private String name;
    private String description;
    private double cost;

    public Project (){
        name = "";
        description = "";
    }
    public Project(String a){
        name = a;
        description = "";
    }
    public Project(String a, String b){
        name = a;
        description = b;
    }
    public Project(double c){
        cost = c;
    }
    //set & get names
    public void setName(String a){
        name = a;
        System.out.println(name);
    }
    public String getName(){
        return name;
    }
    //set & get descriptions
    public void setDescription(String b){
        description = b;
        System.out.println(description);
    }
    public String getDescription(){
        return description;
    }
    public void setCost(double c){
        cost = c;
        System.out.println(cost);
    }
    public String getCost(){
        String classCost = Double.toString(cost);
        return classCost;
    }
    
}
