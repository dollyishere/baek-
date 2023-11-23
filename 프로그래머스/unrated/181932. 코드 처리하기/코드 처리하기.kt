class Solution {
    fun solution(code: String): String {
        var answer: String = ""
        var mode: Int = 0
        
        for (idx in 0..code.length-1) {
            if (mode == 0) {
                if (code[idx].toString() != "1") {
                    if (idx % 2 == 0) {
                        answer += code[idx].toString()
                    }
                } else {
                    mode = 1
                }
            } else {
                if (code[idx].toString() != "1") {
                    if (idx % 2 == 1) {
                        answer += code[idx].toString()
                    } 
                } else {
                    mode = 0
                }
            }
        }
        
        if (answer == "") {
            answer = "EMPTY"
        }
        
        return answer
    }
}