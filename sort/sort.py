import random
import time

def test_data_ordered(n):
    return [i for i in range(n)]

def test_data_random(n):
    return [random.randint(0,1000) for _ in range(n)]

def check_sorted(alist):
    """Zkontroluje, zda je posloupnost setřízená"""
    pass

print(test_data_ordered(10))
print(test_data_random(10))

def split(alist,l,r):
    pindex = (l+r)//2
    l0 = l
    r0 = r
    pivot = alist[pindex]
    print("Pivot: {}".format(pivot))
    # Prohazování prvků tak, aby v první části byly
    # prvky menší než pivot a v druhé části větší rovny pivotu

    #l = 0
    #r = len(alist)-1

    l -= 1
    r += 1

    while True:
        # start:
        # jdu l doprava, dokud alist[l] < pivot
        l += 1
        while alist[l] < pivot:
            l += 1
        # jdu r doleva, dokud alist[l] >= pivot
        r -= 1
        while alist[r] > pivot:
            r -= 1
        #if r<l0 and alist[l] >= pivot:
        #    alist[pindex] = alist[l]
        #    alist[l] = pivot

        # zkontroluji, zda se mi l a r nepřekřížily
        print("l: {}, r: {}".format(l,r))
        if l >= r:
            # pokud ano, končím
            break
        else:
            # pokud ne, prohodím a pokračuji znovu od startu
            tmp = alist[l]
            alist[l] = alist[r]
            alist[r] = tmp

    # Vrací index pivota po prohazování
    return l-1

def split2(alist,l,r):
    #print("l: {}, r: {}".format(l,r))
    pindex = (l+r)//2
    pivot = alist[pindex]
    #print("Pivot: {}".format(pivot))
    while (l<=r):
        while (alist[l]<pivot):
            l+=1
        while (alist[r]>pivot):
            r-=1
        if l<r:
            tmp = alist[l]
            alist[l] = alist[r]
            alist[r] = tmp
        if l<=r:
            l+=1
            r-=1
    return (l,r)


def qs(alist,l,r):
    # pokud je seznam nejvýš jednoprvkový, končím
    if r-l == 1 and alist[l]>alist[r]:
        tmp = alist[l]
        alist[l] = alist[r]
        alist[r] = tmp
    if r-l <= 1:
        return
    # rozdělí seznam na části menší než pivot, pivota a >= pivotu
    #print("List pre: {}".format(alist[l:r+1]))
    (midl,midr) = split2(alist,l,r)
    #print("List post: {}".format(alist[l:r+1]))
    #print("L: {}, R: {}, midl: {}, midr: {}".format(l,r,midl,midr))
    # zarekurzí se na levou část
    qs(alist,l,midr)
    # zarekurzí se na pravou část
    qs(alist,midl,r)

def quick_sort(alist):
    qs(alist,0,len(alist)-1)

alist = [1,2,3,4,5]
quick_sort(alist)
print("Vysledek: {}".format(alist))
print()
alist = [5,4,3,2,1]
quick_sort(alist)
print("Vysledek: {}".format(alist))
print()
alist = [1,1,1,1,1]
quick_sort(alist)
print("Vysledek: {}".format(alist))
print()
alist = [1,4,1,2,8]
quick_sort(alist)
print("Vysledek: {}".format(alist))


alist = test_data_random(10)
quick_sort(alist)
print("Vysledek je {} a je : {}".format(alist == sorted(alist),alist))

for _ in range(1000):
    alist = test_data_random(1000)
    quick_sort(alist)
    if alist != sorted(alist):
        print("Sorted wrong!")
        exit(1)


def select_sort(alist):
    """Vraci setrizeny seznam"""
    for i in range(len(alist)):
        minindex = -1
        minval = 100000000
        for j in range(i,len(alist)):
            if minval > alist[j]:
                minindex = j
                minval = alist[j]
        tmp = alist[i]
        alist[i] = alist[minindex]
        alist[minindex] = tmp

data = test_data_random(10000)
start = time.time()
select_sort(data)
end = time.time()
#print(data)

print("Trvalo to {:.3} s".format(end-start))

