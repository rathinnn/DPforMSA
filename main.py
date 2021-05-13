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
Penalty = ast.literal_eval(sys.argv[3])
print(Penalty)
if Penalty == []:
    usePenal = False
else:
    usePenal = True
print(sys.argv[4])
print(type(sys.argv[4]))
Strings = ast.literal_eval( sys.argv[4] )
MAlign(Strings,Penalty,d,usePenal)
#print(verify(Strings,Penalty,usePenal))