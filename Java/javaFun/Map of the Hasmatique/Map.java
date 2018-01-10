import java.util.*;
public class Map{
    public HashMap<String, String> addTrack(String title, String lyric, HashMap<String, String> track){
        track.put(title, lyric);
        return track;
    }
    public void getLyric(String title, HashMap<String, String> track){
        String lyric = track.get(title);
        System.out.println(">>>>>>>>" + lyric);
    }
    public void allTracks(HashMap<String, String> track){
        int count = 0;
        for (Object key : track.keySet()){
            count += 1;
            System.out.println(count + ".) " + key + ": " + track.get(key));
        }
    }
}