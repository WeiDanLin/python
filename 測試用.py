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