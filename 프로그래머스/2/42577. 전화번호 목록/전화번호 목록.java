import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for (int i=0;i<phone_book.length-1;i++) {
            String prefix = phone_book[i];
            String phone = phone_book[i+1];
            if (prefix.length() > phone.length()) {
                continue;
            }
            if (prefix.equals(phone.substring(0, prefix.length()))) {
                return false;
            }
        }
        return true;
    }
}