# -*- coding: utf-8 -*-

from auto import *

# 在这个文件中写你的脚本
# 我已经尽可能让脚本和自然语言差不多了


# 脚本写在这个函数里
def 脚本():
    尼禄祭本战孔明_自动版()


def 尼禄祭本战孔明_自动版():
    设置阵容([
        '大英雄',
        '弓凛',
        '孔明1',
        '骑金时',
        '孔明2',
        '占位从者'
    ])
    使用技能('大英雄', 3)
    宝具('大英雄')
    使用技能('孔明1', 3)
    使用技能('孔明1', 1, 目标='弓凛')
    使用技能('咕哒', 3)
    换人('孔明1', '孔明2')
    使用技能('孔明2', 3)
    使用技能('孔明2', 1, 目标='骑金时')
    使用技能('弓凛', 3)
    使用技能('弓凛', 2)
    使用技能('弓凛', 1)
    使用技能('骑金时', 2)
    使用技能('骑金时', 1)
    使用技能('咕哒', 1)
    宝具('骑金时', 敌对目标=2, 选卡策略=[
        ['骑金时-宝具', '任意-任意', '弓凛-任意'],
        ['骑金时-宝具', '骑金时-任意', '骑金时-任意'],
        ['骑金时-宝具', '任意-任意', '骑金时-任意']
    ])
    # 如果有4张孔明的卡1张金时的卡，或者5张孔明的卡就认命
    # 等待(16.0) 开启自动选卡之后会自动等待
    宝具('弓凛')


def 尼禄祭本战孔明():
    设置阵容([
        '大英雄',
        '弓凛',
        '孔明1',
        '骑金时',
        '孔明2',
        '占位从者'
    ])
    使用技能('大英雄', 3)
    宝具('大英雄')
    使用技能('孔明1', 3)
    使用技能('孔明1', 2)
    使用技能('孔明1', 1, 目标='弓凛')
    使用技能('咕哒', 3)
    换人('孔明1', '孔明2')
    使用技能('孔明2', 3)
    使用技能('孔明2', 2)
    使用技能('孔明2', 1, 目标='骑金时')   
    使用技能('弓凛', 3)
    使用技能('弓凛', 2)
    使用技能('弓凛', 1)
    使用技能('骑金时', 2)
    使用技能('骑金时', 1)
    使用技能('咕哒', 1)
    宝具('骑金时', 手动选卡=True, 敌对目标=2)
    等待(16.0)
    宝具('弓凛')
    
    
    
def 尼禄祭初赛孔明():
    设置阵容([
        '大英雄',
        '弓凛',
        '孔明1',
        '黑枪',
        '孔明2',
        '占位从者'
    ])
    使用技能('孔明1', 3)
    使用技能('孔明1', 2)
    使用技能('孔明1', 1, 目标='弓凛')
    宝具('大英雄')
    使用技能('咕哒', 3)
    换人('孔明1', '孔明2')
    使用技能('黑枪', 1)
    使用技能('黑枪', 3)
    使用技能('弓凛', 1)
    使用技能('弓凛', 3)
    使用技能('孔明2', 3)
    使用技能('孔明2', 2)
    宝具('黑枪')
    等待(12.0) #24
    使用技能('咕哒', 1)
    使用技能('弓凛', 2)
    宝具('弓凛')
    
    
def 尼禄祭初赛梅林():
    设置阵容([
        '大英雄',
        '弓凛',
        '孔明',
        '黑枪',
        '梅林',
        '占位从者'
    ])
    使用技能('孔明', 3)
    使用技能('孔明', 2)
    使用技能('孔明', 1, 目标='弓凛')
    宝具('大英雄')
    使用技能('咕哒', 3)
    换人('孔明', '梅林')
    使用技能('咕哒', 1)
    使用技能('黑枪', 1)
    使用技能('黑枪', 3)
    使用技能('弓凛', 1)
    使用技能('弓凛', 3)
    使用技能('梅林', 1)
    使用技能('梅林', 3, 目标='弓凛')
    宝具('黑枪')
    等待(24.0)
    使用技能('弓凛', 2)
    宝具('弓凛')


def 小莫冲浪():
    设置阵容([
        '冲莫',
        '信长',
        '小玉',
        '占位从者1',
        '占位从者2',
        '占位从者3'
    ])
    使用技能('冲莫', 3)
    使用技能('冲莫', 2)
    使用技能('信长', 1)
    使用技能('小玉', 3, 目标='冲莫')
    宝具('冲莫')
    宝具('冲莫')
    宝具('冲莫')
