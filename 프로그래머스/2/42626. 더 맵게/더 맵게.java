import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int sc: scoville) {
            pq.add(sc);
        }
        
        int answer = 0;
        while (!pq.isEmpty() && pq.peek() < K) {
            if (pq.size() < 2) return -1;
            int first = pq.remove();
            int second = pq.remove();
            pq.add(first + second * 2);
            answer++;
        }
        return answer;
    }
}