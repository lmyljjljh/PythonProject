import random
import sys
import os
import time

na = input('你的名字:')
name = na


# 主角属性
class Person:
    def __init__(self, na, tal, Life):
        self.name = na
        self.talent = tal
        self.lingqi = 0.0
        self.lingshi = 0.0
        self.life = Life

    def xiulian(self):
        self.lingqi += 0.08 * (1 + random.choice(talent) / 100) * self.talent


# 判断境界和寿命减少方式
def iff(s):
    if 0 <= s.lingqi < 20:
        print('境界:', '练气')
    elif 20 <= s.lingqi < 40:
        s.life += 0.9 * s.talent / 5
        print('境界:', '筑基')
    elif 40 <= s.lingqi < 60:
        s.life += 0.6 * s.talent / 5
        print('境界:', '金丹')
    elif 60 <= s.lingqi < 80:
        s.life += 0.3 * s.talent / 5
        print('境界:', '元婴')
    elif 80 <= s.lingqi < 100:
        s.life += 0.1 * s.talent / 5
        print('境界:', '分神')
    elif 100 <= s.lingqi < 150:
        s.life += 0.05 * s.talent / 5
        print('境界:', '出窍')
    elif 150 <= s.lingqi < 200:
        s.life += 0.01 * s.talent / 5
        print('境界:', '炼虚合道')
    elif s.lingqi >= 200:
        print('境界:', '渡劫圆满')
    return


# 发生的事件
def sth_happened(s, a, b, c):
    if random.choice(a) == 0:
        print(random.choice(b))
    else:
        aa = random.choice(c)
        bb = c.index(aa)
        print(aa)
        if bb == 0:
            s.talent += 1
        elif bb == 1:
            s.lingqi += 10
        elif bb == 2:
            s.lingshi += 1
        elif bb == 3:
            s.life += 10
        elif bb == 4:
            s.life -= 8
        elif bb == 5:
            s.life -= 5
        elif bb == 6:
            s.lingqi += 0.5
        elif bb == 7:
            s.lingqi += random.choice([-1, 1, 10, 20])
        elif bb == 8:
            s.lingqi += 5
    return


# INIT
talent = [1, 2, 3, 4, 5]
slife = [100, 90, 85, 95]
s = Person(name, random.choice(talent), random.choice(slife))

# 事件库
get = [0, 1]
actually_get0 = ['这一年无事发生...', '你感觉自己修为又上涨了一分', '你萌生了下山的想法', '师父收了个师妹，你想认识一下', '你觉得很无聊，于是开始学习python', '你做了个梦，梦见自己飞升了',
                 '快乐逐渐减少...']
actually_get1 = ['你获得了一本绝世功法', '师父见你修炼过慢，给了你一枚灵气丹', '走在路上，捡到了一枚下品灵石，你很高兴', '师父感觉你会老死，给了你一枚寿元丹', '你向师姐表白失败，道心受挫，寿命减少了',
                 '你向师妹表露心迹，师妹以你太丑拒绝了你', '你走在路上捡到了一枚壮阳丹', '你走在路上捡到了一枚神秘的丹药', '听说山下妖魔作祟，师父让你下山除妖，你的修为进一步提升']

# 主程序循环
for i in range(1000):
    print('第', i, '年')
    print('-----------')
    s.xiulian()
    print('姓名:  ', s.name)
    iff(s)
    print('寿命:', round(s.life, 2))
    s.life -= 1
    print('灵气值:', round(s.lingqi, 2))
    sth_happened(s, get, actually_get0, actually_get1)
    print('---------------------------')
    if s.lingqi >= 1000:
        print('修行之路，与天争寿，功成圆满，飞升而去...')
        break
    if s.life <= 0:
        print('修行之路，与天争寿，奈何时也命也，你寿终而亡...')
        break
    input("A new year...")
    print('-----------')
