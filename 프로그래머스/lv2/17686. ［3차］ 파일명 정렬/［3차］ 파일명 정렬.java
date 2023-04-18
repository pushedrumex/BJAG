import java.util.Arrays;

class Solution {

    public static void main(String[] args) {
        System.out.println(solution(new String[]{"img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"}));
    }

    static class Node {
        String HEAD;
        int NUMBER;

        public Node(String HEAD, int NUMBER) {
            this.HEAD = HEAD;
            this.NUMBER = NUMBER;
        }
    }
    static Node parseString(String s) {
        String HEAD = "";
        String NUMBER = "";
        char c;
        int i;

        s = s.toLowerCase();
        for (i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if ('0' <= c && c <= '9')
                break;
            HEAD += c;
        }

        for (; i < s.length(); i++) {
            c = s.charAt(i);
            if (!('0' <= c && c <= '9'))
                break;
            NUMBER += c;
        }
        return new Node(HEAD, Integer.parseInt(NUMBER));
    }

    public static String[] solution(String[] files) {

        Arrays.sort(files, (o1, o2) -> {
            Node node1 = parseString(o1);
            Node node2 = parseString(o2);

            int n = node1.HEAD.compareTo(node2.HEAD);

            if (n > 0) {
                return 1;
            } else if (n == 0) {
                return node1.NUMBER - node2.NUMBER;
            }

            return -1;
        });
        return files;
    }
}