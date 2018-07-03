# -*- coding: utf-8 -*-
"""
@time:2018/5/12 18:52

@author: BX
"""
from card import card
from user import user
import random
class ATM:
    def __init__(self,allusers,userinfos):
        self.alluser=allusers
        self.userinfo=userinfos

    #新建用户功能
    def createuser(self):
        #向用户字典中添加一对键值对（卡号-用户）
        name=input('请输入您的姓名：')
        idcard=input('请输入您的身份证号：')
        phone=input('请输入您的电话号码：')
        prestoremony=int(input('请输入预存款金额：'))
        if prestoremony<0:
            print('预存款输入有误')
            return  -1
        onepasswd=input('请设置密码：')
        if not self.checkpasswd(onepasswd):
            print('密码输入错误，开户失败')
            return -1
        cardid=self.randomcardid()
        card1=card(cardid,onepasswd,prestoremony)
        user0=user(name,idcard,phone,card1)
        #0-身份证号，1-密码，2-余额，3-锁定状态
        alluser=[user0.idcard,user0.card.cardpasswd,user0.card.cardmoney,user0.card.lock]
        #0-用户名，1-电话号码，2-卡号
        userinfo=[user0.name,user0.phone,user0.card.cardid]
        #print(list(user1))
        self.alluser[cardid]=alluser
        self.userinfo[idcard]=userinfo
        print('开户成功！请记住卡号(%s)'%cardid)
    #查询功能
    def serchuserinfo(self):
        cardnum=input('请输入您的卡号：')
        #验证是否存在该卡号
        my=self.alluser.get(cardnum)
        #print(my)
        if not my:
            print('该用户不存在，查询失败')
            return -1

        #验证密码
        if not self.checkpasswd(my[1]):
            print('该卡已被锁定，请解锁后进行操作')
            my[3]=True
            return -1
        #验证是否锁定
        if my[3]:
            print('该卡已被嗦定，查询失败')
            return -1
        print('账号：%s  余额:%d'%(cardnum,my[2]))
    #取款功能
    def withdrawls(self):
        #验证卡号
        cardnum = input('请输入您的卡号：')
        my = self.alluser.get(cardnum)
        if not my:
            print('该用户不存在，取款失败！')
            return -1
        #验证密码
        if not self.checkpasswd(my[1]):
            print('该卡已被锁定，请解锁后进行操作')
            my[3]=True
            return -1
        # 验证是否锁定
        if my[3]:
            print('该卡已被嗦定，取款失败')
            return -1
        money=int(input('请输入取款金额：'))
        if money>my[2]:
            print('余额不足 ，请充钱！')
        my[2] -= money
        print('取款成功,余额为：%d'%my[2])


    def savemoney(self):
        # 验证卡号
        cardnum = input('请输入您的卡号：')
        my = self.alluser.get(cardnum)
        if not my:
            print('该用户不存在，存款失败！')
            return -1
        # 验证密码
        if not self.checkpasswd(my[1]):
            print('该卡已被锁定，请解锁后进行操作！')
            my[3] = True
            return -1
        # 验证是否锁定
        if my[3]:
            print('该卡已被嗦定，存款失败')
            return -1
        money=int(input('请输入存款金额:'))
        my[2]+=money
        print('您的余额：%d'%my[2])
     #转账功能
    def transer(self):
        cardnum = input('请输入您的卡号：')
        my = self.alluser.get(cardnum)
        if not my:
            print('该用户不存在，转账失败！')
            return -1
        # 验证密码
        if not self.checkpasswd(my[1]):
            print('该卡已被锁定，请解锁后进行操作')
            my[3] = True
            return -1
        # 验证是否锁定
        if my[3]:
            print('该卡已被锁定，转账失败！')
            return -1
        another_id=input('请输入对方卡号：')
        another= self.alluser.get(another_id)
        if not my:
            print('该用户不存在，转账失败！')
            return -1
        print('请确认收款卡号：%s'%another_id)
        t_money=int(input('请输入转账金额：'))
        select=input('确认是否转账！（y/n）')
        if select=='n':
            print('已取消转账')
        else:
            my[2]-=t_money
            another[2]+=t_money
        print('您的余额：%d'%my[2])
     # 改密功能
    def changepasswd(self):
        cardnum = input('请输入您的卡号：')
        my = self.alluser.get(cardnum)
        if not my:
            print('该用户不存在，操作失败！')
            return -1
        # 验证密码
        if not self.checkpasswd(my[1]):
            print('该卡已被锁定，请解锁后进行操作')
            my[3] = True
            return -1
        # 验证是否锁定
        if my[3]:
            print('该卡已被锁定，操作失败！')
            return -1
        new_pwd=input('请输入新密码：')
        if not self.checkpasswd(new_pwd):
            print('密码输入错误，设置密码失败！')
            return -1
        my[1]=new_pwd
        print('改密成功！请您牢记新密码：%s'%my[1])

    def lockuser(self):
        cardnum=input('请输入卡号：')
        user=self.alluser.get(cardnum)
        if not user:
            print('该卡号不存在，锁定失败')
            return -1
        if  user[3]:
            print('该卡已被嗦定，请解锁后使用')
            return -1
        if not self.checkpasswd(user[1]):
            print('该卡已被锁定，请解锁后进行操作')
            user[3]=True
            return -1
        tempidcard=input('请输入身份证号;')
        if tempidcard!=user[0]:
            print('身份证输入错误，锁定失败')
            return -1
        user[3]=True
        print('锁定成功')

    def unlockuser(self):
        cardnum=input('请输入卡号;')
        user=self.alluser.get(cardnum)
        if not user:
            print('该卡号不存在，解锁失败')
            return -1
        if not user[3]:
            print('该卡没被锁定，无需解锁')
            return -1
        if not self.checkpasswd(user[1]):
            print('密码输入错误，解锁失败')
        tempidcard = input('请输入身份证号;')
        if tempidcard != user[0]:
            print('身份证输入错误，解锁失败')
            return -1
        user[3]=False
        print('解锁成功')

    #补卡操作
    def newcard(self):
        #name=input('请输入姓名：')
        id=input('请输入身份证号：')
        myinfo=self.userinfo.get(id)
        if not myinfo:
            print('该用户不存在，操作失败')
            return -1
        new_cardid = self.randomcardid()
        new_pwd = input('请输入新密码：')
        if not self.checkpasswd(new_pwd):
            print('密码输入错误，设置密码失败！')
            return -1
        card1 = card(new_cardid, new_pwd, self.alluser.get(myinfo[2])[2])
        self.alluser[new_cardid]=[card1.cardid,card1.cardpasswd,card1.cardmoney,card1.lock]
        self.userinfo.get(id)[2]=new_cardid
        print('办卡成功，您的新卡号：%s'%new_cardid)


    #销户操作
    def killuser(self):
        cardnum = input('请输入卡号:')
        idcard=input('请输入身份证号:')
        myinfo = self.userinfo.get(idcard)
        user=self.alluser.get(cardnum)
        if not myinfo:
            print('该用户不存在，操作失败')
            return -1
        if not user:
            print('该卡号不存在，解锁失败')
            return -1
        if user[3]:
            print('该卡已被锁定，请解锁后进行操作！')
            return -1
        if not self.checkpasswd(user[1]):
            print('密码输入错误，解锁失败')

        self.alluser.pop(cardnum)
        #self.userinfo.pop(idcard)
        #self.userinfo.pop(idcard)
        self.userinfo.pop(idcard)
        #print(type(self.userinfo))
        #print(type(self.alluser))

        print('操作成功！')

    #验证密码
    def checkpasswd(self, realpasswd):
        for i in range(3):
            temppasswd = input('请输入密码：')
            if temppasswd == realpasswd:
                return True
        return False

    def randomcardid(self):
        # 卡号
        str = ''
        for i in range(6):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            str += ch
        if not self.alluser.get(str):
            return str


