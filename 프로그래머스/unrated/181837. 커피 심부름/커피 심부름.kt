class Solution {
    companion object {
        const val CAFE_PRICE = 5000
        const val AMERI_PRICE = 4500

        val ameri = arrayOf("iceamericano", "americanoice", "hotamericano", "americanohot", "americano")
        val cafe = arrayOf("icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte")
    }

    
    fun solution(order: Array<String>): Int {
        var answer: Int = 0
        
        for (or in order) {
            answer += when (or) {
                in cafe -> CAFE_PRICE
                else -> AMERI_PRICE
            }
        }
        return answer
    }
}