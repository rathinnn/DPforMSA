from SA.SingleAlign import SAlign

Penalty = [[0,4,2,4],[4,0,4,2],[2,4,0,4],[4,2,4,0]]
d = 8

S1 = "AGT"
S2 = "AAGC"

SAlign(S1,S2,Penalty,d)

S1 = "TACGTCAGC"
S2 = "TATGTCATGC"

SAlign(S1,S2,Penalty,d)