class Solution {
    fun solution(num_list: IntArray): Int {
        var answer: Int = 0
        var num_list_c: IntArray = num_list
        var check_cnt: IntArray = IntArray(num_list_c.size)
        while (true) {
            var cnt: Int = 0
            for (i in 0 until num_list_c.size) {
                if (num_list_c[i] == 1) {
                    cnt ++
                } else if (num_list_c[i] % 2 == 0) {
                    num_list_c[i] /= 2
                    check_cnt[i] ++
                } else if (num_list_c[i] % 2 == 1) {
                    num_list_c[i] -= 1
                    num_list_c[i] /= 2
                    check_cnt[i] ++
                }
            }
            if (cnt == num_list.size) {
                break
            }
        }
        
        for (j in 0 until check_cnt.size) {
            answer += check_cnt[j].toInt()
        }
        return answer
    }
}