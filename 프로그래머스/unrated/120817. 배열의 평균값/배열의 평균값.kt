class Solution {
    fun solution(numbers: IntArray): Double {
        var answer: Double = 0.0
        for (i in 0 until numbers.size) {
            answer += numbers[i]
        }
        answer /= numbers.size
        return answer
    }
}