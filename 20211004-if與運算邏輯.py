#python 內建的function
# 可以添加參數 input([參數])
# =之前等於建立變數

# 如何使用數字、數字用法

# 加法
print(8+5)

# 減法
print(8-5)

# 乘法
print(8*5)

# 除法
print(8/5)

# //整數除法
print(8//5)

# 一樣會先乘除後加減
print(8+8*5)

# 有括號一樣會先計算
print((8+8)*5)

# 使用變數計算
number = 8
print(number+5)

# %是取餘數 ex:8/5=1...3,得3
number = 8
print(number%5)

# str() 將()內的數字或變數成為字串
number = 8
print(str(number))

# "字串"可+轉換成的字串
number = 8
print("會印出"+str(number))

# 數字不與字串相加 (為正常運行,下方計算改為字串+字串,不是計算數值)
number = 8
print("8"+str(number))

# abs(),將()絕對值
number = -8
print(abs(number))

# pow(),將()內 ,前為數值 ,後為次方
print(pow(2,4))

print(pow(2,0))

# max(),找()最大值
print(max(2,3,87,188,57,84))

# min(),找()最小值
print(min(2,3,87,188,57,84))

# round(),將()四捨五入
print(round(4.4))
print(round(4.6))

# from math import *
# 模組引入，將寫的這些程式碼新增為函式庫

from math import *

# floor(),將()內無條件捨去
print(floor(4.6))
print(floor(5.1))

# ceil(),將()內無條件進位
print(ceil(5.8))
print(ceil(6.1))

# sqrt(),將()內開根號
print(sqrt(64))
print(sqrt(36))

chinese = int(input("請輸入國文分數：")) 
#建立變數>修改資料型態類型>鍵入內容（input)
type(chinese)


# 運用邏輯
# % >餘數
print(4%3) #輸出顯示 1
# // >整數除法
print(4//3) #輸出顯示 1

n1 = int(input("請輸入被除數（整數）:"))
n2 = int(input("請輸入除數（整數,不可為0):"))
print("商:",n1 // n2,"餘數:", n1%n2)

y = 100
#複合指定運算子
y += 100
y

z = 0
y=float(input("數字1:"))
z += y
y=float(input("數字2:"))
z += y
y=float(input("數字3:"))
z += y
print=("三個數字的總和",z)

#if 判斷式 (True or Flase)
#   縮排tab鍵

#if
#elif
#else

#關係運算子 左右兩邊要有運算元
# < 小於
# <= 小於等於
# > 大於
# >= 大於等於
# == 兩邊是否等於
#!= 兩邊是否不等於

#範例 5==5 >輸出True
#條件分析語法計 單項選擇/多項選擇/雙向選擇
#單向選擇
a = 18
if a > 18:
    print("a大於18")
    print("True程式")
print("結束")

#雙向選擇
a = int(input("請輸入數字"))
if a >= 18:
    print("大於100")
else:
    print("小於100")
print("結束")

#多項選擇
age = int(input("請輸入您的年齡"))
if age > 18:
    print("您屬於青壯年")
elif age >= 12:
    print("您屬於青少年")
else:
    print("您屬於少年")
print("執行完成")

#抓區段 if age>12 and age<18:

n1 = int(input("請輸入您的成績"))
if n1 >= 101:
    n2 = "成績最高只能100分"
elif n1 >=90:
    n2 = "優"
elif n1 >= 80:
    n2 = "甲"
elif n1 >= 70:
    n2 = "乙"
elif n1 >= 60:
    n2 = "丙"
elif n1 >= 0:
    n2 = "丁"
else:
    n2 = "成績不得低於0"

print("成績類型為",n2)

#巢狀判斷
furry = True
small = True

if furry:
    if small:
        print("貓")
    else:
        print("熊")
else:
    if small:
        print("小蜥蜴")
    else:
        print("人")
#邏輯運算子
furry = True
small = True

if furry==True and small==True:
    print("貓")
elif furry==True and small==False:
    print("熊")
elif furry==False and small==True:
    print("小蜥蜴")
elif furry==False and small==False:
    print("人")
