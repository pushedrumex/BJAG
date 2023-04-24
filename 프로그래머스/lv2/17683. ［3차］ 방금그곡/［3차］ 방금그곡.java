import java.util.*;

class Solution {
    int toMinute(String time) {
        String[] temp = time.split(":");
        return Integer.parseInt(temp[0]) * 60 + Integer.parseInt(temp[1]);
    }
    String toLower(String s) {
        List<String> result = new ArrayList<>();
        String[] temp = s.split("");
        
        for (int i=0;i<s.length();i++) {
            if (temp[i].equals("#")) {
                result.set(result.size()-1, result.get(result.size()-1).toLowerCase());
            } else {
                result.add(temp[i]);
            }
        }
        return String.join("", result);
    }
    String getMelody(String lyrics, int t) {
        String result = "";
        int n = lyrics.length();
        int share = t / n, remainder = t % n;
        
        for (int i=0;i<share;i++) {
            result += lyrics;
        }
        result += lyrics.substring(0, remainder);
        return result;
    }
    public String solution(String m, String[] musicinfos) {
        int time = 0, t = 0;
        String answer = "(None)";
        String[] temp;
        String start, end, title, lyrics, melody;
        m = toLower(m);
        for (String musicinfo: musicinfos) {
            temp = musicinfo.split(",");
            start = temp[0];
            end = temp[1];
            title = temp[2];
            lyrics = toLower(temp[3]);
            
            t = toMinute(end) - toMinute(start);
            melody = getMelody(lyrics, t);
            
            if (melody.contains(m) && time < t) {
                time = t;
                answer = title;
            }
        }
        return answer;
    }
}