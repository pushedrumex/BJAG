import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String nums = br.readLine();

        int i = 0;
        long n = 1;
        boolean end = false;
        while (true) {
            for (char c: String.valueOf(n).toCharArray()) {
                if (nums.charAt(i) == c) {
                    i++;
                    if (i >= nums.length()) {
                        end = true;
                        break;
                    }
                }
            }
            if (end) {
                break;
            }
            n++;
        }
        System.out.println(n);
    }


}
