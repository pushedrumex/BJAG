import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int L = S.length();

        HashMap<String, Boolean> map = new HashMap<>();
        int answer = 0;
        for (int l = 1; l <= L; l++) {
            for (int i = 0; i <= L - l; i++) {
                String substring = S.substring(i, i + l);
                if (!map.containsKey(substring)) {
                    map.put(substring, true);
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
}