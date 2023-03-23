import re

# user
def YH(x):
    t1 = re.match("^[a-zA-Z0-9]{6,12}$",x)
    return t1

print(YH("ashdua913"))

# password
def MM(x):
    t2 = re.match("^[a-zA-Z0-9]{9,18}$",x)
    return t2
print(MM("dsjasj8894"))

# 手机号
def SJ(x):
    t3 = re.match("^1[3-9]\d{9}$",x)
    return t3

print(SJ("17847374657"))






