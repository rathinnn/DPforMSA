from SA.SingleAlign import SAlign

Penalty = [[0,1,1,1],[1,0,1,1],[1,1,0,1],[1,1,1,0]]
d = 2

S1 = "AGT"
S2 = "AAGC"

SAlign(S1,S2,Penalty,d)