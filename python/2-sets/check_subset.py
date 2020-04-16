# Enter your code here. Read input from STDIN. Print output to STDOUT
ntests=int(input())
for i in range(ntests):
    a=int(input())
    A=set(map(int, input().split()))
    b=int(input())
    B=set(map(int, input().split()))
    # def of subset: A subset B iff EVERY elements of A were in B
    if len(A.intersection(B))==len(A):
        print(True)
    else:
        print(False)
