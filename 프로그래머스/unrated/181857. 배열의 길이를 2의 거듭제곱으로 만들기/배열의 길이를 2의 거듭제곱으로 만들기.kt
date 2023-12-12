class Solution {
    fun solution(arr: IntArray): IntArray {
        var answer: IntArray = arr
        var here: Int = 1
        
        while (here < arr.size) {
            here *= 2
        }
        
        while (answer.size != here) {
            answer += 0
        }
        
        return answer
    }
}