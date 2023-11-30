class Solution {
    fun solution(n: Int, slicer: IntArray, num_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        val a: Int = slicer[0]
        val b: Int = slicer[1]
        val c: Int = slicer[2]
        
        answer = when(n) {
            1 -> num_list.slice(0 .. b).toIntArray()
            2 -> num_list.slice(a until num_list.size).toIntArray()
            3 -> num_list.slice(a .. b).toIntArray()
            else -> num_list.slice(a .. b step c).toIntArray()
        }
        
        return answer
    }
}