import random as A
a=A.randint(1,100)
b=int(input("guess the number"))
times=0
while a != b:
    times += 1#python 无++ --
    if a > b:
        print("小了")
    else:
        print("大了")
    b=int(input("再试试"))

print("猜对了", times)
