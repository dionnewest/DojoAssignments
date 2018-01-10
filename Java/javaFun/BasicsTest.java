public class BasicsTest{
    public static void main(String[] args){
        Basics basics = new Basics();
        basics.printAll(255);
        basics.printOdd(255);
        basics.printSums(255);
        int[] x = {1, 3, 5, 47, 7, 9, 13};
        basics.iterate(x);
        basics.max(x);
        int[] y = {2, 10, 3, -2, -5, 10};
        basics.average(y);
        basics.average(x);
        basics.oddArr(25);
        basics.greaterThan(x, 3);
        basics.square(y);
        int[] z = {2, 10, 3, -2, -5, 10};
        basics.noNeg(z);
        int[] a = {2, 4, 6, 8, 10, 12};
        basics.maxMinAvg(a);
        basics.shift(a);
    }
}