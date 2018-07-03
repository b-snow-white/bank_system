# -*- coding: utf-8 -*-
"""
@time:2018/5/12 18:08

@author: BX
"""

import json
import os
import time
from view import View
from ATM import ATM
def main():
    #管理员开机
    view=View()

    view.printAdminView()
    if view.admin1():
        return -1
    abspath = os.getcwd()
    filepath1 = os.path.join(abspath, r'allusers.txt')
    filepath2=os.path.join(abspath,r'userinfos.txt')
    f1=open(filepath1,'r+')
    r1=f1.readlines()
    f2=open(filepath2,'r+')
    r2=f2.readlines()
    #print(b)
    #print(type(b))
    allusers=json.loads(r1[0])#读出来是一个字典
    userinfos=json.loads(r2[0])
    #print('***')
    #allusers={}
    #userinfos={}
    atm=ATM(allusers,userinfos)
    while True:
        view.sysFunctionView()
        #等待用户操作
        option=input('请输入您的操作：')
        if option=='1':
            atm.createuser()
        if option=='2':
            atm.serchuserinfo()
        if option=='3':
            atm.withdrawls()
        if option=='4':
            atm.savemoney()
        if option=='5':
            atm.transer()
        if option=='6':
            atm.changepasswd()
        if option=='7':
            atm.lockuser()
        if option=='8':
            atm.unlockuser()
        if option=='9':
            atm.newcard()
        if option=='10':
            atm.killuser()
        if option=='t':
            if not view.admin1():
                # 将当前用户信息保存在文件中
                 f1=open(filepath1,'w+')
                 f1.write(json.dumps(atm.alluser,ensure_ascii=False))
                 f1.close()
                 f2 = open(filepath2, 'w+')
                 f2.write(json.dumps(atm.userinfo, ensure_ascii=False))
                 f2.close()
                 #print(atm.alluser)
                 #print(type(atm.alluser))
                 return -1


        time.sleep(2)



if __name__=='__main__':
    main()
