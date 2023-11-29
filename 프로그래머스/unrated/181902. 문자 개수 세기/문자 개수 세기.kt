class Solution {
    fun solution(my_string: String): IntArray {
        var answer: IntArray = IntArray(52)
        var ascii: Int = 65
        
        for (i in 0 until 52) {
            // 아스키 코드에서 char 형태로 전환
            var nowChar = ascii.toChar()
            var nowCnt = 0
            for (j in 0 until my_string.length) {
                if (nowChar == my_string.get(j)) {
                    nowCnt ++
                }
            }
            answer[i] = nowCnt
            
            if (ascii == 90) {
                ascii = 97
            } else {
                ascii ++
            }
            
        }
        
        return answer
    }
}