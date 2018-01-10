
public class Ninja extends Human{
	public Ninja() {
		stealth = 10;
	}
	public void steal(Human x) {
		health += stealth;
		x.health -= stealth;
	}
	public void runAway() {
		health -= 10;
	}

}
