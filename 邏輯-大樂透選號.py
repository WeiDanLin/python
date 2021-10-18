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