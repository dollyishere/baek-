class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        for (a in arr) {
            for (i in 0 until a) {
                answer += a
            }
        }
        return answer
    }
}