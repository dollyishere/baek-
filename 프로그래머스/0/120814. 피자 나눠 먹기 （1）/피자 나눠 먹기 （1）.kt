class Solution {
    fun solution(n: Int): Int {
        var answer: Int = (n / 7)
        
        if (n % 7 != 0) {
            answer ++
        }
        return answer
    }
}