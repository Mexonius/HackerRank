# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/py-the-captains-room/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

k = int(input())
seq = sorted(list(map(int, input().split())))
nrooms = len(set(seq)) # (len(seq)-1 // k) + 1

count=list()
prev=0
tmp=0
start=1
ls = len(seq)
for i in range(ls):
    if start==1:
        prev=seq[i]
        start=0

    if seq[i]==prev:
        tmp+=1
    else:
        count.append( (prev, tmp) )
        tmp=1
        prev=seq[i]

    if i==ls-1:
        count.append( (prev, tmp) )

for i in count:
    if i[1]==1:
        print(i[0])
