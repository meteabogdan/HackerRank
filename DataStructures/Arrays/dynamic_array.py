import sys

line = [int(arr_temp) for arr_temp in input().strip().split(' ')]
n = line[0]
q = line[1]
arr = []
lastAns = 0

seqList = []
for i in range(n):
    seqList.append([])

for arr_i in range(q):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    if(arr_t[0] == 1):
        seqList[(arr_t[1] ^ lastAns) % n].append(arr_t[2])
    elif(arr_t[0] == 2):
        lastAns = seqList[(arr_t[1] ^ lastAns) % n][arr_t[2] %
                                                    len(seqList[(arr_t[1] ^ lastAns) % n])]
        print(lastAns)
