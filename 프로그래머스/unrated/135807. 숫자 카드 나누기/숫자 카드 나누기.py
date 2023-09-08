# 최대 공약수 구하는 데에 있어 유클리드 호재법(재귀) 사용
def gcd(a, b):
    if b%a == 0:
        return a
    else:
        return gcd(b%a, a)

def gcd_result(array):
    gcd_num = array[0]
    for num in array:
        gcd_num = gcd(gcd_num, num)
    return gcd_num

# 만약 현재 숫자가 상대 행렬의 최대공약수로도 나눠진다면,
# 해당 num과 상대 카드들의 최대공약수와의 최대공약수를 구해 나눠주는 것으로 해결
def check_each_gcd(array, other_result, other_gcd):
    for num in array:
        if num % other_gcd == 0:
            other_result = other_gcd // gcd(num, other_gcd)
    return other_result
    
def solution(arrayA, arrayB):
    answer = 0
    
    result_a = gcd_result(arrayA) 
    result_a = check_each_gcd(arrayB, result_a, result_a)
    result_b = gcd_result(arrayB)
    result_b = check_each_gcd(arrayA, result_b, result_b)

    if result_a > result_b:
        answer = result_a
    elif result_a == result_b:
        answer = 0
    else:
        answer = result_b
    
    return answer
