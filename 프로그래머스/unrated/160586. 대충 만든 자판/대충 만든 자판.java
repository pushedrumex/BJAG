import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        int cnt;
        Map<Character, Integer> map = new HashMap<>();
        
        for (String keylist: keymap)
            for (int i=0;i < keylist.length();i++)
                map.put(keylist.charAt(i), Math.min(map.getOrDefault(keylist.charAt(i), keylist.length()), i + 1));
        
        for (int i=0;i < targets.length;i++) {
            cnt = 0;
            for (char c: targets[i].toCharArray()) {
                if (map.containsKey(c))
                    cnt += map.get(c);
                else {
                    cnt = -1;
                    break;
                }
            }
            answer[i] = cnt;        
        }
        return answer;
    }
}