先改代码用吧
随便玩玩

###GetDanmaku.py
修改第22行的live标记为https://api.vtb.wiki/v2/bilibili/live/c30faf76-bb73-5f5c-9e87-12acdd42c29c/history?time=1562596200中对应场次的Id

然后运行就会把所有弹幕都爬到文件里了

###TransFilter.py
输出ass也写到里面去了

总之按照main里面的方式调用就行

doFilter(将要被过滤的文本文件,用于过滤的正则表达式) -> 过滤结果list[[时间戳,文本],...]
renderASS(输出的ass文件名,录播开始时间对应的时间戳,结果list) -> 无输出，会生成ass文件
