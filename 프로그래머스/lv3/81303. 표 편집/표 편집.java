import java.util.*;

class Solution {
    public String solution(int n, int k, String[] cmd) {
        String[] table = new String[n];
        Arrays.fill(table, "O");

        Node head = set(n);
        Node current = find(k, head);

        Stack remove = new Stack();

        for (String c: cmd) {
            if (c.equals("C")) {
                remove.push(current);
                table[current.n] = "X";
                if (current.prev == null) {
                    current = current.next;
                    current.prev = null;
                } else if (current.next == null) {
                    current = current.prev;
                    current.next = null;
                } else {
                    current.prev.next = current.next;
                    current.next.prev = current.prev;
                    current = current.next;
                }
            } else if (c.equals("Z")) {
                Node node = (Node) remove.pop();
                table[node.n] = "O";
                if (node.prev != null)
                    node.prev.next = node;
                if (node.next != null)
                    node.next.prev = node;
                if (current == null)
                    current = node;

            } else {
                String[] tmp = c.split(" ");
                int num = Integer.parseInt(tmp[1]);
                if (tmp[0].equals("U")) {
                    while (num-- > 0)
                        current = current.prev;
                } else {
                    while (num-- > 0)
                        current = current.next;
                }
            }
        }
        return String.join("", table);
    }

    private Node set(int n) {
        Node head = new Node();
        Node prev = head;
        Node node;
        for (int i = 1; i < n; i++) {
            node = new Node();
            node.n = i;
            node.prev = prev;

            prev.n = i - 1;
            prev.next = node;
            prev = node;
        }
        return head;
    }

    private Node find(int k, Node head) {
        Node node = head;
        while (k-- > 0) {
            node = node.next;
        }
        return node;
    }

    class Node {
        int n;
        Node prev;
        Node next;
    }
}