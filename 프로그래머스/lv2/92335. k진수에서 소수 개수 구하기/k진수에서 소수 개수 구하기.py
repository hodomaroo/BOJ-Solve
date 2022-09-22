from collections import Counter
from math import sqrt,ceil

def solution(n, k):
    def isPrime(num : int) -> bool:
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:    return False
        return num != 1
    
    def convertDecimalTo_K_Base(num : int, k : int) -> str:
        convert_list = []
        while num:
            convert_list.append(str(num % k)) 
            num //= k
        
        return "".join(convert_list[::-1])
        
    converted = convertDecimalTo_K_Base(n, k)
    print(converted)
    return sum(isPrime(int(v)) for v in converted.split("0") if v)    
    
    #해당 숫자를 k진수로 변환하기
    #2로 / / / / / / / -> MOD를 붙이기 -> 역순으로 만들기!
    
    