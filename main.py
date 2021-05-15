import sys
import json
from SA.SingleAlign import SAlign
from MSA.MultipleAlign import MAlign
from MSA.MultipleAlign import verify
#Penalty = [[0,4,2,4],[4,0,4,2],[2,4,0,4],[4,2,4,0]]
#d = 8

#S1 = "AATT"
#S2 = "AGT"

#SAlign(S1,S2,Penalty,d)

#S1 = "TACGTCAGC"
#S2 = "TATGTCATGC"

#SAlign(S1,S2,Penalty,d)
#print()
#d = 1
#Penalty = [[0,1,1,1,1],[d,0,1,1,1],[d,1,0,1,1],[d,1,1,0,1],[d,1,1,1,0]]
#d = 8
#Penalty = [[0,8,8,8,8],[8,0,4,2,4],[8,4,0,4,2],[8,2,4,0,4],[8,4,2,4,0]]


#S1 = "GARFIELDTHELASTFATCAT"
#S2 = "GARFIELDTHEFASTCAT"
#S3 = "GARFIELDTHEVERYFASTCAT"
#S4 = "THEFATCAT"
#S5 = "GARFIELDTHEVASTCAT"
#S1 = "TACGTCAGC"
#S2 = "TATGTCATGC"
#MAlign([S1,S2],Penalty,d,True)
#MAlign([S1,S2,S3,S4,S5],Penalty,d,False)

#print()
#V = ['GARFIELDTHELASTFATCAT_', 'GARFIELDTHEFASTCAT____', 'GARFIELDTHEVERYFASTCAT', '____________THEFATCAT_', 'GARFIELDTHEVASTCAT____'] 
#RV = ['GARFIELDTHELASTFA_TCAT', 'GARFIELDTHE____FASTCAT', 'GARFIELDTHEVERYFASTCAT', '________THE____FA_TCAT', 'GARFIELDTHE____VASTCAT'] 
#print(verify(V,Penalty,False))
#print(verify(RV,Penalty,False))
#K = ['__','GA']
#print(verify(K,Penalty,False))
import ast
n = int(sys.argv[1])
d = int(sys.argv[2])

check = sys.argv[3]
if(check != 'X'):
    matrixar = sys.argv[3].split(',')
    #Penalty = [[0] * 5]*5
    Penalty = [ [ 0 for i in range(5) ] for j in range(5) ]

    c = 0
    for i in range(5):
        for j in range(5):
            Penalty[i][j] = int(matrixar[c])
            c+=1
        
    #Penalty = ast.literal_eval(sys.argv[3])
    print(Penalty)
    usePenal = True
else:
    usePenal = False
    Penalty = []
Strings = sys.argv[4].split(',')
MAlign(Strings,Penalty,d,usePenal)
#print(verify(Strings,Penalty,usePenal))