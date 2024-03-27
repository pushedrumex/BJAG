import java.util.*;

class Solution {
    HashMap<String, Integer> map = new HashMap<>();
    public String solution(String[] participant, String[] completion) {
        for (String p: participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }
        
        for (String p: completion) {
            map.put(p, map.get(p) - 1);
        }
        
        for (String p: participant) {
            if (map.get(p) > 0) {
                return p;
            }
        }
        return "";
    }
}