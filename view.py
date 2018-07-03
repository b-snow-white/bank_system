# -*- coding: utf-8 -*-
"""
@time:2018/5/12 17:58

@author: BX
"""
from card import card
from user import user
import time
class View:
    admin='1'
    passwd='1'
    #def __init__(self,admin,passwd):
        #self.admin=admin
        #self.passwd=passwd
    def printAdminView(self):
        print('************************************************')
        print('*                                              *')
        print('*                                              *')
        print('*                                              *')
        print('*           欢迎登陆Snow White银行              *')
        print('*                                              *')
        print('*                                              *')
        print('*                                              *')
        print('************************************************')

    def sysFunctionView(self):
        print('************************************************')
        print('*         开户（1）             查询（2）        *')
        print('*         取款（3）             存款（4）        *')
        print('*         转账（5）             改密（6）        *')
        print('*         锁定（7）             解锁（8）        *')
        print('*         补卡（9）             销户（10）       *')
        print('*                    退出（t）                  *')
        print('************************************************')
    def admin1(self):
        inputadmin = input('请输入管理员帐号：')
        if self.admin != inputadmin:
            print('账号输入有误！')
            return -1
        inputpwd = input('请输入管理员密码：')
        if self.passwd != inputpwd:
            return -1
        print('succesful,waiting......')
        time.sleep(2)
        #return 0
