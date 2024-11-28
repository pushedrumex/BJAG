import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] count = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            count[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 2; i <= N; i++) {
            count[i] += count[i-1];
        }

        int maxCount = 0;
        int periodCount = 0;
        for (int i = 1; i <= N - X + 1; i++) {
            int _count = count[i + X - 1] - count[i - 1];
            if (maxCount < _count) {
                maxCount = _count;
                periodCount = 1;
            } else if (maxCount == _count) {
                periodCount++;
            }
        }

        if (maxCount == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(maxCount);
            System.out.println(periodCount);
        }
    }
}