class Solution {
    fun solution(str_list: Array<String>, ex: String): String {
        var answer: String = str_list.filter { !it.contains(ex) }.joinToString("")
        return answer
    }
}