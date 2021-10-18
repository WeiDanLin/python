import random
print("猜數字遊戲開始！")
font = '''
#################################
規則：數字為1~100之間數字,整數數字
################################# '''
print(font)
a = random.randint(1,100)
min = 1
max = 100
cont =0
while(True):
    n = int(input("請輸入一個整數"))
    cont += 1
    if( n >= min and n <= max ):
        if(a < n ):
            print("數字小於",n)
            max = n-1
            print(min,"~",max)
        elif(a > n):
            print("數字大於",n)
            min = n+1
            print(min,"~",max)
        elif(a == n):
            print("答案為",a)
            break
        print("您猜了",cont,"次")
    else:
        print("請輸入",min,"~",max,"之間數字")
print("遊戲結束 恭喜您獲勝了")

'''import random
min = 1
max = 100
count = 0
target = random.randint(1,100)
print("===============猜數字遊戲==================\n")
while(True):
    count += 1
    keyin = int(input("猜數字範圍"+str(min)+"~"+str(max)+":"))
    if(keyin >= min and keyin <= max):
        if(keyin == target):
            print("賓果!猜對了, 答案是:", target)
            print("您猜了",count,"次")
            break
        elif(keyin > target):
            print("再小一點")
            max = keyin - 1
        elif(keyin < target):
            print("再大一點")
            min = keyin + 1
        print("您已經猜了", count, "次")
    else:
        print("請輸入提示範圍內的數字")

print("game over")'''