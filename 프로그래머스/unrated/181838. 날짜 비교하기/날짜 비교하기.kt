class Solution {
    fun changeInt(target: IntArray): Int {
        return target.map { it.toString() }.joinToString("").toInt()
    }
    
    fun solution(date1: IntArray, date2: IntArray): Int {
        var answer: Int = if (changeInt(date1) < changeInt(date2)) 1 else 0
        return answer
    }
}