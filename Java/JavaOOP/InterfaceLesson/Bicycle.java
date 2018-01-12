class Bicycle implements OperateBicycle{
    private int speed;
    
    public Bicycle(){
        speed = 0;
    }

    public static void staticMethod(){
        OperateBicycle.staticMethod();
    }

    public void speedUp(int increment){
        speed += increment;
    }

    public void applyBrakes(int decrement){
        speed -= decrement;
    }

    public int getSpeed(){
        return speed;
    }
}