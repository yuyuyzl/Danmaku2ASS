import urllib3
import json
def requestDanmaku(liveStr,file):

    res=[]
    offset=0
    hasMore=True
    http = urllib3.PoolManager()
    while(hasMore):
        r = http.request('get',"https://api.vtb.wiki/v2/bilibili/live/"+liveStr+"/comments",fields={'offset':offset})
        data=json.loads(r.data.decode())
        hasMore=data["HasMoreItems"]
        offset=offset+200
        for danmaku in data["Comments"]:
            print(danmaku["PublishTime"],danmaku["Content"],file=file)


        print(round(offset * 100 / data["TotalCount"],2),'%',sep="")


if __name__=="__main__":
    liveStr="l:one:live:record:14917277:1562594953"
    res=requestDanmaku(liveStr,open("test.txt","w",encoding='utf-8'))
