import java.util.*;
public class SLLTest{
    public static void main(String[] args){
        SLL sll = new SLL();
        sll.add(5);
        sll.add(10);
        sll.add(15);
        sll.add(20);
        sll.printNode();
        sll.remove();
        sll.printNode();
    }
}