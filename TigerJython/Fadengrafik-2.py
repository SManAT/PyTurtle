from gturtle import *
from Vector2D import *
makeTurtle('sweetTurtle.gif')

# Zeichne eine Linie von A > B
def Linie(A,B):
    setPos(A)
    moveTo(B)
    
# zeichne die Begrenzungslinien und gib dir Punkte als Array zurück
def zeichneBegrenzung(A,B):
    # make copies!!
    A = list(A)
    B = list(B)
    pkts = []
    v = createVecFromPoints(A,B)
    # Verschiebevektor
    v.scalar(1/Teile)
    P = A
    setPos(P)
    for i in range(Teile+1):
        pkts.append(list(P)) #!
        moveTo(P)
        # neuen Punkt berechnen
        P[0] = P[0]+v.getX()
        P[1] = P[1]+v.getY()
    return pkts

def drawFaden(P1, P2, P3):
    # Speicher f. Zwischenpunkte
    punkte1=zeichneBegrenzung(P1, P2)
    punkte2=zeichneBegrenzung(P1, P3)
    
    # Zeichne Zwischenlinien
    for i in range(len(punkte1)-1, 0, -1):
        l = len(punkte2)-i
        #print("%s > %s" % (i, l))
        Linie(punkte1[i], punkte2[l])    
# ================================
max = 280
fac = 0.6
Teile=30

ht()
P1=[-max*fac,max]
P2=[-max*fac,-max]
P3=[max*fac, max]
drawFaden(P1,P2,P3)

P1=[max*fac,max]
P2=[-max*fac,max]
P3=[max*fac, -max]
drawFaden(P1,P2,P3)

P3=[max*fac,max]
P2=[-max*fac,-max]
P1=[max*fac, -max]
drawFaden(P1,P2,P3)

P3=[-max*fac,max]
P1=[-max*fac,-max]
P2=[max*fac, -max]
drawFaden(P1,P2,P3)
st()
    
    







