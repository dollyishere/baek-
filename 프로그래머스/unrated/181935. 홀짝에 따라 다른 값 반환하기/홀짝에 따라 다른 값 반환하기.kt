import kotlin.math.*

class Solution {
    fun solution(n: Int): Int {
        var answer: Int = 0
        
        if (n % 2 == 0) {
            for (i in 1..n) {
                if (i % 2 == 0) {
                    answer += i.toDouble().pow(2).toInt()
                }
            }
        } else {
            for (i in 1..n) {
                if (i % 2 != 0) {
                    answer += i
                }
            }
        }
        return answer
    }
}