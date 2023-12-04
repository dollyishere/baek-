class Solution {
    fun solution(arr: IntArray): Int {
        var answer: Int = 0
        var answerArr: IntArray = arr
        
        while (true) {
            var cnt: Int = 0
            
            for (i in 0 until answerArr.size) {
                if (answerArr[i] >= 50 && answerArr[i] % 2 == 0) {
                    answerArr[i] /= 2
                    cnt ++
                } else if (answerArr[i] < 50 && answerArr[i] % 2 == 1) {
                    answerArr[i] *= 2
                    answerArr[i] += 1
                    cnt ++
                }
            }
            
            if (cnt == 0) {
                break
            } else {
                answer += 1
            }
        }
        return answer
    }
}