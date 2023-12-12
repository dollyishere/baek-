class Solution {
    fun solution(strArr: Array<String>): Int {
        var answer: Int = 0
        var letters = mutableMapOf<Int, Int>()
        var maxKey = 1
        
        for (a in strArr) {
            letters[a.length] = letters.getOrDefault(a.length, 0) + 1
        }
        
        return letters.values.maxOrNull() ?: 0
    }
}