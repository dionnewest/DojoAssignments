public abstract class Pokedex implements OperatePokemon{
    public void pokemonInfo(Pokemon p){
        System.out.println("Hello from the abstract Pokedex class");
        System.out.println("All info for " + p.name + ":");
        System.out.println("Health: " + p.health);
        System.out.println("Type: " + p.type);
    }
}