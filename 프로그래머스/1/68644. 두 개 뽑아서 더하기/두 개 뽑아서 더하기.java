import java.util.ArrayList;

class Solution {
    public int[] solution(int[] numbers) {
        ArrayList<Integer> nums = new ArrayList<>();
        for (int i=0;i<numbers.length;i++) {
            for (int j=0;j<numbers.length;j++) {
                if (i != j) {
                    int numPlus = numbers[i] + numbers[j];
                    if (!nums.contains(numPlus)) {
                        nums.add(numPlus);
                    }
                }
            }
        }
        
        nums.sort((a, b) -> a - b);
        
        int[] answer = nums.stream()
                            .mapToInt(Integer::intValue)
            .toArray();
        
        return answer;
    }
}