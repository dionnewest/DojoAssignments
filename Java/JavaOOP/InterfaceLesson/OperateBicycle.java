public interface OperateBicycle{
    double myConstant = 3.0;
    default void sayHello(){
        System.out.println("Hello everybody");
    }
    static void staticMethod(){
        System.out.println("Hello from the static method of the interface");
    }
    void speedUp(int increment);
    void applyBrakes(int decrement);
}