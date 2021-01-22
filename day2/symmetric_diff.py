a=int(input())
m=set([int(i) for i in input().split(" ")])
b=int(input())
n=set([int(i) for i in input().split(" ")])
g=m.union(n)
h=m.intersection(n)
sym = g-h
sym1=sorted(sym)
for i in sym1:
    print(i)