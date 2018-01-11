public class PokemonTest{
    public static void main(String args[]) {
        Pokemon pikachu = new Pokemon();
        pikachu.createPokemon("Pikachu", 100, "electric");
        pikachu.pokemonInfo(pikachu);
        Pokemon snorlax = new Pokemon();
        snorlax.createPokemon("Snorlax", 200, "normal");
        snorlax.pokemonInfo(snorlax);
        pikachu.attackPokemon(snorlax);
        // pikachu.speak();
        // snorlax.speak();
        Pokemon.staticMethod();
        
    }
}