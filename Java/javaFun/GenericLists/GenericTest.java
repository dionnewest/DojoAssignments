import java.util.*;
public class GenericTest{
    public static void main(String[] args){
        Generic generic = new Generic();
        ArrayList<Object> myList = new ArrayList<Object>();
        myList.add("13");
        myList.add("hello world");
        myList.add(48);
        myList.add("Goodbye World");
        System.out.println(myList);
        generic.convert(myList);
    }
}