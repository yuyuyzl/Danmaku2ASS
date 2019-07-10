import re
import assconfig
def doFilter(file,regex):

    res=[]
    for line in file.readlines():
    # .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
        spls=line.rstrip().split(" ",2)
        if(len(spls)>1):
            matchObj = re.search(regex, spls[1])
            if matchObj:
                #print(matchObj.group())
                res.append([int(spls[0]),matchObj.group()])

    return res
def gethmmss(seconds):
    h=seconds//60//60
    mm=seconds%3600//60
    ss=seconds%60
    return str(h)+":"+('%02d' % mm)+":"+('%02d' % ss)+".00"
def renderASS(filename,starttime,res):
    file=open(filename,'w',encoding='utf-8')
    print(assconfig.assTemplate,file=file)
    for tc in res:
        dialogList=assconfig.assDialogue.split(',')
        dialogList[1]=gethmmss(tc[0]-starttime)
        dialogList[2]=gethmmss(tc[0]+3-starttime)
        dialogList[9]=tc[1]
        print(','.join(dialogList),file=file)

if __name__=="__main__":
    renderASS('test.ass',1562594953,doFilter(open("test.txt",encoding='utf-8'),r'(?<=[“【]).*(?=[】”])'))
