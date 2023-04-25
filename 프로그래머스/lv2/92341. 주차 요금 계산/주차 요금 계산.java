import java.util.*;

class Solution {
    int basic;
    int basicFee;
    int unit;
    int unitFee;
    
    int convertToMinute(String time) {
        String[] temp = time.split(":");
        return Integer.parseInt(temp[0]) * 60 + Integer.parseInt(temp[1]);
    }
    
    public int[] solution(int[] fees, String[] records) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        Map<String, Integer> feeMap = new HashMap<>();
        
        basic = fees[0];
        basicFee = fees[1];
        unit = fees[2];
        unitFee = fees[3];
        
        for (String record: records) {
            String[] temp = record.split(" ");
            if (temp[2].equals("IN")) {
                map.put(temp[1], convertToMinute(temp[0]));
            } else {
                feeMap.put(temp[1], feeMap.getOrDefault(temp[1], 0) + convertToMinute(temp[0])-map.get(temp[1]));
                map.put(temp[1], -1);
            }
        }
        for (String key: map.keySet()) {
            if (map.get(key) >= 0) {
                feeMap.put(key, feeMap.getOrDefault(key, 0) + convertToMinute("23:59")-map.get(key));
            }
        }
        
        List<String> cars = new ArrayList<>(map.keySet());
        Collections.sort(cars);
        
        for (String car: cars) {
            int t = feeMap.get(car);
            if (t <= basic) {
                answer.add(basicFee);
            } else {
                int temp = (t-basic) / unit;
                if ((t-basic) % unit > 0) {
                    temp++;
                }
                answer.add(basicFee + unitFee * temp);
            }
        }
        return answer.stream().mapToInt(integer -> integer).toArray();
    }
}