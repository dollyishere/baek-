class Solution {
    fun solution(num_list: IntArray): IntArray {
        var answer: IntArray = intArrayOf()
        var newList: IntArray
        
        if (num_list.last() > num_list[num_list.size-2]) {
            newList = intArrayOf(num_list.last() - num_list[num_list.size-2])
        } else {
            newList = intArrayOf(num_list.last() * 2)
        }
        
        answer = num_list + newList
        
        return answer
    }
}