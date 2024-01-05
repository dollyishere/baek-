class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer: IntArray = numbers
        for (a in 0 until numbers.size) {
            answer[a] *= 2
        }
        return answer
    }
}