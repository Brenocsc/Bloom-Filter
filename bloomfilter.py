import numpy as np
import hashlib


def hash_md5(data):
    hash_object = hashlib.md5(bytes(data, encoding="ascii"))
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16) % m


def hash_sha(data):
    hash_object = hashlib.sha1(bytes(data, encoding="ascii"))
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16) % m

def prob_false_positive():
    return (1 - 2.71828182**(-2*int(calc_n())/m) ) ** 2

def calc_n():
    n = 0
    for i in range(0, m):
        if(list[i] == 1):
            n = n + 1
    return n

list = []
m = int(input('Size list:'))

for i in range(0, m):
    list.append(int(0))

while(1):
    print('\n1 - put')
    print('2 - get')
    print('3 - show list')
    op = int(input('option:'))
    if(op == 1):
        data = input('Element:')
        md5 = hash_md5(data)
        sha = hash_sha(data)
        print('md5: ' + str(md5))
        print('sha: ' + str(sha))
        list[md5] = int(1)
        list[sha] = int(1)
    if(op == 2):
        data = input('Element:')
        md5 = hash_md5(data)
        sha = hash_sha(data)
        print('md5: ' + str(md5))
        print('sha: ' + str(sha))
        if(list[md5] == int(1) and list[sha] == int(1)):
            print('maybe / probability of false positive: '+ str(round( prob_false_positive()*100, 2) )+ '%' )
        else:
            print('no')
    if(op == 3):
        for i in range(0, m):
            print('0: ' + str(list[i]))
        



