def solution(places):
    ans=[]
    for place in places:
        ok=1
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    if i+1<5 and place[i+1][j]=='P':
                        ok=0
                    if j+1<5 and place[i][j+1]=='P':
                        ok=0
                    if i+2<5 and place[i+2][j]=='P' and place[i+1][j]=='O':
                        ok=0
                    if j+2<5 and place[i][j+2]=='P' and place[i][j+1]=='O':
                        ok=0
                    if i+1<5 and j+1<5 and place[i+1][j+1]=='P' and (place[i+1][j]=='O' or place[i][j+1]=='O'):
                        ok=0
                    if i+1<5 and j-1>=0 and place[i+1][j-1]=='P' and (place[i+1][j]=='O' or place[i][j-1]=='O'):
                        ok=0
                if ok==0:
                    break
            if ok==0:
                break
        ans.append(ok)
    return ans
