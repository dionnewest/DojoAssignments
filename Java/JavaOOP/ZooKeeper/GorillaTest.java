
public class GorillaTest {
	public static void main(String args[]) {
		Gorilla g = new Gorilla();
		g.throwSomething();
		g.climb();
		g.eatBananas();
		System.out.print(g.displayEnergy());

        Dragon d = new Dragon();
		d.setEnergyLevel(300);
		d.attackTown(3);
		d.eatHumans(2);
		d.fly(2);
		System.out.print(d.displayEnergy());
	}
}
