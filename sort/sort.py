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

def split(alist):
    pivot = alist[len(alist)/2]
    # Prohazování prvků tak, aby v první části byly
    # prvky menší než pivot a v druhé části větší rovny pivotu

    l = 0
    r = len(alist)-1
    # start:
    # jdu l doprava, dokud alist[l] < pivot
    # jdu r doleva, dokud alist[l] >= pivot
    # zkontroluji, zda se mi l a r nepřekřížily
    #   pokud ano, končím
    #   pokud ne, prohodím a pokračuji znovu od startu

    # Vrací index pivota po prohazování

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
print(data)

print("Trvalo to {:.3} s".format(end-start))
