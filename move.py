#-*- coding:utf-8 -*-  

import os
import sys
import codecs
import chardet
import linecache
import binascii
import serial
import time
import shutil

#将路径下面的所有文件，从原来的格式变为UTF-8的格式
def list_files(path):
    list_files = []
    for root,dirs,files in os.walk(path):
        for file in files:
            file_name = os.path.join(root,file)
            list_files.append(file_name)
            print(file_name)
    # print(list_files)
    return list_files


if __name__ == "__main__":
    path = r'..\User'
    path = sys.argv[1]
    print(path)
    list_files = list_files(path)
    # print(list_files)
    
    for i in list_files:
        # print(i)
        name = i.rsplit('\\',-1)[-1]
        if(i.count('\\') > 2):
            shutil.move(i, path+name)