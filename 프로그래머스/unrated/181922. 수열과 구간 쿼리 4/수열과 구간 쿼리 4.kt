class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer: IntArray = arr
        
        for (q in 0 until queries.size) {
            val nowQ = queries[q]
            
            for (i in nowQ[0]..nowQ[1]) {
                if (i % nowQ[2] == 0) {
                    answer[i] ++
                }
            }
            
        }
        
        return answer
    }
}