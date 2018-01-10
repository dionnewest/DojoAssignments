public class PuzzlingTest{
    public static void main(String[] args){
        Puzzling puzzling = new Puzzling();
        // int[] x = {1, 3, 5, 47, 7, 9, 13};
        // puzzling.sums(x, 7);
        // String[] y = {"Nancy", "Jinichi", "Fujibayashi", "Momochi", "Ishikawa", "Oscar"};
        // puzzling.names(y, 5);
        // char[] alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        // puzzling.alphabet(alphabet);
        puzzling.randomNum(55, 100, 10);
        puzzling.randomNumInOrder(55, 100, 10);
    }
}