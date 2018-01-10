public class StringManipulatorTest {
    public static void main (String[] args){
        StringManipulator manipulator = new StringManipulator();
        manipulator.trimAndConcat(" Dionne "," West ");
        char letter = 'o';
        manipulator.getIndexOrNull("Coding", letter);
        manipulator.getIndexOrNull("Hello World", letter);
        manipulator.getIndexOrNull("Hi", letter);
        String word = "Hello";
        String subString = "llo";
        String notSubString = "world";
        manipulator.getIndexOrNull(word, subString);
        manipulator.getIndexOrNull(word, notSubString);
        manipulator.concatSubstring("Hello", 1, 2, "world");
    }
}