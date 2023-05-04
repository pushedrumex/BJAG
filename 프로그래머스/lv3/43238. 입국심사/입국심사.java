import java.util.*;

class Solution {
    int n;
    int[] times;
    long answer, mid;
    public long solution(int n, int[] times) {
        this.n = n;
        this.times = times;
        Arrays.sort(times);
        binarySearch(0, Long.MAX_VALUE / 10);
        return answer;
    }
    long cnt; // mid 시간동안 받을 수 있는 최대 인원 수
    void binarySearch(long start, long end) {
        while (start <= end) {
            cnt = 0;
            mid = start + (end-start)/2;
            
            for (int time: times) {
                cnt += mid / time;
            }
            
            if (cnt < n) {
                start = mid + 1;
            } else {
                answer = mid;
                end = mid - 1;
            }
        }
        
    }
}