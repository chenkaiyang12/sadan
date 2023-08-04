import sys
import os
import socket

url1='-u'
args=sys.argv
help1='help'
cdn_data='-cdn'


def  cdn():
    addresses='Addresses'
    if cdn_data in args:
        cdn_number=args.index(cdn_data)
        cdn_number1=cdn_number+1
        cdn_data1=os.popen('nslookup '+args[cdn_number1]).read()
        if addresses in cdn_data1:
            print(args[cdn_number1]+"该域名存在cdn")
        else:
            print(args[cdn_number1]+"这个域名不存在cdn")

def port_scary():
    port_dic=[80,445,135,3389,21,8080,1433]
    ip='-ip'
    port='-p'

    if ip in args and port in args:
        ip_number=args.index(ip)
        ip_number1=ip_number+1
        ip_data=args[ip_number1]

        port_number=args.index(port)
        port_number1=port_number+1
        port_data=args[port_number1]
        port_dic=port_data.split(',')

        for port_dic_data in port_dic:
            port_dic_data=int(port_dic_data)
            sk = socket.socket()
            socket_data = sk.connect_ex((ip_data, port_dic_data))
            if socket_data == 0:
                print("该" + ip_data + "的" + str(port_dic_data) + "端口开放")
            else:
                pass
    elif ip in args:
        ip_number = args.index(ip)
        ip_number1 = ip_number + 1
        ip_data = args[ip_number1]

        for port1 in port_dic:
            sk=socket.socket()
            sk_data=sk.connect_ex((ip_data,port1))
            if sk_data == 0 :
                print(ip_data+"的"+str(port1)+"开放")
            else:
                pass



def ziyuming():
    if url1 in args:
        a=args.index(url1)
        args_number=a+1

        for dic in open('dic1.txt'):
            l=dic.replace('\n','')
            ttl='TTL='
            urls=l+'.'+args[args_number]

            ping=os.popen('ping  '+urls).read()
            if ttl in ping:
                print("有"+urls+'这个域名')
            else:
                pass

if help1 in args:
    print("-cdn参数指定你要判断的域名。-u 参数指定你需要爆破子域名的域名，-ip指定你要扫描的地址，-p指定你要爆破的端口（如果不指定就默认一些敏感端口）端口用逗号隔开")


if __name__ == '__main__':
    ziyuming()
    cdn()
    port_scary()
