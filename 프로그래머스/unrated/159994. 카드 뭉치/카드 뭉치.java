import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        Deque<String> q1 = new ArrayDeque();
        Deque<String> q2 = new ArrayDeque();
        
        for (String word: cards1)
            q1.addLast(word);
        
        for (String word: cards2)
            q2.addLast(word);
        
        for (String word: goal) {
            if (!q1.isEmpty() && q1.peekFirst().equals(word))
                q1.removeFirst();
            else if (!q2.isEmpty() && q2.peekFirst().equals(word))
                q2.removeFirst();
            else
                return "No";
                
        }
        return "Yes";
    }
}