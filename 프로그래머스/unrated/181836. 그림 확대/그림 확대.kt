class Solution {
    fun solution(picture: Array<String>, k: Int): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        for (pic in picture) {
            var nowP: String = ""
            for (p in pic) {
                repeat(k) { nowP += p }
            }
            repeat(k) { answer += nowP }
        }
        return answer
    }
}