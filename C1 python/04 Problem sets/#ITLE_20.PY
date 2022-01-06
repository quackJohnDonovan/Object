high = 100
sum = 0
for i in range(1,11):
    rebond = high / 2
    if i == 1:
        # 第一次落地时，经过的距离就是高度
        every_long = high
        sum = sum + every_long
    else:
        # 后面几次落地时，经历的距离是上一次的高度
        high = high / 2
        every_long = high * 2
        sum = sum + every_long

print('第'+str(i)+'次落地时，共经过'+str(sum)+'米')
print('第'+str(i)+'次反弹'+str(rebond)+'米')


 #   100+50*2+25*2