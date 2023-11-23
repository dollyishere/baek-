class Solution {
    fun solution(a: Int, b: Int, c: Int): Int {
        var answer: Int = 0
        
        if (a != b && b != c && c != a) {
            answer = a + b + c
        } else if (a == b && b == c && c == a) {
            answer = (a + b + c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)
        } else {
            answer = (a + b + c) * (a*a + b*b + c*c)
        }
        return answer
    }
}