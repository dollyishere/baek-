class Solution {
    fun solution(arr: IntArray, query: IntArray): IntArray {
        var answer: IntArray = arr
        
        for (i in 0 until query.size) {
            if (i % 2 == 0) {
                answer = answer.slice(0 .. query[i]).toIntArray()
            } else {
                answer = answer.slice(query[i] until answer.size).toIntArray()
            }
        }
        
        return answer
    }
}