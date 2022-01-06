'''

求1～100间所有偶数的和（亦可奇数和，使用while循环写）
'''

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i += 1
print(sum)