#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import serial
import time
# os.mkdir("data")
os.chdir("./data")
ser = serial.Serial('COM5', 9600, timeout=0, parity=serial.PARITY_NONE, stopbits=1)
qr = "C9999T1819"

PEC = b'\x02PT##-V3Z#@@#TICKT#CHKET#BOARD\r\n#1980M05R\r\n#0280F05A\r\n#0380G03A\r\n#66B6R00101'
PEC1 = b'\r\n#\r\n\x03'
tp = PEC.decode()+'1'+PEC1.decode()
print(tp)
BPP = b'\x023CP#1C01#01V\r\n#19beishu '
BPP1 = b'\r\n#02zijie '
BPP2 = b'\r\n#03custom\r\n#66'
BPP3 = b'\r\n#$\x03'
tb = BPP.decode() + '1' + BPP1.decode() + '10' + BPP2.decode() + '66C9999T1819AWUX123' + BPP3.decode()
print(tb)


for pnum in range(1,4):
    tp = PEC.decode()+str(pnum)+PEC1.decode()
    print(tp)
    f = open(str(pnum)+'.pec','w')
    f.write(tp)
    f.close()
    ser.write(bytes(tp, encoding='utf-8'))
    time.sleep(0.5)
    for bnum in range(10,20,10):
        # print(bnum)
        if(10 == bnum):
                qr = "C9999T181912"
        else:
                qr = qr + "C9999T1819C9999T1819"
        # print(qr)
        tb = BPP.decode()+str(pnum)+BPP1.decode()+str(bnum)+BPP2.decode()+qr+BPP3.decode()
        # print(tb)
        f = open(str(pnum)+'+'+str(bnum)+'.txt','w')
        f.write(tb)
        f.close()
        ser.write(bytes(tb, encoding='utf-8'))
        time.sleep(5)
ser.close()