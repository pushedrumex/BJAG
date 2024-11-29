import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());

        ArrayList<FastWay>[] fastWays = new ArrayList[D + 1];
        for (int i = 1; i <= D; i++) {
            fastWays[i] = new ArrayList<>();
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            if (end > D) {
                continue;
            }

            fastWays[end].add(new FastWay(start, cost));
        }

        int[] dp = new int[D+1];
        for (int i = 1; i <= D; i++) {
            dp[i] = dp[i-1] + 1;
            for (FastWay fastWay : fastWays[i]) {
                dp[i] = Math.min(dp[i], dp[fastWay.start] + fastWay.cost);
            }
        }

        System.out.println(dp[D]);
    }

    static class FastWay {
        int start;
        int cost;

        FastWay(int start, int cost) {
            this.start = start;
            this.cost = cost;
        }
    }

}
