# Enter your code here. Read input from STDIN. Print output to STDOUT
indexes=list(map(int, input().split()))

# NB: ora alle implementazioni di array e A e B !!!
array=list(map(int, input().split())) # potrebbe avere duplicati
A=set(map(int, input().split())) # non avrà duplicati, non avrebbe senso
B=set(map(int, input().split())) # //

happyness=0
for elem in array:
    if elem in A:
        happyness+=1
    elif elem in B:
        happyness-=1
    
print(happyness)