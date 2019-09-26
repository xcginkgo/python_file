# 第四次上课程序01
#
"""
text = "秋天是美丽迷人的，秋天是五彩斑斓的。秋天是收获的季节，带给人丰收的喜悦。"
t = '秋天'
n = 0
for i in range(1, 10):
    if t in text:
        n += 1
        text = text[text.find(t)+1:]
print(n)
"""

text = "秋天是美丽迷人的，秋天是五彩斑斓的。秋天是收获的季节，带给人丰收的喜悦。"
t = '秋天'
n = 0
while t in text: 
    if t in text:
        n += 1
        text = text[text.find(t)+1:]
print(n)
