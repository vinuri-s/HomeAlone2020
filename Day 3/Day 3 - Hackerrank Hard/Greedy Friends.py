# Written by: Amesh M Jayaweera
# amesh.17@itfac.mrt.ac.lk

MOD = 1000
n,x = map(int,input().strip().split(" "))
towns = list(map(int,input().strip().split(" ")))
q = int(input())

M = int(pow(2,x)-1)

ar = []

for gx in range(n):
    tot = 1
    for gy in range(towns[gx]):
        tot *= (M-gy)
    print(tot,end=' ')
    ar.append(tot%MOD)
print()

arrMax = max(ar)
freq = [0 for _ in range(arrMax+1)]
for i in ar:
    freq[i] += 1


subsets = {}
for i in range(arrMax):
    subsets[i] = 0

for i in range(arrMax,0,-1): 
    sub = 0
    add = freq[i]

    j = 2
    while (i*j<=arrMax):
        add += freq[j*i]
        sub += subsets[j*i]
        j+=1
    subsets[i] = (1<<add) - 1 - sub


if q > arrMax:
    print(0)
else:
    ans = subsets[q]
    print(ans)
