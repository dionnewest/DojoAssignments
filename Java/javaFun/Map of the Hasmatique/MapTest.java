import java.util.*;

public class MapTest{
    public static void main(String[] args){
        Map map = new Map();
        HashMap<String, String> album = new HashMap<>();
        map.addTrack("Happy", "Clap along if you feel like a room without a roof.", album);
        map.addTrack("Sad", "I'm so sad, so sad.", album);
        map.addTrack("Content", "Sway unemotionally.", album);
        map.addTrack("Devestated", "I'm in a pit of despair.", album);
        System.out.println("Album: " + album);
        map.getLyric("Happy", album);
        map.getLyric("Sad", album);
        map.allTracks(album);
    }
}