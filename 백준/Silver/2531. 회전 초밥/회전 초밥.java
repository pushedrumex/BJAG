import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int[] sushis = new int[2 * N];
        for (int i = 0; i < N; i++) {
            int sushi = Integer.parseInt(br.readLine());
            sushis[i] = sushi;
            sushis[i + N] = sushi;
        }

        int answer = 1;
        int[] count = new int[d + 1];
        for (int i = 0; i < k; i++) {
            int sushi = sushis[i];
            if (sushi == c) continue;
            if (count[sushi]++ == 0) answer++;
        }

        int left = 1;
        int right = k;
        int _answer = answer;
        while (left <= N) {
            if (sushis[left - 1] != c) {
                count[sushis[left - 1]]--;
                if (count[sushis[left - 1]] == 0) _answer--;
            }

            if (sushis[right] != c) {
                if (count[sushis[right]] == 0) _answer++;
                count[sushis[right]]++;
            }

            answer = Math.max(answer, _answer);
            left++;
            right++;
        }

        System.out.println(answer);
    }

}
