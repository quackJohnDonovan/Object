'''
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
i = 0
for a in range(1,5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and b != c and c != a:
                i = i+1
                print(str(a)+str(b)+str(c))
print('共有'+str(i)+'个')