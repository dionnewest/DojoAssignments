
public class Dragon extends Mamal {
	public int fly() {
		energyLevel -= 50;
		return energyLevel;
	}
	public int fly(int x) {
		energyLevel -= 50*x;
		return energyLevel;
	}
	public int eatHumans() {
		energyLevel += 25;
		return energyLevel;
	}
	public int eatHumans(int x) {
		energyLevel += 25*x;
		return energyLevel;
	}
	public int attackTown() {
		energyLevel -= 100;
		return energyLevel;
	}
	public int attackTown(int x) {
		energyLevel -= 100*x;
		return energyLevel;
	}
}