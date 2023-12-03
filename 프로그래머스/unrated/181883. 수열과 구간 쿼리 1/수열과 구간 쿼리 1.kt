class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer: IntArray = arr
        for (i in 0 until queries.size) {
            val nowQ = queries[i]
            for (j in nowQ[0].toInt() .. nowQ[1].toInt()) {
                answer[j] ++
            }
        }
        return answer
    }
}