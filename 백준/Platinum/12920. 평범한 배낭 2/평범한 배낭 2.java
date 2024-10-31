import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        ArrayList<Good> goods = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            // 이진수를 통해 물건 세트화
            int k = 1;
            while (K > k) {
                goods.add(new Good(V * k, C * k));
                K -= k;
                k *= 2;
            }
            if (K > 0) {
                goods.add(new Good(V * K, C * K));
            }
            
        }

        N = goods.size();
        int[][] dp = new int[N + 1][M + 1];

        // i번째 물건까지 탐색함
        for (int i = 1; i <= N; i++) {
            Good good = goods.get(i - 1);
            int V = good.V;
            int C = good.C;
            for (int m = 1; m <= M; m++) {
                if (V > m) {
                    dp[i][m] = dp[i - 1][m];
                    continue;
                }
                dp[i][m] = Math.max(dp[i - 1][m], dp[i - 1][m - V] + C);
            }
        }
        System.out.println(dp[N][M]);
    }

    static class Good {
        int V; // 무게
        int C; // 만족도
        Good(int V, int C) {
            this.V = V;
            this.C = C;
        }
    }

}