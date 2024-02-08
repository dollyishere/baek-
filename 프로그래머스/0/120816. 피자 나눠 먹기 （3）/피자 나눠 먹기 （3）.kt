class Solution {
    fun solution(slice: Int, n: Int): Int {
        var answer: Int = (n / slice)
        if (n % slice != 0) {
            answer ++
        }
        return answer
    }
}