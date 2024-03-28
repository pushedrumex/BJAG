import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        HashMap<String, Integer> count = new HashMap();
        HashMap<String, ArrayList<Integer>> song = new HashMap();
        
        String genre;
        for (int i=0;i<genres.length;i++) {
            genre = genres[i];
            count.put(genre, count.getOrDefault(genre, 0) + plays[i]);
            if (!song.containsKey(genre)) {
                song.put(genre, new ArrayList());
            }
            song.get(genre).add(i);
        }
        
        ArrayList<Integer> answer = new ArrayList();
        ArrayList<String> keys = new ArrayList(count.keySet());
        Collections.sort(keys, (o1, o2) -> count.get(o2) - count.get(o1));
        for (String key: keys) {
            ArrayList<Integer> play = song.get(key);
            Collections.sort(play, (o1, o2) -> plays[o2] - plays[o1]);
            int temp = 2;
            for (Integer p: play) {
                answer.add(p);
                temp--;
                if (temp == 0) {
                    break;
                }
            }
        }
        
        return answer.stream().mapToInt(x -> x).toArray();
    }
}