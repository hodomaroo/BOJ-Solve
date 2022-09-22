from collections import defaultdict

def solution(id_list, report, k):
    #한 유저 -> 다른 유저  N명 
    
    reportDict = defaultdict(set)  #USER : Reporters
    messageDict = defaultdict(int) #USER : MESSAGE
    willBeDeprecated = set()
    
    for info in report:
        reporter, reported = info.split()
        
        reportDict[reported].add(reporter)
        if len(reportDict[reported]) >= k:
            willBeDeprecated.add(reported)
        
    for reported in willBeDeprecated:
        for reporter in reportDict[reported]:
            messageDict[reporter] += 1
    
    return [messageDict[member] for member in id_list]
    
    
    