class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: IntArray = num_list.toList().sorted().take(5).toIntArray()
        return answer
    }
}