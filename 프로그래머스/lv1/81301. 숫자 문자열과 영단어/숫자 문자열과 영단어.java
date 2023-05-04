import java.util.*;

class Solution {
    public int solution(String s) {
        Map<String, String> map = new HashMap<>();
        String[] words = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        int num = 0;
        for (String word: words) {
            map.put(word, String.valueOf(num++));
        }
        Deque<String> q = new ArrayDeque<>();
        for (String temp: s.split("")) {
            q.addLast(temp);
        }
        
        StringBuffer temp;
        StringBuffer answer = new StringBuffer();
        while (!q.isEmpty()) {
            temp = new StringBuffer(q.removeFirst());
            char c = temp.charAt(0);
            if ('0' <= c && c <= '9') {
                answer.append(temp);
                continue;
            }
            while (!q.isEmpty() && !map.containsKey(temp.toString())) {
                temp.append(q.removeFirst());
            }
            answer.append(map.get(temp.toString()));
        }
        return Integer.parseInt(answer.toString());
    }
}