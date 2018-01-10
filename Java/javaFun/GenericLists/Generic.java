import java.util.*;
public class Generic{
    public void convert(ArrayList<Object> arr){
        ArrayList<Integer> newList = new ArrayList<Integer>();
        for (int i = 0; i < arr.size(); i++){
            newList.add((Integer) arr.get(i));
        }
        System.out.println(newList);
    }
}