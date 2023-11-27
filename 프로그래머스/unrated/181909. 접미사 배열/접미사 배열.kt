class Solution {
    fun solution(my_string: String): Array<String> {
        var answer: Array<String> = arrayOf<String>()

        for (i in 0 until my_string.length) {
            var nowS = my_string.slice(i until my_string.length).toString()
            if (!(nowS in answer)) {
                answer += nowS
            }
        }
        
        answer.sort()
        
        return answer
    }
}