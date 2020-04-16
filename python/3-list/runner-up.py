# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

    # TEST CASE #6
    # INPUT:
    # 3
    # 50 100 50
    # OUTPUT:
    # 50

    #  TUTTO PERFETTO TRANNE: sbagliato a mettere max(arr)<100 ANZICHE max(arr)<=100 e min(arr)>=-100

if __name__ == '__main__':
    n = int(input())
    arr = list( map(int, input().split()) )

    if 2<=n<=10 and min(arr)>-100 and max(arr)<=100:
        max_score=max(arr)
        # runner_up=0
        # for x in arr:
        #     if runner_up < x < max_score:
        #         runner_up = x

        # not so good this resolurion, because i delete items
        # because n is no bigger than 10 itĺl be much better work on a copy of arr
        arr.sort()
        for i in range( len(arr) ):
            popped = arr.pop()
            if popped < max_score:
                print(popped)
                exit()
        