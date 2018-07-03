# -*- coding: utf-8 -*-
"""
@time:2018/5/12 19:12

@author: BX
"""
class card:
    def __init__(self,cardid,cardpasswd,cardmoney):
        self.cardid=cardid
        self.cardpasswd=cardpasswd
        self.cardmoney=cardmoney
        self.lock=False
