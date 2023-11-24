class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer: IntArray = arr
        
        for (i in 0 until queries.size) {
            val now_query = queries[i]
            val change_value = arr[now_query[0]]
            arr[now_query[0]] = arr[now_query[1]]
            arr[now_query[1]] = change_value
        }
        
        return answer
    }
}