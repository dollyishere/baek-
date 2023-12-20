class Solution {
    fun solution(arr: Array<IntArray>): Array<IntArray> {
        var answer: Array<IntArray> = arr
        var arr_size = arr.size
        var inside_arr_size = arr[0].size
        if (arr_size > inside_arr_size) {
            answer = arrayOf<IntArray> ()
            for (i in 0 until arr_size) {
                var now_add = arr[i]
                repeat(arr_size - inside_arr_size) { now_add += 0 }
                answer += now_add
            }
        } else if (inside_arr_size > arr_size) {
            var add_arr = IntArray(inside_arr_size)
            repeat(inside_arr_size - arr_size) { answer += add_arr }
        }
        return answer
    }
}