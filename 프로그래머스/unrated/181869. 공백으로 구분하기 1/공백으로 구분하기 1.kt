class Solution {
    fun solution(my_string: String): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        var temp: String = ""
        

        for (i in 0 until my_string.length) {
            if (my_string[i] == ' ') {
                answer += temp
                temp = ""
            } else {
                temp += my_string[i]
            }
        }
        
        if (temp != "") {
            answer += temp
            temp = ""
        }
        
        return answer
    }
}