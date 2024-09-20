class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        
        int midV = 0;
        
        if (total != 0) {
            midV = total / num;
        }
        
        int startV = midV - (num / 2);
        
        if (num % 2 == 0) {
            startV++;
        }
        
        for (int i=0;i<num;i++) {
            answer[i] = startV;
            startV++;
        }
        
        return answer;
    }
}