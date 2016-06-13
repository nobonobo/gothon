def hoge():
    print('hoge')

def func(a):
    hoge()
    if a:
        print(a-1)
        return 1
    return 0

def range(n):
    i = 0
    while i<n:
        print(i)
        i+=1

#range(5)
a = 'moge'
a += '!'
print(a)