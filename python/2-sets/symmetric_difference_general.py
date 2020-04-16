# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/symmetric-difference/problem?h_r=next-challenge&h_v=zen
m = int(input())
M = set(map(int, input().split()))

n = int(input())
N = set(map(int, input().split()))

# importante: devo indicare TUTTE le differenze
# diff() infatti ritorna solo gli elementi del set chiamante
# che non compaiono in quello messo in attributo

# NB: update e non add
# infatti difference crea un nuovo set, ma io devo aggiungere gli elementi separati
# e non l'intero set come oggetto atomico

# diff=(M.difference(N)).update( N.difference(M) )  <--- non posso farlo! update() torna un NoneType obj e non un li
diff=(M.difference(N))
diff.update( N.difference(M) ) 

for item in sorted(diff): #diff ora è una list grazie a sorted()
    print(item)