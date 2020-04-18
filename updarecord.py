import urllib.request
import json
import socket
from godaddypy import Client, Account

ip_addr="114.114.114.114"
api_url = 'https://api.godaddy.com/v1/domains/wangxidi.xyz/records';

my_acct = Account(api_key='9ZpSAWHNdgi_9AhPY28hRQ8pheBoNarWk', api_secret='MYBoT7zYoSxRNV4v91Z4CN')
client = Client(my_acct)

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip


client.update_ip(get_host_ip(), domains=['wangxidi.xyz'])



