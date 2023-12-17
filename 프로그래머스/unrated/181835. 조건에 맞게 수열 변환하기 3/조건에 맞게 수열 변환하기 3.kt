class Solution {
    fun solution(arr: IntArray, k: Int): IntArray {
        var answer: IntArray = arr
        for (a in 0 until answer.size) {
            when {
                k % 2 == 1 -> answer[a] *= k
                else -> answer[a] += k
            } 
        }
        return answer
    }
}