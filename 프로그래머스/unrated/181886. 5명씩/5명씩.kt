class Solution {
    fun solution(names: Array<String>): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        for (i in 0 until names.size step 5) {
            answer += names[i].toString()
        }
        return answer
    }
}