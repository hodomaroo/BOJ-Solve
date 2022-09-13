def solution(p : str):
    def isCorrectString(string : str) -> bool:
        count = 0
        for s in string:
            count += [1,-1][s == ")"]
            
            if count < 0:
                return False
            
        return True
    
    def reverseString(string : str) -> str:
        return "".join([[")","("][s == ")"]  for s in string])
    
    def fixString(string : str) -> str:
        if string == "": return ""       
        
        count = 0 #((()))
        for i in range(len(string)): 
            count += [1,-1][string[i] == ")"]
            
            if not count: break
        
        uString = string[:i+1]
        vString = string[i+1:]

        if isCorrectString(uString):
            return uString + fixString(vString)
    
        return "(" + fixString(vString) + ")" + reverseString(uString[1:-1])
    return fixString(p)
        
                