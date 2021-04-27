from SA.SingleAlign import SAlign
from MSA.MultipleAlign import MAlign
from MSA.MultipleAlign import verify
Penalty = [[0,4,2,4],[4,0,4,2],[2,4,0,4],[4,2,4,0]]
d = 8

S1 = "AATT"
S2 = "AGT"

#sSAlign(S1,S2,Penalty,d)

S1 = "TACGTCAGC"
S2 = "TATGTCATGC"

#SAlign(S1,S2,Penalty,d)

d = 1
Penalty = [[0,1,1,1,1],[d,0,1,1,1],[d,1,0,1,1],[d,1,1,0,1],[d,1,1,1,0]]

#S1 = "GARFIELDTHELASTFATCAT"
#S2 = "GARFIELDTHEFASTCAT"
#S3 = "GARFIELDTHEVERYFASTCAT"
#S4 = "THEFATCAT"
#S5 = "GARFIELDTHEVASTCAT"
#MAlign([S1,S2,S3,S4,S5],Penalty,d,False)
V = ['GARFIELDTHELASTFATCAT_', 'GARFIELDTHEFASTCAT____', 'GARFIELDTHEVERYFASTCAT', '____________THEFATCAT_', 'GARFIELDTHEVASTCAT____'] 
RV = ['GARFIELDTHELASTFA_TCAT', 'GARFIELDTHE____FASTCAT', 'GARFIELDTHEVERYFASTCAT', '________THE____FA_TCAT', 'GARFIELDTHE____VASTCAT'] 
print(verify(V,Penalty,False))
print(verify(RV,Penalty,False))
K = ['__','GA']
print(verify(K,Penalty,False))