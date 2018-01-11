public interface OperatePokemon{
    // default void speak(){
    //     System.out.println("Hi! My name is " + this.name);
    // }

    static void staticMethod(){
        System.out.println("All pokemon are awesome");
    }

    void createPokemon(String name, int health, String type);
    void attackPokemon(Pokemon pokemon);
    void pokemonInfo(Pokemon pokemon);
}