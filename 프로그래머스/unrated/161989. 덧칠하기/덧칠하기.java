import java.util.*;

class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int temp;
        Deque<Integer> q = new ArrayDeque();
        
        for (int i: section)
            q.addLast(i);
        
        while (!q.isEmpty()) {
            temp = q.removeFirst();
            answer++;
            while (!q.isEmpty() && q.peekFirst() - temp + 1 <= m)
                q.removeFirst();
        }
        
        return answer;
    }
}