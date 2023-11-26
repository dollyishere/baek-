class Solution {
    fun solution(l: Int, r: Int): IntArray {
        var answer: IntArray = intArrayOf()
        val checkNums:  Array<String> = arrayOf("0", "5")
        // until 사용할 시 r은 포함되지 않으므로 .. 사용
        for (i in l..r) {
            var nowNum = i.toString()
            var check = true
            
            for (j in 0 until nowNum.length) {
                if (!(nowNum[j].toString() in checkNums)) {
                    check = false
                    break
                }
            }
            if (check) {
                answer += nowNum.toInt()
            }
        }
        
        if (answer.size == 0) {
            answer += -1
        }
        return answer
    }
}