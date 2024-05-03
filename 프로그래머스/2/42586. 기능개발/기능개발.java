import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int N = progresses.length;
        ArrayDeque<Integer> dq = new ArrayDeque<>();
        for (int i=0;i<N;i++) {
            int progress = progresses[i];
            int speed = speeds[i];
            dq.addLast(getDeploy(progress, speed));
        }
        
        ArrayList<Integer> answer = new ArrayList<>();
        while (!dq.isEmpty()) {
            int now = dq.removeFirst();
            int count = 1;
            
            while (!dq.isEmpty() && dq.peekFirst() <= now) {
                count++;
                dq.removeFirst();
            }
            
            answer.add(count);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }
    
    int getDeploy(int progress, int speed) {
        int deploy = (100 - progress) / speed;
        if ((100 - progress) % speed > 0) deploy++;
        return deploy;
        
    }
}