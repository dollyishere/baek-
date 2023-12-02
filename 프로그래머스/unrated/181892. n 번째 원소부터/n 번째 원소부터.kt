class Solution {
    fun solution(num_list: IntArray, n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        answer = num_list.slice(n-1 until num_list.size).toIntArray()
        return answer
    }
}