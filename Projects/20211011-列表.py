'''
變數：只可以存在一個值

python內建的資料結構
lists,Tuples,Dictionaries,and Sets
tuples 建立後不可修改  暫時儲存多個值
使用：（）
list 可以修改內容 可以增加元素
使用：[]
索引標籤
由右至左讀取 編號-1起
由左至右讀取 編號0起

'''
# 列表、列表用法

scores = [90,70,50,80,60]
# score1 = 90
# score2 = 70
# score3 = 50
# score4 = 80
# score5 = 60
print(scores)

# 可在列表內輸入字串&數字
friends = ["半","泉"]
things = [90,"半", True]

# 印出列表第0位
print(scores[0])

# 印出列表倒數第一位
print(scores[-1])

# 印出列表包含第0到不包含第2位的值
print(scores[0:2])

# 印出列表包含第1到不包含第4位的值
print(scores[1:4])

# 印出列表包含第1位之後所有的值
print(scores[1:])

# 印出列表不包含第4位之前所有的值
print(scores[:4])

# 一樣可套用在字串
phrase = "Hello R.Ahalf"
print(phrase[0:8])

# 將[]的位數的值更改為=後的值
scores[0] = 30
print(scores)

# 列表好用的函式

# .extend() ,將()內列表延伸在前面的列表之後
scores.extend(friends)
print(scores)

# .append() ,將()內的值出現在列表的最後
scores.append(30)
print(scores)

# .insert(,) ,將()內,後方 的值在,前方 指定的位置插入在列表中
scores.insert(2,30)
print(scores)

text = ">_<"
print(text)

a = 1
b = 2
c = 3
#a,b,c = (1,2,3) 同步建立
print(a)
list1=['H','e','l','l','o', 'W','o','r','l','d']
list1[0]
print(list1[3:5]) #輸出 3,4不包含5
print(list1[2:]) #輸出 2之後全部
print(list1[:3]) #輸出 3之前 不包含3

nb = ['筆記電腦', '商用筆電']
mobile = ['APPLE', 'ASUS', 'HTC']
home = [3, '冰箱', 2, '洗衣機']
all3c = [nb, mobile, home]

nums = 5
scores = []
sum = 0

for i in range(nums): #執行次數
    inputValue = int(input(f"請輸入第{i+1}位學生的資料:")) #f#格式化字串 > f"字串"   f"國文：{c},數學{d},英文{e}"
    scores.append(inputValue)

for na in scores:
    sum += na
ave = sum / nums
print("全班總成績為{0:d}分,平均為{1:.2f}分".format(sum,ave))

import random

students = []
for _ in range(5):
    scores = []
    for _ in range(5):
        scores.append(random.randint(50,100))
    students.append(scores)
print(students)

studentId = 0
for stu in students:
    studentId += 1
    print(f"學生:{studentId}")
    print(stu)
    sum = 0
    for score in stu:
        sum += score
    print("總分為:{0:d},平均為:{1:.2f}".format(sum, sum/5))
    print()

cities = ['台北', '台中', '高雄']
cities.append('台南')
print(cities)

cities = ['台北', '台中', '高雄', '台南']
others = ['花蓮', '台東']
cities += others
print(cities)

cities = ['台北', '台中', '高雄', '台南']
others = ['花蓮', '台東']
cities.extend(others)
print(cities)

#實體方法insert()

citys = ['台北', '台中', '高雄']
citys.insert(0,'台南')
print(citys)

#實體方法pop() 
citys = ['台北', '台中', '高雄', '台南', '花蓮']
citys.pop() #砍最後一位
print(citys)

citys = ['台北', '台中', '高雄', '台南', '花蓮']
citys.pop(0)
print(citys)

#del 
citys = ['台北', '台中', '高雄', '台南', '花蓮']
del citys[4]
print(citys)

#remove()
all3c = ['筆記電腦', '商用筆電', 'APPLE', 'ASUS', 'HTC'] 
all3c.remove('APPLE')
print(all3c)

marxes =  ['Groucho', 'Chico', 'Harpo'] 
sorted_marxes = sorted(marxes)
sorted_marxes

marxes =  ['Groucho', 'Chico', 'Harpo']
marxes.sort()
marxes

num2 = [3, 8, 11, 7, 9 , 5]
sorted(num2,reverse=True)

integers = list()
nums = int(input("請輸入數值:"))
for i in range(nums):
    inputNum = int(input(f'請輸入第{i+1}數值:'))
    integers.append(inputNum)
#排序
integers.sort()

#顯示
for item in integers:
    print(item,end='  ')

#Dictionary


codes = {
    'tw':'Taiwan',
    'jp':'Japan',
    'hk':'Hong Kong'}
codes

import random
students = list()
s = 0
for i in range(5):
    scores = {}
    subjects =  ["國文","英文","數學","社會","自然"]
    for subject in subjects:
        scores[subject] = random.randint(50,100)
    
    students.append(scores)
print(students)

dict1 = {'a':100, 'b':200, 'c':300}
print(dict1)

del dict1['a']
print(dict1)