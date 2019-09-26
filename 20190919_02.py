"""
输出金字塔
for i in range(1,5):
    print(' '*(4 - i), end="")
    print('*'*(2*i-1))
"""
n = 7
for row in range(1,n+1):
    space=' '*(10-row)
    print(space,end="")
    num=row
    while num>=1:
        print(num,end="")
        num-=1
    num = 2
    while num <= row:
        print(num,end="")
        num+=1
    print("")
