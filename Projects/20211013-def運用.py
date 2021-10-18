# Dictionary

#{dict}
#dict()
#{key:value,key:value}
#刪除動作可以分為刪除資料、清除所有項目與刪除字典三種
#del dict[key]刪除某一個key的資料
#dict.clear()清除所有項目
#del dict刪除字典
#內容item > item in list(dictionary,set) > 輸出True or False

from typing import overload


list1 = [10,9,8,7]
6 in list1 

dict1 = {'a':100,'b':200,'c':300}
'a' in dict1

del dict1['a']
'a' in dict1
#>>輸出false

#dict 實體
#實體的屬性
#實體的方法 -keys()
#         -values()
#         -items()

#dict1 = {'a':100,'b':200,'c':300}
#dict1.keys() > 傳出list 傳出a b c
#dict1.values() > 傳出 100 200 300
#dict1.item() > 暫時得值'a':100,'b':200,'c':300

signals = {'綠燈': '走', '黃燈': '走快些', '紅燈':'停等',}

for color,action in signals.items():
    print(f'顏色:{color},行為:{action}')

#set
empty_set = set()

even_numbers = {0,2,4,6,8,8,8}
set('letters')

#呼叫function 引數名稱 真正的值
def lotadd():
    import random
    lot = set()
    while(len(lot) < 7):
        randomValue = random.randint(1, 49)
        lot.add(randomValue)
    print('本期大樂透電腦選號號碼如下：')
    lotlist = list(lot)
    for num in lotlist[:-1]:   #不包含-1
        print(num, end="   ")
    print()
    print(f'特別號為:{lotlist[-1]}')
lotadd()


def lotadd():
    import random
    lot = set()
    while(len(lot) < 7):
        randomValue = random.randint(1, 49)
        lot.add(randomValue)
    print('本期大樂透電腦選號號碼如下：')
    lotlist = list(lot)
    for num in lotlist[:-1]:   #不包含-1
        print(num, end="   ")
    print()
    print(f'特別號為:{lotlist[-1]}')
lotadd()

num = int(input('請輸入要產生的數量'))
for n in range(num):
    print(f'第{n+1}組')
    lotadd()
    print()

def func_sun():
    print("呼叫函式")

func_sun()

def do_nothing():
    pass

#有參數但沒有傳出值
def func_sum(a,b):
    c = a + b
    print(c)
func_sum(3,6)

#有參數但有傳出值
def func_sum(a,b):
    c = a + b
    print(c)
sum = func_sum(3,6)
print(sum)

def temperature(value):
    return 1.8 * value + 32
while (True):
    value = int(input('請輸入攝氏溫度'))
    result = temperature(value)
    print(f'華氏溫度{result}')

    inputValue = input("程式還要繼續嗎？（輸入N結束）")
    if inputValue == 'N':
        break;

print("over")

number_list = []
for i in range(5):
    num = number_list.append(i+1)

#comprehension語法
[i+1 for i in range(5)]

[i for i in range(20) if i%2 == 0]

[(i,j) for i in range(5) for j in range(6)]

import random
[{subject:random.randint(50,100) for subject in ['a','b','c']} for _ in range(50)]

import random
[[random.randint(50,100) for _ in range(5)]for _ in range(50)]