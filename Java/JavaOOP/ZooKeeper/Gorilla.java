
public class Gorilla extends Mamal {
	public int throwSomething() {
		energyLevel -= 5;
		return energyLevel;
	}
	public int eatBananas() {
		energyLevel += 10;
		return energyLevel;
	}
	public int climb() {
		energyLevel -= 10;
		return energyLevel;
	}
}
