import urllib.request
import json

ip_addr="114.114.114.114"
api_url = 'https://api.godaddy.com/v1/domains/wangxidi.xyz/records';
def update_NS(api_url,ip_addr):
   
    head = {}
  
    head['Accept'] = 'application/json'
 
    head['Content-Type'] = 'application/json'
 
    head['Authorization'] = '9ZpSAWHNdgi_9AhPY28hRQ8pheBoNarWk'

    records_a = {
    "data" : ip_addr,
    "name" : "@",
    "ttl" : 600,
    "type" : 'A',
    }
 
    records_NS01 = {
    "data" : "ns07.domaincontrol.com",
    "name" : "@",
    "ttl" : 3600,
    "type" : "NS",
    }
    records_NS02 = {
    "data" : "ns08.domaincontrol.com",
    "name" : "@",
    "ttl" : 3600,
    "type" : "NS",
    }
  
    put_data = [records_a,records_NS01,records_NS02]
  
    try:
      
        req = urllib.request.Request(api_url,headers = head,data = json.dumps(put_data).encode(),method = "PUT")
        rsp = urllib.request.urlopen(req)
      
        code = rsp.getcode()
        #判断是否成功
        if code == 200:
            print('成功更改域名解析：'+ip_addr)
        else:
            print('更改失败！')
    #原谅我偷懒。官方有400/401/422等错误，这里统一处理了
    except:
        print('错误！')
