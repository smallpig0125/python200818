import random
num=random.randint(1,10)
print("num",num)
i=0
while i<5:
    ans=int(input("請輸入數字"))
    if ans == num:
        print("恭喜答對")
        print("你總共猜了",i,"次")
        break
    elif ans < num:
        print("太小")
    elif ans > num:
        print("太大")

    i=i+1