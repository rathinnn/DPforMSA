import numpy as np
def SAlign(Str1,Str2,Penalty,d):
    m = len(Str1)
    n = len(Str2)
    dp = np.zeros((m+1,n+1),dtype = int)
    tb = np.zeros((m+1,n+1),dtype = int)
    
    initiallize(dp,d,m,n,tb)
    iterate(dp,d,m,n,Penalty,Str1,Str2,tb)
    #list_as_array = np.array(dp)
    #print(list_as_array)
    print(dp[m][n])
    print(tb)
    print(dp)

def iterate(dp,d,m,n,Penalty,Str1,Str2,tb):
    
    Index = {'A':0,'C':1,'G':2,'T':3}


    for i in range(1,m+1):
        for j in range(1,n+1):
            costindex1 = Index[Str1[i - 1]]
            costindex2 = Index[Str2[j - 1]]
            (dp[i][j],tb[i][j]) = custmin( dp[i - 1][j] + d, dp[i][j - 1] + d, dp[i - 1][j - 1] + Penalty[costindex1][costindex2] , Str1[i-1]==Str2[j-1])


def custmin(a,b,c,match):
    if(a<b):
        if(a<c):
            return (a,0)
        else:

            if(match):
                return (c,1)
            else:
                return (c,-1)
    else:
        if(b<c):
            return (b,0)
        
        else:
            if(match):
                return (c,1)
            else:
                return (c,-1)


def initiallize(dp,d,m,n,tb):
    for i in range(1,m + 1):
        
        dp[i][0] = dp[i - 1][0] + d
        tb[i][0] = 0
        #print(dp[i][0])
        #print(dp)

    for i in range(1,n + 1):
        dp[0][i] = dp[0][i - 1] + d
        tb[0][i] = 0

