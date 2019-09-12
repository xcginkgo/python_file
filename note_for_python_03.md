# 零、基础部分，与C语言的差异
## 关于自增、自减
**i++ & i--这类语句在python中不被允许**
## 函数range()

>#计算1到20中能被3整除的数之和
```
s = 0
for i in range(1, 10):
	if i % 3 == 0:
		s+=i
print(s)
```
## 换行书写
**若字符串需要跨行，则使用左右三个引号**
>例如
```
text = """hello
my name is xc"""

print(text)
```

#### 注意

该跨行字符串中的回车有效，即print的输出结果为
```
hello
my name is xc
```
如果需要换行而忽略回车，应该
```
text = "hello\
 my name is xc"
```
**以反斜杠结尾表示换行书写在非字符串时也有效**

---
# 一、算法
算法就是解决问题的方法，此部分内容与C语言重合。
## 程序设计三大结构
1. 顺序结构
2. 分支结构
3. 循环结构
---
# 二、python模块
## 载入模块
```
import random
```

## 取一个别名

```
import random as A
```

---
# 三、选择结构
## 判断
```
if 判断条件:
	语句1
	语句2
	...
	语句n
```

## 双分支选择结构
if 条件表达式:
	语句序列
else 
	语句序列

## 多分支选择结构
```
if 条件1:
elif 条件2:
else:
```
---

# 四、循环结构
## while 循环语句
eg:

```

```

## for 循环(遍历循环)
eg:

```
for i in range(1,10):
	i = i+2
	print(i)

```
**for循环内部循环变量的变化不改变原来的变化**
---
# 五、else 可以与for 对齐（搭配），break的使用
```
for :
	c
else:
	p
```

```
s=6
flag=1
for i in range(2,7):
	if s % i == 0:
		flag=0
		break
else :
	print("yes")

```


被break中断时不进入else，自然退出时进入else
