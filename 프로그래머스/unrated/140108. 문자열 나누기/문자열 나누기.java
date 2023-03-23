import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        int same, diff;
        Deque<String> q = new ArrayDeque(Arrays.asList(s.split("")));
        String first, target;
        
        while (!q.isEmpty()) {
            answer++;
            first = q.removeFirst();
            same = 1;
            diff = 0;
            
            while (!q.isEmpty() && same != diff ) {
                target = q.removeFirst();
                if (target.equals(first)) {
                    same++;
                } else {
                    diff++;
                }
            }
        }
        
        return answer;
    }
}