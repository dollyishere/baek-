class Solution {
    fun solution(myStr: String): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        var check: Array<Char> = arrayOf<Char>('a', 'b', 'c')
        var temp: String = ""
        
        for (s in myStr) {
            if (s in check)  {
                if (temp != "") {
                    answer += temp
                    temp = ""
                }
            } else {
                temp += s
            }
        }
        
        if (temp != "") {
            answer += temp
        }
        
        if (answer.size == 0) {
            answer = arrayOf<String>("EMPTY")
        }
        return answer
    }
}