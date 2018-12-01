import numpy as np
temp = input("请输入我心里现在想的数字：")
guess = int(temp)
time = 0
while time <= 1 :
    guess_true=np.random.randint(1,10)
    if guess == guess_true:
        print("你可真懂我啊！")
        break
    else:
        if guess > guess_true:
            print("大了大了！")
            temp = input("请重新输入：")
            guess = int(temp)
        else:
            print("小了小了！")
            temp = input("请重新输入：")
            guess = int(temp)
    time=time+1
print("游戏结束！")
