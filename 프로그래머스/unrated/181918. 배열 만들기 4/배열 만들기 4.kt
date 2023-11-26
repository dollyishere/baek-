import java.util.ArrayList;

class Solution {
    fun solution(arr: IntArray): IntArray {
        var stk = ArrayList<Int>()
        var i: Int = 0
        
        while (i < arr.size) {
            if (stk.isEmpty()) {
                stk += arr[i]
                i ++
            } else {
                if (stk.last() < arr[i]) {
                    stk += arr[i]
                    i ++
                } else {
                    stk.removeLast()
                }
            }
        }
        
        return stk.toIntArray()
    }
}