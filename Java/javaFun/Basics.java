import java.util.*;
public class Basics{
    public void printAll(int num){
        for (int i =1; i <= num; i++){
            System.out.println(i);
        }
    }
    public void printOdd(int num){
        for (int i = 1; i <= num; i++){
            if (i % 2 == 1){
                System.out.println(i);
            }
        }
    }
    public void printSums(int num){
        int sum = 0;
        for (int i = 0; i <= num; i++){
            sum += i;
            System.out.println("New number: " + i + " Sum: " + sum);
        }
    }
    public void iterate(int[] x){
        for (int i = 0; i < x.length; i++){
            System.out.println(x[i]);
        }
    }
    public void max(int[] x){
        int max = x[0];
        for (int i = 1; i < x.length; i++){
            if(x[i] > max){
                max = x[i];
            }
        }
        System.out.println(max);
    }
    public void average(int[] x){
        double sum = 0.0;
        for (int i = 0; i < x.length; i++){
            sum += x[i];
        }
        double avg = sum/x.length;
        System.out.println(avg);
    }
    public void oddArr(int num){
        ArrayList<Integer> y = new ArrayList<Integer>();
        int i = 0;
        while (i <= num){
            y.add(i);
            i++;
        }
        System.out.println(y);
    }
    public void greaterThan(int[] x, int y){
        int count = 0;
        for (int i = 1; i < x.length; i++){
            if(x[i] > y){
                count += 1;
            }
        }
        System.out.println(count);
    }
    public void square(int[] x){
        for (int i = 0; i < x.length; i++){
            x[i] = x[i] * x[i];
        }
        System.out.println(Arrays.toString(x));
    }
    public void noNeg(int[] x){
        for (int i = 0; i < x.length; i++){
            if(x[i] < 0){
                x[i] = 0;
            }
        }
        System.out.println(Arrays.toString(x));
    }
    public void maxMinAvg(int[] x){
        int max = x[0];
        int min = x[0];
        int sum = x[0];
        for(int i = 1; i < x.length; i++){
            if(x[i] > max){
                max = x[i];
            } else if (x[i] < min){
                min = x[i];
            }
            sum += x[i];
        }
        double avg = sum/x.length;
        ArrayList<Object> y = new ArrayList<Object>();
        y.add(max);
        y.add(min);
        y.add(avg);
        System.out.println(y);
    }
    public void shift(int[] x){
        for(int i = 0; i < x.length - 1; i++){
            x[i] = x[i + 1];
        }
        x[x.length - 1] = 0;
        System.out.print(Arrays.toString(x));
    }
}