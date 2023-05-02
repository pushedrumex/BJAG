import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        
        for (String p: participant) {
            map.put(p, map.getOrDefault(p, 0)+1);
        }
        
        for (String c: completion) {
            map.put(c, map.get(c)-1);
        }
        
        for (String c: map.keySet()) {
            if (map.get(c) > 0) {
                return c;
            }
        }
        return null;
    }
}