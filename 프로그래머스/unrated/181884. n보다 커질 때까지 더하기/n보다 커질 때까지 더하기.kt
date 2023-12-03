class Solution {
    fun solution(numbers: IntArray, n: Int): Int {
        var answer: Int = 0
        for (i in 0 until numbers.size) {
            answer += numbers[i].toInt()
            if (answer > n) {
                break
            }
        }
        return answer
    }
}