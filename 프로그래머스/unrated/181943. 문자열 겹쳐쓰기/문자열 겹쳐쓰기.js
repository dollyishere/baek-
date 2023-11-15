function solution(my_string, overwrite_string, s) {
    var answer = '';
    var slicing_s = my_string.substring(0, s)
    var over_length = overwrite_string.length + s
    answer = slicing_s + overwrite_string + my_string.substring(over_length)
    return answer;
}