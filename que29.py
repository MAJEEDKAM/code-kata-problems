minute=int(input())
secs =(minute*60)
hours = secs // 3600
minutes = secs // 60 - hours * 60
print (hours,minutes)
