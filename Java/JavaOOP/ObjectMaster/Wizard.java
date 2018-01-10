
public class Wizard extends Human{
	
	public Wizard() {
		health = 50;
		intelligence = 8;
	}
	public void heal(Human x) {
		x.health += intelligence;
	}
	public void fireball(Human x) {
		x.health -= intelligence*3;
	}
}
