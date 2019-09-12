# 计算购书款的程序
price=10
flag=int(input("是否有会员卡，1(有),0(无)"))
books=int(input("输入购了多少本书"))
if flag:
    if books >= 5:
        total=books*0.75*price
    else :
        total=books*0.85*price
else :
    if books >= 5:
        total=books*0.85*price
    else :
        total=books*0.95*price
print("total is",total)


