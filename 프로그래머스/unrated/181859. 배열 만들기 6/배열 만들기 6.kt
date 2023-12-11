class Solution {
    fun solution(arr: IntArray): IntArray {
        var stk: IntArray = intArrayOf()
        for (i in 0 until arr.size) {
            if (stk.size == 0) {
                stk += arr[i]
            } else {
                if (stk.last() == arr[i]) {
                    stk = stk.toList().slice(0 until (stk.size - 1)).toIntArray()
                } else {
                    stk += arr[i]
                }
            }
        }
        
        if (stk.size == 0) {
            stk = intArrayOf(-1)
        }
        return stk
    }
}