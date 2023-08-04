import os
def ziyuming(url):
    for dic in open('dic1.txt'):#字典文件要在同一目录下
        a=dic.replace('\n','')
        url1=a+"."+url
        ping=os.popen('ping '+url1).read()
        ttl="TTL"
        if ttl in ping:
            print(url1+"--->存在")
        else:
            pass
ziyuming(input("请输入你的url"))
