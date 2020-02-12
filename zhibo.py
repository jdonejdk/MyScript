#-*- coding:utf-8 -*-  
import sys
import time
import json
import chardet
import requests
from prettytable import PrettyTable

url = 'https://api.live.bilibili.com/ajax/msg'

form={'roomid': 21721813,
'csrf_token': 'zzzzzzzzzzz'
}

data = []
table_headers = ['UID', 'NAME', 'LEVEL','TIME','TEXT']
table = PrettyTable(table_headers) # 创建一个带有表格题头的table
# f.write(table.get_string())


try:
    while True:
        html = requests.post(url,data=form)
        jsonobj = json.loads(html.text)['data']['room']
        for i in range(100):
            try:
                jsonobj[i]
                dataTmp = [
                    str(jsonobj[i]['uid']),
                    jsonobj[i]['nickname'],
                    str(jsonobj[i]['user_level'][0]),
                    jsonobj[i]['timeline'],
                    jsonobj[i]['text']
                ]
                if dataTmp in data:
                    continue
                else:
                    data.append(dataTmp)
                    table.add_row(dataTmp)
                    print(dataTmp)
            except:
                break
        time.sleep(0.1)
except KeyboardInterrupt:
    print(table.get_string())
    with open("danmu.txt", "w+",encoding="utf-8") as f:
        f.write(table.get_string())
    f.close()
    print("logout")
    sys.exit(0)
