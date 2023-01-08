def solution(n, lost, reserve):
    answer = 0
    arr = [1 for _ in range(n+1)]
    
    for i in lost:
        arr[i] -=1
    for i in reserve:
        arr[i] +=1
    print(arr)
    for i in range(1,n+1):
        if arr[i]: 
            answer+= 1
            print(i)
        elif arr[i-1] > 1:
            print(i)
            arr[i-1] -= 1
            answer+= 1
        elif i != n and arr[i+1]>1:          
            print(i)
            arr[i+1] -=1
            answer+=1
            
    return answer