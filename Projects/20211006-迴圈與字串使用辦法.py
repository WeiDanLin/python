# 迴圈loop
# 下方執行完後回上方重複執行>明確知道執行次數
# for....in (迴圈)
# 不明確知道要執行幾次
# while (迴圈)
'''
boot
邏輯運算子
｜not
｜and > 同時
｜or > 或者

｜not false > true
while 後面必定會接邏輯運算子
比較運算子

範例：
1.建立變數
while 2.比較變數
｜程式區塊
｜
｜
｜3.改變變數值
'''

#字串、字串用法

#函式 function

#計算位置以0開始為第一位

# lower 字串全部改小寫
phrase = "Hello Ahalf"
print(phrase.lower())

# upper 字串全部改大寫
phrase = "Hello Ahalf"
print(phrase.upper())

# 詢問字串是否為大寫
phrase = "Hello Ahalf"
print(phrase.isupper())

# 詢問字串是否為小寫
phrase = "Hello Ahalf"
print(phrase.islower())

# 字串全部改大寫,是否全為大寫 (反之可改問.islower)
phrase = "Hello Ahalf"
print(phrase.upper().isupper())

# 字串全部改小寫,是否全為小寫 (反之可改問.isupper)
phrase = "Hello Ahalf"
print(phrase.lower().islower())

# []印出字串位置第6個的值
phrase = "Hello Ahalf"
print(phrase[6])

# .index("") 計算""內的值是第幾個 (重複以第一個為主)
phrase = "Hello Ahalf"
print(phrase.index("a"))

# .replace ("1","2") 將"2"代替"1"
phrase = "Hello Ahalf"
print(phrase.replace("l","L"))

a = 6 #建立變數
while a > 0: #a小於0 變成false
    print(a) #執行 印出a
    a -=1 #執行a-1 後 返回 a>0 執行到a<0 後停止

dep = 0
num = 0
while(dep<30000):
    num += 1
    inputnum = int(input("請輸入第" + str(num) + "個月份的存款"))
    dep += inputnum
print("恭喜您已存滿了，",num,"個月","金額共",dep,"的錢")

a = 0
b = int(input("請輸入每月需要存的錢"))
c = 0
while a < 30000:
    a += b
    c += 1
    print("第",c,"個月",a)
print("已存滿",a,"元")

'''
break > 跳出迴圈
'''

sum = 0
num = 1
while(True):
    score = int(input("請輸入第" + str(num) + "位學生的成績："))
    if(score < 0):
        break;
    num += 1
    sum += score
print(num-1,"位學生分數總和為",sum,"平均分數為",sum/(num))

'''
continue > 下方迴圈 停止運作
'''
sum = 0
num = 0
while(True):
    num += 1
    inputnum = int(input("請輸入第" + str(num) + "個數值："))
    if(inputnum < 0):
        break;
    elif(inputnum % 2 == 1):
        continue
    sum += inputnum

print("所有輸入的正偶數的加總是:",sum)

#內置工具箱   外部工具箱需透過pip下載
#工具箱有名稱  需import {工具箱名稱}.{工具名稱}

#for 自訂變數 in range(參數) ---for in 迴圈
#(5,10) >>5,6,7,8,9
#(0,10,2) >> 0,2,4,6,8

c = 1
d = 2
e = 3
#格式化字串 > f"字串"
f"國文：{c},數學{d},英文{e}"
#使用字串的方法format新寫法
"國文：{0:},數學:{1:},英文:{2:}".format(c,d,e)
#使用字串的方法format舊寫法
"國文：%d,數學:%2f,英文:%2f" % (c,d,e)

