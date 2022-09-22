from collections import defaultdict
from math import ceil

def solution(fees, records):
    def getTime(start : str, end : str) -> int: #분단위로 환산해 리턴
        startHour,startMinute = list(map(int,start.split(":")))
        endHour,endMinute = list(map(int,end.split(":")))
        
        return endHour * 60 + endMinute - (startHour * 60 + startMinute)
        
        #내역이 없으면 -> 23 : 59분 출차 
    
    def calculatedBill(time : int) -> int:
        time -= fees[0]
        return fees[1] + ceil((max(0,time) / fees[2])) * fees[3] 
    
    accumulatedTime = defaultdict(int)
    inOutInfo = defaultdict(list) #car_id : [start,end]
    
    
    for record in records:
        time, car_id, inOut = record.split()
        
        if inOut == "IN":
            inOutInfo[car_id] = time
        
        if inOut == "OUT":
            accumulatedTime[car_id] += getTime(inOutInfo.pop(car_id),time)
    
    for car_id in inOutInfo:
        accumulatedTime[car_id] += getTime(inOutInfo[car_id],"23:59")
    
    return [calculatedBill(accumulatedTime[car_id]) for car_id in sorted(accumulatedTime)]
        
    

#주차시간-> 분단위로 환산 필요