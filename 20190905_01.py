#第二周python课

"""
k1 = int(input("please enter the first score:"))
k2 = int(input("please enter the second score:"))
k3 = int(input("please enter the thrid score:"))
"""


'''数据类型转换
k1 = eval(input) eval函数接受整型和实型数据
int() & float() 均为类型转换函数
''
ave = (k1 + k2 + k3) / 3
print(ave)
'''

'''
a = eval(input()) 
b = eval(input())
print(a,end="")
#end=""表示不换行
print(b)
'''

"""python的基本运算符

+、-、*、/
** : 幂
// : 取商
% : 求余
"""

'''三种除法的区分

a = int(input())
b = int(input())
print(a // b)
print(a % b)
print(a / b)

'''

'''关系运算符
关系运算符基本同C语言
>= , <= 为新增运算符
'''


'''引号
python中单、双引号可以任意使用，
但如果字符串中已经包含了一种引号，
则只能使用另一种引号来指示字符串
'''
"""
'''转义字符
\ 在行尾表示续行符
\f 换页符
\r 回车
\t 水平制表
\v 垂直制表
\0 Null
'''
"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#查找字符串、替换字符串、将字符串提取出来
"""字符串操作----索引
s[] 括号内填索引号

 0   1   2   3   4   5   正序递增索引
 p   y   t   h   o   n
-6 -5 -4 -3 -2 -1        倒序递减索引
"""

'''
test program
st='python study'
s1=st[2:8]
s2=st[2:8:2]#最后一个2为步长
s3=st[::2]#前两位缺少时，表示开始和结束
s4=st[::-1]#步长为-1表示倒过来
print(s1)
print(s2)
print(s3)
print(s4)
'''

'''分离函数split
text='学习 python 语言'
s1=text.split()#参数缺少时默认按space分
print(s1)
'''

'''
s1,s2,s3=text.split()

print(s1)
print(s2)
print(s3)
'''

'''find的用法
text='study python language'
print(text.find('study'))
print(text[text.find('study'):text.find('study')+5])
'''

'''
text='study python language'
a='study' in text
b='study' not in text
print(a,b)
s1=text.replace('study','train')#在train后有可选参数为替换次数
print(s1)
'''


#split左闭右开
#方法find  replace  split
#字符串查找、替换、分片

#---------------------------------------------------------------------------------------------

'''字符串操作
+与*
'''

text='study python language'
s1 = max(text)
print(s1)
s2=len(text)
print(s2)
#此处有语法高亮，max为内置函数

'''求sqrt(2)
import math
a=math.sqrt(2)
print(a)
'''



















