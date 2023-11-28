class Solution {
    fun solution(n: Int): Int {
        var answer: Int = 1000001
        
        for (x in 1 .. n) {
            if (n % x == 1) {
                if (answer > x) {
                    answer = x
                }
            }
        }
        return answer
    }
}