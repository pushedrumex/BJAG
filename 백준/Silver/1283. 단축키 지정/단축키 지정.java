import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] infos = new String[N];

        for (int i = 0; i < N; i++) {
            infos[i] = br.readLine();
        }

        HashSet<String> visited = new HashSet<>();
        String[] answer = new String[N];
        for (int i = 0; i < N; i++) {
            String info = infos[i];
            boolean done = false;
            
            // 단어의 첫글자 확인
            String[] words = info.split(" ");
            for (int j = 0; j < words.length; j++) {
                String word = words[j];
                String x = word.substring(0, 1).toUpperCase();
                if (!visited.contains(x)) {
                    done = true;
                    visited.add(x);
                    StringBuffer sb = new StringBuffer();
                    for (int k = 0; k < words.length; k++) {
                        if (k != 0) sb.append(" ");
                        if (k == j) {
                            sb.append("[" + word.substring(0, 1) + "]" + word.substring(1));
                        } else {
                            sb.append(words[k]);
                        }
                    }
                    answer[i] = String.valueOf(sb);
                    break;
                }
            }

            // 왼쪽부터 탐색
            if (done) continue;
            for (int j = 0; j < info.length(); j++) {
                String x = info.substring(j, j + 1).toUpperCase();
                if (x.equals(" ")) {
                    continue;
                }
                if (!visited.contains(x)) {
                    done = true;
                    visited.add(x);
                    StringBuffer sb = new StringBuffer();
                    for (int k = 0; k < info.length(); k++) {
                        if (k == j) {
                            sb.append("[" + info.substring(k, k + 1) + "]");
                        } else {
                            sb.append(info.substring(k, k + 1));
                        }
                    }
                    answer[i] = String.valueOf(sb);
                    break;
                }

            }

            if (done) continue;

            // 지정할 수 없음
            answer[i] = info;
        }

        for (String t: answer) {
            System.out.println(t);
        }
    }

}
