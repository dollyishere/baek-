class Solution {
    fun solution(str1: String, str2: String): String {
        var answer: String = ""
        
        // indices = 문자열이나 리스트 같은 컬렉션의 유효한 인덱스 범위를 나타내는 함수
        for (num in str1.indices) {
            answer += str1[num]
            answer += str2[num]
        }
        return answer
    }
}