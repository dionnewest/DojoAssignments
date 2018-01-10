public class HumanTest {
	public static void main(String args[]) {
		Wizard wizard = new Wizard();
//		System.out.println("Wizard Stats: Health- " + wizard.displayHealth() + ", Intelligence " + wizard.displayIntelligence());
		Samurai samurai = new Samurai();
//		System.out.println("Samurai Stats: Health- " + samurai.displayHealth());
		Ninja ninja = new Ninja();
//		System.out.println("Ninja Stats: Health- " + ninja.displayHealth() + ", Stealth " + ninja.displayStealth());
		//WIZARD ATTACKING NINJA
		wizard.attack(ninja);
		wizard.fireball(ninja);
		wizard.heal(ninja);
		ninja.printStats();
		
		//SAMURAI ATTACKING WIZARD
		samurai.attack(wizard);
		samurai.deathBlow(wizard);
		System.out.println(samurai.displayHealth());
		samurai.meditate();
		System.out.println(samurai.displayHealth());
		wizard.printStats();
		
		//NINJA ATTACKING SAMURAI
		ninja.attack(samurai);
		ninja.steal(samurai);
		ninja.runAway();
		ninja.runAway();
		System.out.println(ninja.displayHealth());
		samurai.printStats();
		System.out.println(samurai.howMany());
	}
}