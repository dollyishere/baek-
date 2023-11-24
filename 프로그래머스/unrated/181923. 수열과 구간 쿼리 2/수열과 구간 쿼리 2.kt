class Solution {
    fun solution(arr: IntArray, queries: Array<IntArray>): IntArray {
        var answer: IntArray = intArrayOf()
        
        for (i in 0 until queries.size) {
            var start = queries[i][0]
            var end = queries[i][1]
            var line = queries[i][2]
            
            var nowValue = 1000001
            
            for (j in 0 until arr.size) {
                if (start <= j && j <= end && line < arr[j] && nowValue > arr[j]) {
                    nowValue = arr[j]
                }
            }
            
            if (nowValue == 1000001) {
                nowValue = -1
            }
            answer += nowValue
        }
        
        return answer
    }
}