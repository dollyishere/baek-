class Solution {
    fun solution(n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        for (i in 0 .. n) {
            if (i % 2 == 1) {
                answer += i
            }
        }
        return answer
    }
}