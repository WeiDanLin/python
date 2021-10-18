#  沒有print 的話 他是為儲存格 他會輸出 最後一行傳出的值
#  in[2]>out[2] 沒有輸出任何東西就不會有out
#  儲存格最後一行有輸出值 就會計算 但不會有out
#  del => 整行不會產生 （記憶體內的參數移除） _刪除變數
#  #<此符號後之文字 程式碼不會讀取 視同人類查看備註

import abc

print(3) #整數值
print(0.12) #浮點數
print("文字") #字串
print(1+1) #運算 ＿轉line 35
print(1,0.12,"文字",1+1) #多重參數

#參數嘗試
a = 100
print("a=",a)
b = 200
print("b=",b)
print("總和:", a+b)

# 基本資料類型(data type) 查資料類型（type)  
# 範例 
a = 10
print(type(a)) #int類型 輸出顯示<class 'int'> 
a = 10.2
print(type(a)) #float類型 輸出顯示<class 'float'>
a = "10"
print(type(a)) #str類型 輸出顯示<class 'str'>
a = True
print(type(a)) #bool類型 輸出顯示<class 'bool'>
# int > 整數值
# float > 浮點數
# str > 字串
# bool > 布林值

# 基本運算方式
# + >加法
print(2+1) #輸出顯示 3
# - >減法
print(2-1) #輸出顯示 1
# * >乘法
print(1*2) #輸出顯示 2
# / >除法
print(4/2) #輸出顯示 2.0
# // >整數除法
print(4//3) #輸出顯示 1
# % >餘數
print(4%3) #輸出顯示 1
# ** > 次方
print(4**3) #輸出顯示 64

# Python Conole
# 試算公式 試算用的 無法回測修改（僅jupyter notebook修改器可以回測修改）

# 複合指定運算子
a = 95
a -=3 #把a的內容減去3 輸出結果 print = 92
print(a)

#測試
a = 5
a **=3
print(a) #輸出結果 125

#運算子優先順序(由上至下，由左至右)
# （）
# ＊＊
# 正負
# ＊ / % //
# + -
# =

#範例
a=2 * (1+2) ** 2 - 2 ** 2 * 2
#       3
#            9        4
#         18              8
#                10
# a=10 
print(a) #輸出結果 print(a) = 10

#布林值
int(True) #輸出結果 1
int(False) #輸出結果 0
int(98.6) #輸出結果 98 (省略小數點)
int("99") #輸出結果 99(字串>數字)
int("-23") #輸出結果 -23（字串>數字）

print(int(True)) 
print(int(False)) 
print(int(98.6)) 
print(int("99")) 
print(int("-23")) 

print("單行文字範例")

#單行文字換行文字
font = "仍有不少民眾因為更改意願，至今尚未輪到疫苗預約接種，對此，指揮中心發言人莊人祥建議，\
「尚未輪到接種疫苗的民眾，可以加勾選BNT疫苗，因為接下來BNT疫苗主打第一劑，民眾可以在不更動意願的狀\
 況下，增加勾選BNT疫苗，加速接種疫苗機會。」"

print(font)

print("多行文字範例")

#多行文字(‘’‘頭三尾三)
font = '''
仍有不少民眾因為更改意願，至今尚未輪到疫苗預約接種，對此，指揮中心發言人莊人祥建議，

「尚未輪到接種疫苗的民眾，可以加勾選BNT疫苗，因為接下來BNT疫苗主打第一劑，民眾可以

在不更動意願的狀況下，增加勾選BNT疫苗，加速接種疫苗機會。」'''

print(font)

#字串相加（複合式指定運算子）
font1 = ""
font1 += "abc"
font1 += "bcd"
print(font1)

#換行 \n
#空格 \t
#""  \"

print("範例:")

font = "仍有不少民眾\n因為更改\t意願，至今\"尚未輪到疫\"苗預約接種"

print(font)

#input > 預設傳出字串
value=int(input("請輸入一個整數："))
print(type(value))

# 建立BMI計算機

# input("") 函數可以列印（顯示）字串，並等待使用者輸入文字、數字
# float() 函數可以將數字轉換為浮點數，所謂浮點數就是包含小數點的數值
# Height 和 Weight 分別是要記錄身高與體重數值的變數
Height = float(input("請輸入身高，單位為公分:"))
Weight = float(input("請輸入體重，單位為公斤:"))
# BMI 是浮點數的變數，BMI 的計算公式是體重除以身高（單位：公尺）的平方
BMI = Weight/((Height/100)**2)
# Status 初始化是空字串，Status 是字串變數
Status = ""
# 關於 if、elif、else 的說明
'''
if 條件判斷:
    程式區塊
#--------------
if 條件判斷1:
    程式區塊A
elif 條件判斷2:
    程式區塊B
#--------------
if 條件判斷1:
    程式區塊A
elif 條件判斷2:
    程式區塊B
else:           <==這代表不是條件判斷1，也不是條件判斷2
    程式區塊C
'''
if BMI < 18.5:
    Status = "太輕"
elif 18.5<=BMI<25:
    Status = "正常"
elif 25<=BMI<30:
    Status = "過重"
else:
    Status = "肥胖"
# 這裡的重點在於要將數值轉換為字串，才能用加號與其他字串做串連成一個字串，使用的函數是str()
print("your BMI is " + str(BMI) + " 您的體重" + Status)

# 建立基本計算機

#input(""),可請用戶輸入""提示內的回答
name = input("請輸入你的名字")
print("Hello,"+ name)
age = input("輸入年齡")
print("你今年"+ age +"歲")

# 此輸入是以字串顯示,故是字串1+字串2
number1 = input("輸入第一個數字:")
number2 = input("輸入第二個數字:")
print(number1 + number2)

# int(),將()內轉換為整數
number1 = input("輸入第一個數字:")
number2 = input("輸入第二個數字:")
print(int(number1) + int(number2))

# float(),將()轉換為有小數點的數值
number1 = input("輸入第一個數字:")
number2 = input("輸入第二個數字:")
print(float(number1) + float(number2))

#以上結束