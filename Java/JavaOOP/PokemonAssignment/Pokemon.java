public class Pokemon extends Pokedex{
    public String name;
    public int health;
    public String type;
    public static int pokemonCount = 0;

    public Pokemon(){
        pokemonCount += 1;
    }

    public static void staticMethod(){
        OperatePokemon.staticMethod();
    }
    
    public void createPokemon(String a, int b, String c){
        pokemonCount +=1;
        name = a;
        health = b;
        type = c;
    }

    public void attackPokemon(Pokemon p){
        p.health -= 10;
        System.out.println(p.name + "'s health is now " + p.health);
    }

    // public void pokemonInfo(Pokemon p){
    //     System.out.println("All info for " + p.name + ":");
    //     System.out.println("Health: " + p.health);
    //     System.out.println("Type: " + p.type);
    // }

    public void setName(String a){
        name = a;
    }

    public String getName(){
        return name;
    }

    public void setHealth(int a){
        health = a;
    }

    public int getHealth(){
        return health;
    }

    public void setType(String a){
        type = a;
    }

    public String getType(){
        return type;
    }

}