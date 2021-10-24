
#進階的function
def menu(wine, entree, dessert):
    return {'wine':wine ,'entree':entree,'dessert':dessert}
#引數位置的呼叫
menu('白酒','牛排','蛋糕')
#引數名稱的呼叫，可以不用依照順序
menu(wine='白酒',entree='牛排',dessert='蛋糕')

#引述位置和引數名稱混合呼叫
#前面一定先用引數位置，後面再使用引數名稱
#使用引數名稱後就不可以再使用引數位置
menu('紅酒',dessert='蛋糕',entree='雞排')
#指定預設參數的值
def menu(wine, entree, dessert='奶昔'):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}
#引數位置
menu('紅酒','雞排')
#引數位置
menu('紅酒','雞排',dessert='蛋糕')
print("1","2","3")
print("1","2","3",sep='-',end='\n\n')  #7:26分＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

def print_args(*args):
    print('這是tuple',args) #tuple

print_args(1,"2",'3',4)

#**kwargs
def print_kwargs(**kwargs):
    print('這是dict:',kwargs)

print_kwargs(wine='紅酒',dessert='蛋糕',entree='牛排',abc='123')

#建立一個空的類別
class Person():
    def __init__(self,name): #建立實體
        self.name = name

    def display_name(self): 
        print(f"您的姓名是{self.name}")

p1 = Person('robert')
p2 = Person('jenny')

type(p1)
print(p1.name)
print(p2.name)

p1.display_name()

#內部的package csv json等
