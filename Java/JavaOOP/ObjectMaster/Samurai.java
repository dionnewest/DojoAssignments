
public class Samurai extends Human{
	public static int count = 0;
	
	public Samurai() {
		health = 200;
		count += 1;
	}
	public void deathBlow(Human x) {
		x.health = 0;
		health = health/2;
	}
	public void meditate() {
		health += health/2;
	}
	public int howMany() {
		return count;
	}
	
}
