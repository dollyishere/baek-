class Solution {
    fun solution(n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        var x: Int = n
        
        while (true) {
            answer += x
            
            if (x == 1) {
                break
            }
            
            if (x % 2 == 0) {
                x /= 2
            } else {
                x = 3 * x + 1
            }
        }
        
        return answer
    }
}