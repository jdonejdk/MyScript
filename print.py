#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
import time
import serial


def print_btp(ser,prefix_name):
    f=open(prefix_name+".pec",'rb')  
    ser.write(f.read())
    f.close()
    time.sleep(0.5)
    f=open(prefix_name+".txt", 'rb')
    str = f.read().decode("gb2312").encode("utf-8")
    f.close()
    ser.write(str)

def path_list(path):
    for root, dirs, files in os.walk(path):
        list_files = []
        for file in files:
            file = os.path.splitext(file)
            file_name = os.path.join(root, file[0])
            list_files.append(file_name)
        return list_files

if __name__ == "__main__":
    path = r'..\User'
    path = sys.argv[1]
    key = sys.argv[2]
    ser = serial.Serial('COM5', 9600, timeout=0, parity=serial.PARITY_NONE, stopbits=1)
    lists = path_list(path)
    lists = list(set(lists))
    print(lists)
    for prefix_name in lists:
        if(key in prefix_name):
            print(prefix_name)
            print_btp(ser,prefix_name)
    ser.close()