import java.util.*;

class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        Arrays.fill(answer, "X");
        
        for (int j=0;j<quiz.length;j++) {
            StringBuilder firstV = new StringBuilder();
            StringBuilder secondV = new StringBuilder();
            StringBuilder resultV = new StringBuilder();
            
            boolean isPlus = true;
            int trigger = 0;
            
            for (int i=0;i<quiz[j].length();i++) {
                char nowC = quiz[j].charAt(i);
                
                switch (trigger) {
                    case 0:
                        if (nowC == ' ') {
                            trigger++;
                            continue;
                        }
                        firstV.append(nowC);
                        break;
                    case 1:
                        if (nowC == ' ') {
                            trigger++;
                            continue;
                        }
                        if (nowC == '-') {
                            isPlus = false;
                        }
                        break;
                    case 2:
                        if (nowC == ' ') {
                            trigger++;
                            continue;
                        }
                        secondV.append(nowC);
                        break;
                    case 3:
                        if (nowC == ' ' || nowC == '=') {
                            continue;
                        }
                        resultV.append(nowC);
                        break;
                    default:
                        break;
                }
            }
            
            int realR = 0;
            if (isPlus) {
                realR = Integer.parseInt(firstV.toString()) + Integer.parseInt(secondV.toString());
            } else {
                realR = Integer.parseInt(firstV.toString()) - Integer.parseInt(secondV.toString());
            }
            
            if (realR == Integer.parseInt(resultV.toString())) {
                answer[j] = "O";
            }
        }
        
        return answer;
    }
}