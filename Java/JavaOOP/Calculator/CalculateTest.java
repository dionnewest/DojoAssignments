public class CalculateTest{
    public static void main(String args[]){
        Calculate addition = new Calculate(4.55, "+", 5.45);
        addition.performOperation();
        Calculate multiplication = new Calculate(3.5, "*", 2);
        multiplication.performOperation();
        Calculate subtraction = new Calculate(15.0, "-", 7.5);
        subtraction.performOperation();
        Calculate division = new Calculate(20.7, "/", .5);
        division.performOperation();
    }
}