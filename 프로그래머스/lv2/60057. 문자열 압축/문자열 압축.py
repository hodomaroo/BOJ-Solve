# 2022-06-06
# 2022-07-29
# 문자열 압축
def solution(s):
    answer = 1000
    # 체크할 길이
    for i in range(1, len(s) + 1):
        temp_str = []
        temp = ""
        cnt = 1
        #print(i)
        for j in range(0, len(s), i):
            string = s[j:j+i]
            
            if not temp or temp != string:
                if temp:
                    if cnt > 1:
                        temp_str.append(str(cnt))
                    temp_str.append(temp)
            
                temp = string
                cnt = 1
            
            else:
                cnt += 1
                
        #print(i,temp_str)
        
        if cnt > 1:
            temp_str.append(str(cnt))
        temp_str.append(temp)
        answer = min(len("".join(temp_str)), answer)
        
        # /체크 
    return answer


#solution("aabbaccc")