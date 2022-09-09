
def solution(string : str):
    minLength = len(string)#개수 표시
    
    def zipString(string : str, length : int) -> int:
        stack = []
        for i in range(0,len(string), length):
            st = string[i:i + length]
            
            if not stack or st != stack[-1][0]:
                stack.append([string[i:i + length], 1])
            else:
                stack[-1][1] += 1
        return sum(len(v1) + len(str(v2)) - (v2 == 1)  for v1,v2 in stack)
        
        
    for i in range(1,len(string) // 2 + 1):
        minLength = min(minLength, zipString(string, i))
    
    
    return minLength