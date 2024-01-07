class Solution {
    fun solution(angle: Int): Int {
        var answer = when {
            0 < angle && angle < 90 -> 1
            angle == 90 -> 2
            90 < angle && angle < 180 -> 3
            else -> 4
        }
        return answer
    }
}