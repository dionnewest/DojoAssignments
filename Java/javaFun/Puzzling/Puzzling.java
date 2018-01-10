import java.util.*;
import java.util.concurrent.ThreadLocalRandom;
public class Puzzling{
    public void sums(int[] x, int y){
        int sum = x[0];
        ArrayList<Integer> z = new ArrayList<Integer>();
        for (int i = 1; i < x.length; i++){
            sum += x[i];
            if(x[i] > y){
                z.add(x[i]);
            }
        }
        System.out.println("The sum is: " + sum + ", and the numbers greater than " + y + " are: " + z);
    }
    public void names(String[] x, int y){
        int index;
        String temp;
        Random random = new Random();
        for (int i = x.length-1; i >0; i--){
            index = random.nextInt(i+1);
            temp = x[index];
            x[index] = x[i];
            x[i] = temp;
        }
        ArrayList<String> z = new ArrayList<String>();
        for (int i = 0; i < x.length; i++){
            if(x[i].length() <= y){
                z.add(x[i]);
            }
        }
        System.out.println(Arrays.toString(x) + " " + z);
        
    }
    public void alphabet(char[] x){
        int index;
        char temp;
        Random random = new Random();
        for (int i = x.length-1; i >0; i--){
            index = random.nextInt(i+1);
            temp = x[index];
            x[index] = x[i];
            x[i] = temp;
        }
        System.out.println(">>>>>>>" + x[x.length - 1]);
        if (x[0] == 'a' || x[0] == 'e' || x[0] == 'i' || x[0] == 'o' || x[0] == 'u'){
            System.out.println("The first letter in the shuffled alphabet is: " + x[0] + ", a vowel.");
        } else {
            System.out.println(">>>>>>>" + x[0]);
        }
        System.out.println(Arrays.toString(x));
    }
    public void randomNum(int min, int max, int count){
        ArrayList<Integer> x = new ArrayList<Integer>();
        for (int i = min; i <= max; i++){
            x.add(i);
        }
        Integer[] y = x.toArray(new Integer[x.size()]);
        // System.out.println(Arrays.toString(y));
        int index;
        int temp;
        Random random = new Random();
        for (int i = y.length-1; i > 0; i--){
            index = random.nextInt(i+1);
            temp = y[index];
            y[index] = y[i];
            y[i] = temp;
        }
        // System.out.println(Arrays.toString(y));
        ArrayList<Integer> z = new ArrayList<Integer>();
        for (int i = 0; i < count; i++){
            z.add(y[i]);
        }
        System.out.println(z);
    }
    public void randomNumInOrder(int min, int max, int count){
        ArrayList<Integer> x = new ArrayList<Integer>();
        for (int i = min; i <= max; i++){
            x.add(i);
        }
        Integer[] y = x.toArray(new Integer[x.size()]);
        // System.out.println(Arrays.toString(y));
        int index;
        int temp;
        Random random = new Random();
        for (int i = y.length-1; i > 0; i--){
            index = random.nextInt(i+1);
            temp = y[index];
            y[index] = y[i];
            y[i] = temp;
        }
        System.out.println(Arrays.toString(y));
        ArrayList<Integer> z = new ArrayList<Integer>();
        for (int i = 0; i < count; i++){
            z.add(y[i]);
        }
        Integer[] a = z.toArray(new Integer[z.size()]);
        Arrays.sort(a);
        System.out.println(Arrays.toString(a));
    }
}