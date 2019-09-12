#求1到20能被3整除的数之和
s=0
for i in range(1, 20):
    if i % 3 == 0:
        s+=i
print(s)
