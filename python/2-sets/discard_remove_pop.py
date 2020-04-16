# soluzione BRUTTA che più RBTUTTA NON SI PUÒ, ma funzionale

n = int(input())
if 0<n<20:
    s = set(map(int, input().split()))
    N = int(input())
    if 0<N<20:
        commands=set()
        for i in range(N):
            command=list(input().split())
            if command[0]=='pop':
                s.pop()
            elif command[0]=='remove':
                s.remove(int(command[1]))
            elif command[0]=='discard':
                s.discard(int(command[1]))
            
print(sum(s))
