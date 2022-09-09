

def solution(p : str):
    def checkCorrect(p : str) -> bool:
        count = 0
        for v in p:
            if v == "(":
                count += 1
            else:
                count -= 1
            if count < 0:   return False
        return True
    
    def convertString(string : str) -> str:
        return "".join([")","("][v == ")"] for v in string)
    
    def dfs(string : str):
        print(string)
        if not string:
            return ""
        
        count = 0
        for i in range(len(string)):
            if string[i] == "(":
                count += 1
            else:
                count -= 1
                
            if not count and i:
                break
                
        front = string[:i+1]
        res = dfs(string[i+1:])
        print("dd" ,i,front,res, convertString(front[1:-1]))
        if checkCorrect(front):
            return front + res
        
        return "(" + res + ")" + convertString(front[1:-1])
    return dfs(p)            
        
    
