import java.util.*;

class Solution {
    Map<String, String> nickname = new HashMap<>();

    public String[] solution(String[] record) {
        List<Record> records = new ArrayList<>();

        for (int i=0;i<record.length;i++) {
            String[] temp = record[i].split(" ");
            if (temp[0].equals("Enter")) {
                records.add(new Record(temp[1], "들어왔습니다."));
                nickname.put(temp[1], temp[2]);
            } else if (temp[0].equals("Leave")) {
                records.add(new Record(temp[1], "나갔습니다."));
            } else if (temp[0].equals("Change")) {
                nickname.put(temp[1], temp[2]);
            }
        }

        String[] answer = new String[records.size()];
        for (int i=0;i<records.size();i++) {
            Record r;
            r = records.get(i);
            answer[i] = nickname.get(r.userId)+"님이 "+r.act;
        }
        return answer;
    }
    class Record {
        String userId;
        String act;
        Record (String userId, String act) {
            this.userId = userId;
            this.act = act;
        }
    }
}