class Solution {
    fun solution(number: String): Int {
        var answer: Int = 0
        var change: Long = 0
        
        for (i in 0 until number.length) {
            // number의 값이 Int 타입을 넘어서는 경우(case 2)가 있어서 Long 타입으로 대체
            change += number[i].toString().toLong()
        }
        
        answer = change.toInt() % 9
        
        return answer
    }
}