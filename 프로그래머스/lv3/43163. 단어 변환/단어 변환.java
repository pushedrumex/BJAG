import java.util.*;

class Solution {
    Map<String, Boolean> map = new HashMap<>();
    int answer = Integer.MAX_VALUE;
    String[] words;
    String target;
    
    public int solution(String begin, String target, String[] words) {
        if (!Arrays.asList(words).contains(target)) return 0;
        this.words = words;
        this.target = target;
        map.put(begin, true);
        dfs(0, begin);
        return answer;
    }
    
    int countDiff(String s1, String s2) {
        int result = 0;
        for (int i=0;i<s1.length();i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (++result == 2) return result;
            }
        }
        return result;
    }
    void dfs(int cnt, String s) {
        if (s.equals(target)) {
            answer = Math.min(answer, cnt);
            return;
        }
        for (String word: words) {
            if (!map.containsKey(word) && countDiff(s, word) == 1) {
                map.put(word, true);
                dfs(cnt+1, word);
                map.remove(word);
            }
        }
    }
}