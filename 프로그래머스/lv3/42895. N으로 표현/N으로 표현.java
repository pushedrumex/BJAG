import java.util.*;

class Solution {
    public int solution(int N, int number) {
        Set<Integer>[] dp = new Set[9];
        
        for (int i=1;i<9;i++) {
            dp[i] = new HashSet<>();
            
            StringBuffer temp = new StringBuffer();
            int cnt = i;
            while (cnt-- > 0) temp.append(String.valueOf(N));
            
            dp[i].add(Integer.parseInt(temp.toString()));
            
            for (int j=1;j<=i/2;j++) {
                for (int n1: dp[j]) {
                    for (int n2: dp[i-j]) {
                        dp[i].add(n1+n2);
                        dp[i].add(n1*n2);
                        dp[i].add(n1-n2);
                        dp[i].add(n2-n1);
                        if (n1 > 0) dp[i].add(n2/n1);
                        if (n2 > 0) dp[i].add(n1/n2);
                    }
                }
            }
        }
        
        for (int i=1;i<9;i++) {
            for (int n: dp[i]) {
                if (n == number) return i;
            }
        }
        
        return -1;
    }
}

