import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Deque<String> q = new ArrayDeque<>();

        for (String city : cities) {
            city = city.toUpperCase();
            if (q.contains(city)) {
                answer += 1;
                q.remove(city);
            } else {
                answer += 5;
            }
            q.addLast(city);
            while (q.size() > cacheSize) {
                q.removeFirst();
            }
        }
        return answer;
    }
}