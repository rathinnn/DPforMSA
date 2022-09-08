import numpy as np
def SAlign(Str1,Str2,Penalty,d):
    m = len(Str1)
    n = len(Str2)
    dp = np.zeros((m+1,n+1), dtype = int)
    tb = np.zeros((m+1,n+1), dtype = int)
    
    initiallize(dp, d, m, n, tb)
    iterate(dp, d, m, n, Penalty, Str1,Str2,tb)
    #list_as_array = np.array(dp)
    #print(list_as_array)
    print(dp[m][n])
    print()
    print(tb)
    print()
    print(dp)
    traceback(tb,dp,Str1,Str2,m,n)

def iterate(dp,d,m,n,Penalty,Str1,Str2,tb):
    
    Index = {'A':0, 'C':1, 'G':2, 'T':3}

    for i in range(1, m+1):
        for j in range(1, n+1):
            costindex1 = Index[Str1[i - 1]]
            costindex2 = Index[Str2[j - 1]]
            (dp[i][j], tb[i][j]) = custommin( dp[i - 1][j] + d, dp[i][j - 1] + d, dp[i - 1][j - 1] + Penalty[costindex1][costindex2])

def custommin(a,b,c):
    if(a < b):
        if(a < c):
            return (a, -1)
        else:

            return (c, 1)
    else:
        if(b<c):
            return (b, 0)
        else:
            return (c, 1)

def initiallize(dp, d, m, n, tb):
    for i in range(1, m + 1):
        
        dp[i][0] = dp[i - 1][0] + d
        tb[i][0] = -1
        #print(dp[i][0])
        #print(dp)

    for i in range(1, n + 1):
        dp[0][i] = dp[0][i - 1] + d
        tb[0][i] = 0

def traceback(tb, dp, Str1, Str2, m, n):
    retStr1 = ""
    retStr2 = ""
    i = m
    j = n
    mini = 0
    while(i != 0 or j != 0):
        
        minop = tb[i][j]
        (retStr1, retStr2,i,j) = selectOp(Str1, retStr1, Str2, retStr2, minop, i, j)
        
    print(retStr1)
    print(retStr2)

def selectOp(Str1, retStr1, Str2, retStr2, minop, i, j):
    if(minop == -1):
        #print('Here')
        retStr1 = Str1[i-1] + retStr1
        retStr2 = '_' + retStr2
        i = i-1
    elif(minop == 0):
        #print('Here2')
        retStr2 = Str2[j-1] + retStr2
        retStr1 = '_' + retStr1
        j = j-1
    else:
        #print('Here3')
        retStr1 = Str1[i-1] + retStr1
        retStr2 = Str2[j-1] + retStr2
        i = i-1
        j = j-1
    
    return(retStr1, retStr2, i, j)
