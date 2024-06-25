import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int a : arr) {
            if (a % divisor == 0) {
                answer.add(a);
            }
        }
        
        if (answer.size() == 0) {
            answer.add(-1);
        } else {
            // todo: 정렬 직접 구현
            Collections.sort(answer);
        }
        
        // stream을 이용한 ArrayList<Integer> => int[] 변환
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}