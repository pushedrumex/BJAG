import java.util.*;
import java.io.*;

public class Main {

    static int[] upCount;
    static int[] down;
    static int[] downCount;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        down = new int[N+1];
        downCount = new int[N+1];
        upCount = new int[N+1];
        Arrays.fill(upCount, 1);
        for (int i = 1; i <= N; i++) {
            int n = Integer.parseInt(br.readLine());
            down[i] = n;
            downCount[n]++;
        }
        for (int n = 1; n <= N; n++) {
            if (upCount[n] == 1 && downCount[n] == 0) {
                decrease(n);
            }
        }
        int count = 0;
        for (int n = 1; n <= N; n++) {
            if (downCount[n] > 0) {
                count++;
            }
        }

        System.out.println(count);
        for (int n = 1; n <= N; n++) {
            if (downCount[n] > 0) {
                System.out.println(n);
            }
        }
    }

    static void decrease(int n) {
        upCount[n]--;
        int m = down[n];
        downCount[m]--;
        if (downCount[m] == 0) {
            decrease(m);
        }
    }
}