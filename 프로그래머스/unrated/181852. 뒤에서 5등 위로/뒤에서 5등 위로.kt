class Solution {
    fun solution(num_list: IntArray): IntArray {
        var minFive: List<Int> = num_list.toList().sorted()
        
        return minFive.slice(5 until minFive.size).toIntArray()
    }
}