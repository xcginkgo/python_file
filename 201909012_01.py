#猜数游戏

#1 creat a number
import random
a=random.randint(1,20)
print(a)
b=int(input("guess the number"))
if a==b:
    print("Nice, you are right!")
    flag = 0
else : 
    if a > b:
        print("Too small")
    else: 
        print("Too big")
#a=random.randint(10,20)
#返回[10,20]范围内随机整数
#a=random.random()
#返回[0,1)范围内随即生成的一个实数
#a=random.randrange(2,10,2)
#在序列2,4,6,8,10中产生一个随机整数
