import java.util.*;

class Solution {
    public int[] solution(String msg) {
        int[] answer;
        List<Integer> answerList = new ArrayList<>();
        String[] arr = msg.split("");
        int idx = 1;
        Map<String, Integer> dic = new HashMap<>();
        Deque<String> q = new ArrayDeque<>();
        String word = "";
        
        for (String alpha:"ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")) {
            dic.put(alpha, idx++);
        }
        
        for(String alpha:msg.split("")) {
            q.addLast(alpha);
        }
        
        while (!q.isEmpty()) {
            word += q.removeFirst();
            while (!q.isEmpty() && dic.get(word) != null) {
                word += q.removeFirst();
            }
            System.out.println(word);
            if (dic.get(word) != null) {
                answerList.add(dic.get(word));
            } else {
                answerList.add(dic.get(word.substring(0, word.length()-1)));
                dic.put(word, idx++);
                q.addFirst(word.substring(word.length()-1));
                word = "";
            }
        }
        
        answer = new int[answerList.size()];
        for (int i=0;i<answer.length;i++) {
            answer[i] = answerList.get(i);
        }
        return answer;
    }
}