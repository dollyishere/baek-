class Solution {
    fun solution(todo_list: Array<String>, finished: BooleanArray): Array<String> {
        var answer: Array<String> = arrayOf<String>()
        for (i in 0 until todo_list.size) {
            if (!finished[i]) {
                answer += todo_list[i].toString()
            }
        }
        return answer
    }
}