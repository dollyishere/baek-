import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        List<String> list = new ArrayList<>(Arrays.asList(strings));
        
        // Comparator(제네릭 인터페이스)의 compare 메서드는 두 객체 비교해서 정렬 순서 결정함
        // 음수일 시 , 첫 번째 객체가 두 번째 객체보다 작음
        // 0일 시, 두 객체가 같음
        // 양수일 시, 첫 번째 객체가 두 번째 객체보다 큼
        Collections.sort(list, new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                // out of range 방지
                if (s1.length() <= n || s2.length() <= n) {
                    return 0;
                }

                int charComparsion = Character.compare(s1.charAt(n), s2.charAt(n));
                // 해당 인덱스 문자가 같다면, 전체적으로 비교
                if (charComparsion == 0) {
                    return s1.compareTo(s2);
                }
                return charComparsion;
            }
        });
        
        
        // String array 형식으로 변환
        String[] answer = list.toArray(new String[0]);
        return answer;
    }
}