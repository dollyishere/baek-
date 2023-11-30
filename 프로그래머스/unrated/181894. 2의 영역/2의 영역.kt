class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var findTwo = false
        var start = 0
        var end = 0
        
        for (i in 0 until arr.size) {
            if (arr[i] == 2) {
                if (start == 0 && findTwo == false) {
                    start = i
                    findTwo = true
                } else {
                    end = i
                }
            }
        }
        
        
        if (start == 0 && end == 0) {
            answer = intArrayOf(-1)
        } else {
            if (end != 0) {
                answer = arr.slice(start .. end).toIntArray()
            } else {
                answer = intArrayOf(arr[start])
            }
        }
        
        return answer
    }
}