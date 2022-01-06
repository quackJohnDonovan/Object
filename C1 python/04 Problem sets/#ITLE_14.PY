# 100以内的菲波那切数列
a = 0
b = 1
list = [0,1]
while True:
    c = a + b
    if c > 100:
        break
    a = b
    b = c
    list.append(c)
    print(list)
