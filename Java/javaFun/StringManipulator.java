public class StringManipulator {
    public void trimAndConcat(String a, String b){
        a = a.trim();
        b = b.trim();
        System.out.println(a+b);
    }
    public void getIndexOrNull(String word, char x){
        if(word.indexOf(x)>0){
            System.out.println(word.indexOf(x));
        } else {
            System.out.println("null");
        }
    }
    public void getIndexOrNull(String word, String subword){
        if(word.indexOf(subword)>0){
            System.out.println(word.indexOf(subword));
        } else {
            System.out.println("null");
        }
    }
    public void concatSubstring(String mainWord, int a, int b, String word){
        mainWord = mainWord.substring(a, b);
        System.out.println(mainWord + word);
    }
}