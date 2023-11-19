class Solution {
    fun solution(a: Int, b: Int): Int {
        var answer: Int = 0
        var ab : Int = (a.toString() + b.toString()).toInt()
        var twoab : Int = 2 * a * b
        
        if (ab >= twoab) {
            answer = ab
        } else {
            answer = twoab
        }
        return answer
    }
}