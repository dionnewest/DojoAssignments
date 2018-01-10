
public class Human {
	public int strength = 3;
	public int stealth = 3;
	public int intelligence = 3;
	public int health = 100;
	
	public int displayHealth() {
		return health;
	}
	public int displayStealth() {
		return stealth;
	}
	public int displayStrength() {
		return strength;
	}
	public int displayIntelligence() {
		return intelligence;
	}
	public void attack(Human x){
		x.health -= strength;
	}
	public void printStats() {
		System.out.print("Health - " + health);
		System.out.print(" Strength - " + strength);
		System.out.print(" Stealth - " + stealth);
		System.out.println(" Intelligence - " + intelligence);
	}
	
}
