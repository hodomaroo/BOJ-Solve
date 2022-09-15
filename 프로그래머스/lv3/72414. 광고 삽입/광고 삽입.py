def solution(play_time, adv_time, logs):
    def convertFormatToSec(time : str)  -> int:
        hh,mm,ss = map(int,time.split(":"))
        return hh * 3600 + mm * 60 + ss #초단위로 환산
    
    def convertSecToFormat(sec : int) -> str:
        
        hh = sec // 3600
        sec %= 3600
        mm = sec // 60 
        sec %= 60
        #hh mm sec -> 
        #print(hh,mm,sec)
        return ("0" if len(str(hh)) == 1 else "") +  str(hh) + ":" + ("0" if len(str(mm)) == 1 else "") +  str(mm) + ":" + ("0" if len(str(sec)) == 1 else "") + str(sec) # -> hh:mm:ss -> 포맷스트링
    
    prefix = [0] * (convertFormatToSec(play_time) + 2)
    
    
    for log in logs:
        a,b = log.split("-")
        prefix[convertFormatToSec(a) + 1] += 1 #시작시간에 현재 시청자수 + 1 표시
        prefix[convertFormatToSec(b) + 1] -= 1 #종료시간 + 1에 시청자수 - 1 표시 
        
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i-1] + prefix[i]  #누적 -> 초별 시청자 수
    
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i-1] + prefix[i]  #누적 -> i초까지의 누적 시청시간
    prefix[-1] = 0
    
    mmaxTime = 0 #최대 시청 시간
    mmaxStart = 0 #실제 영상을 넣을 시간
    
    prefix = prefix + [0]
    cvt_ad = convertFormatToSec(adv_time)
    #print(prefix[convertFormatToSec("01:00:00")])
    for i in range(convertFormatToSec(play_time) - convertFormatToSec(adv_time) + 1):        
        if prefix[i + cvt_ad] - prefix[i] > mmaxTime:
            mmaxTime = prefix[i + cvt_ad] - prefix[i]
            mmaxStart = i
    
    return convertSecToFormat(mmaxStart)

#단순히 시청자 수가 제일 많은 구간이 아님 
#어느 한 시청자의 시작지점 -> 한명이 더 보는거니까 이득!