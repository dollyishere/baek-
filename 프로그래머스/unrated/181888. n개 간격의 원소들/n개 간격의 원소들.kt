class Solution {
    fun solution(num_list: IntArray, n: Int): IntArray {
        var answer: IntArray = intArrayOf()
        answer = num_list.slice(0 until num_list.size step n).toIntArray()
        return answer
    }
}