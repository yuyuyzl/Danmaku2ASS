import time

file=open('qqgroupcopy.txt',encoding='utf-8')
filenew=open("test.txt","w",encoding='utf-8')
for line in file.readlines():
    ls=line.rstrip().split(" ",3)
    timestr=ls[0]+" "+ls[1]
    timeArray = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))+14*3600
    print(timeStamp)
    print(timeStamp,ls[2],file=filenew)
