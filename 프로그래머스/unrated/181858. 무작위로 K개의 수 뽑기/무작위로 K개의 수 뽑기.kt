class Solution {
    fun solution(arr: IntArray, k: Int): IntArray {
        var answer: IntArray = intArrayOf()
        var maxI: Int = 0
        
        for (a in arr) {
            if (answer.size == k) {
                break
            }
            if (a !in answer) {
                answer += a
            }
        }
        
        while (answer.size < k) {
            answer += -1
        }
        return answer
    }
}