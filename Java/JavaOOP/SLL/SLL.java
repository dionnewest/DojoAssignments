import java.util.*;
public class SLL{
    private Node head;

    public SLL(){
        head = null;
    }

    public void add(Integer a){
        System.out.println("The head is: " + head);
        Node newNode = new Node(a);
        if(head == null){
            head = newNode;
        } else {
            Node runner = head;
            while (runner.next != null){
                runner = runner.next;
            }
            runner.next = newNode;
        }
    }
    public void printNode(){
        Node runner = head;
        while (runner.next != null){
            System.out.println(runner.value);
            runner = runner.next;
        }
        if (runner.next == null){
            System.out.println(runner.value);
            runner = runner.next;
        }
    }    
    public void remove(){
        Node runner = head;
        while (runner.next.next != null){
            runner = runner.next;
        }
        runner.next = null;
        // System.out.println(runner.value);
    }


}