import java.util.*;

class Solution {
    
    // 최대공약수
    private int gcd(int a, int b) {
        // b가 0이 될때까지 계산(0이 된다면, 약수임)
        while (b != 0) {
            // 기존 b값을 temp에 저장
            int temp = b;
            // b 값을 a에 b를 나눈 뒤 나머지 값으로 대체
            b = a % b;
            // a 값을 temp로 교체
            a = temp;
        }
        return a;
    }
    
    // 최소공배수(lcm)를 구하는 메서드
    private int lcm(int a, int b) {
        // gcd를 활용해 lcm 계산
        // b는 그대로 둔 뒤, a만 최대공약수로 나눠서 공통 약수를 없애고 b와 곱하는 것
        return (a / gcd(a, b)) * b;
    }
    
    
    public int solution(int[] arr) {
        // arr의 첫 값으로 일단 세팅해둔 뒤, 두번째 값부터 lcm 실행
        // answer 값과 다음 arr의 최소공배수 값으로 매번 answer 갱신
        int answer = arr[0];
        
        for (int i=1;i<arr.length;i++) {
            answer = lcm(answer, arr[i]);
        }
        
        // 답 return
        return answer;
    }
}
