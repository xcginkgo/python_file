list1 = []
list2 = [1, 2, 3, 'thor', [12, 34, 5.7]]
'''
print(list2[4][1])
print(list2)
print(list2[3])
print(list2[1:4])
'''
string = 'hello, world'
for i in string:
    print(i)

sc = []
pe = 0
a = int(input('请输入成绩'))
while a != -1:
    sc.append(a)
    pe += 1
    a = int(input('请输入成绩'))
print(max(sc))
print(min(sc))
print(sum(sc)/pe)
