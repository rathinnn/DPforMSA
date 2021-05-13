iters = 1
import numpy as np
import sys
from itertools import combinations
sys.setrecursionlimit(10*5)
def MAlign(AStrings,Penalty,d,usePenal):
    dimensions = []
    indexes = []
    nindexes = []
    RetStrings = []
    for AString in AStrings:
        dimensions.append(len(AString) + 1)
        indexes.append(len(AString))
        nindexes.append(len(AString))
        RetStrings.append("")

    indexes = tuple(indexes)
    memo = np.full(dimensions, -1)
    Strmemo = np.empty(dimensions, dtype = list)
    #print(memo.shape)
    Align(Penalty,memo,tuple(indexes),AStrings,RetStrings,d,Strmemo,usePenal)
    #print(memo.shape)
    #print(nindexes)
    print(Strmemo[tuple(nindexes)])
    print(memo[tuple(nindexes)])
    #print(memo)
    f = open("out.txt", "w")
    f.write(str(Strmemo[tuple(nindexes)]))
    f.close()

        
def Align(Penalty,memo,indexes,Strings,RetStrings,d,Strmemo,usePenal):
    global iters
    #print(iters)
    iters = iters + 1
    #print(indexes)
    (check,theString) = checkBaseCase(indexes)
    #print(check,theString)
    if(check == -1):
        #print('Hey')
        memo[indexes] = 0
        Strmemo[indexes] = ['']*len(indexes)
        return 0
    elif(check != -2):
        #print('Hey2 ' + str(check*d*(len(indexes)-1)))
        memo[indexes] = check*d*(len(indexes)-1)
        Strmemo[indexes] = ['_']*len(indexes)
        Strmemo[indexes][theString] = Strings[theString][0:check]
        #print(Strmemo[indexes] )
        #print(memo)
        return check*d*(len(indexes)-1)

    #print(str(indexes)+'--')
    minval = 9999
    minchar = None
    minStrsaved = None
    mind = None
    dcount = 1
    newindex = []
    for i in range(len(indexes),0,-1):
        indices = list(combinations(range(len(indexes)),i))

        
        for ind in indices:
            #print(indices)
            #print(ind,end='____')
            #print()
            previndex = newindex
            newindex = []
            for j in range(len(indexes)):
                if(j in ind and indexes[j] > 0):
                    #print('yes')
                    newindex.append(indexes[j] - 1)
                else:
                    newindex.append(indexes[j])
            newindex = tuple(newindex)
            #print(str(indexes)+'-')
            #print(newindex)
            
            #print()
            #print(memo[newindex])
            if(memo[newindex] !=- 1 and newindex!=indexes and previndex!=newindex):
                newval = memo[newindex] + getPenalty(Penalty,indexes,ind,Strings,usePenal)
                #print('Here3 ')
                
                if(newval < minval):
                    #print(newval ,end = '----==============================1 ')
                    #print(indexes)
                    #print(getPenalty(Penalty,indexes,ind,Strings,usePenal))
                    minval = newval
                    minchar = ind
                    #mind = newindex
                    minStrsaved = Strmemo[newindex]
                #else:
                    #print(newval ,end = '----==============================3 ')
                    #print()
            elif(newindex!=indexes and previndex!=newindex):
                
                newval = Align(Penalty,memo,newindex,Strings,RetStrings, d,Strmemo,usePenal) + getPenalty(Penalty,indexes,ind,Strings,usePenal)
                #print('Here4 ')
                if(newval < minval):
                    #print(newval ,end = '----==============================2 ')
                    #print(indexes)
                    #print(getPenalty(Penalty,indexes,ind,Strings,usePenal))
                    minval = newval
                    minchar = ind
                    #mind = newindex
                    minStrsaved = Strmemo[newindex]
                #else:
                    #print(newval ,end = '----==============================4 ')
                    #print()
        
    #minStr = Strmemo[mind]
    minStr = minStrsaved
    memo[indexes] = minval
    #print(minval)
    newStr = []
    EvalChars = []
    for j in range(len(indexes)):
        indic = j
        if(indic in minchar and indexes[indic] > 0):
            EvalChars.append(Strings[indic][indexes[indic] - 1])
        else:
            EvalChars.append('_')
    i=0
    #print('-')
    #print(minchar)
    #print(indexes)
    #print(minval)
    #print(mind)
    #print('-')
    #print()
    for stri in minStr:
        stri = stri + EvalChars[i]
        #sprint(stri)
        i += 1
        newStr.append(stri)
    Strmemo[indexes] = newStr
        
    return minval
        
        






def checkBaseCase(indexes):
    #print(indexes)
    count = 0
    k = -1
    ii = -1
    for i in range(len(indexes)):
        #print(i)
        if(indexes[i]!=0):
            if(count == 0):
                count += 1
                k = indexes[i]
                ii=i
            else:
                return (-2,-1)
    #print((k,li))
    return (k,ii)

def getPenalty(Penalty,indexes,indices,Strings,usePenal):
    ACGTi = {'_':0, 'A':1, 'C':2, 'G':3, 'T':4}
    #print(indices)
    #print(indexes)
    EvalChars = []
    for j in range(len(indexes)):
        indic = j
    #for indic in indexes:
        if(indic in indices and indexes[indic] > 0):
            #print('asa')
            EvalChars.append(Strings[indic][indexes[indic] - 1])
        else:
            EvalChars.append('_')
    evaluations = combinations(EvalChars,2)
    totalPenalty = 0
    if(usePenal):
        #print('Lollllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll')
        for evaluation in evaluations:
            index1 = ACGTi[evaluation[0]]
            index2 = ACGTi[evaluation[1]]
            totalPenalty += Penalty[index1][index2]

    
    else:
        
        for evaluation in evaluations:
            #print(evaluation)
            if(evaluation[0] != evaluation[1]):
                totalPenalty+=1
        #print('Lollllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll '+str(totalPenalty))

    return totalPenalty

def verify(Strings,Penalty,usePenal):
    ACGTi = {'_':0, 'A':1, 'C':2, 'G':3, 'T':4}
    totalPenalty = 0
    for i in range(len(Strings[0])):
        EvalChars = []
        for j in range(len(Strings)):

            EvalChars.append(Strings[j][i])
            
        evaluations = combinations(EvalChars,2)
        
        if(usePenal):
            #print('Lollllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll')
            for evaluation in evaluations:
                index1 = ACGTi[evaluation[0]]
                index2 = ACGTi[evaluation[1]]
                totalPenalty += Penalty[index1][index2]
        else:
            for evaluation in evaluations:
                #print(evaluation)
                if(evaluation[0] != evaluation[1]):
                    totalPenalty+=1
    
    return totalPenalty
    


    