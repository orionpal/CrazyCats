#crazt cats
#pieces (NESW): BHPFGFOH, BHPFGFOH, PFBFOHGH, OFBHGHPF, GFPHGHOF, BFOHBHPF, BFPHGHOF, GFOFPHBH, OFPFGHBH
#Blue Pink Green Orange ; Head Feet
#rules: arrange the cards in such a way that the heads and tails of the same color will match.
import string
import array



def solve():
    potM = -1
    uniqMs = []
    def step1((i, p)):
        NW = p
        used = [i]
        for p1 in tryVpiece(NW, used):
            step2(NW, p1[1], used+[p1[0]])
        
        #print 'for {i}:'.format(i = i)
        #print posNMs#'posNMs: {l}'.format(l = len(posNMs))
        #print posEMs#'posEMs: {l}'.format(l = len(posEMs))
        #print posSMs#'posSMs: {l}'.format(l = len(posSMs))
        #print posWMs#'posWMs: {l}'.format(l = len(posWMs))
        
    def step2(NW, WM, used):
        for p1 in tryHpiece(NW, used):
            for p2 in tryHpiece(WM, used+[p1[0]]):
                if vmatch(p1[1], p2[1]):
                    potM = p2[0]
                    step3(NW, WM, p1[1], p2[1], used+[p1[0],p2[0]])
    def step3(NW, WM, NM, M, used):
        for p1 in tryHpiece(NM, used):
            for p2 in tryHpiece(M, used+[p1[0]]):
                if vmatch(p1[1], p2[1]):
                    step4(NW, WM, NM, M, p1[1], p2[1], used+[p1[0],p2[0]])
    def step4(NW, WM, NM, M, NE, EM, used):
        for p1 in tryVpiece(WM, used):
            for p2 in tryVpiece(M, used+[p1[0]]):
                for p3 in tryVpiece(EM, used+[p1[0],p2[0]]):
                    if hmatch(p1[1],p2[1]) and hmatch(p2[1],p3[1]) and (potM not in uniqMs):
                        uniqMs.append(potM)
                        print NW
                        print NM
                        print NE
                        print WM
                        print M
                        print EM
                        print p1[1]
                        print p2[1]
                        print p3[1]
        
    j = 0
    while j<9:
        for p in pieces[j]:
            step1((j, p))
        j = j+1
    #for p1 in pieces[0]:
     #   tmp = []
      #  used = []
def tryHpiece(orig, used):
    posH = []
    for p1 in pieces:
        ind = pieces.index(p1)
        if ind not in used:
            for po in p1:
                if hmatch(orig, po):
                    posH.append((ind, po))
    return posH
def tryVpiece(orig, used):
    posV = []
    for p1 in pieces:
        ind = pieces.index(p1)
        if ind not in used:
            for po in p1:
                if vmatch(orig, po):
                    posV.append((ind, po))
    return posV

def rotateRight(piece):
    tmp = piece[2:8]
    tmp = tmp+piece[:2]
    return tmp
def rotateLeft(piece):
    tmp = piece[:6]
    tmp = piece[6:8]+tmp
    return tmp
def posO(piece):
    tmp = [piece]
    tmp.append(rotateRight(piece))
    tmp.append(rotateRight(rotateRight(piece)))
    tmp.append(rotateLeft(piece))
    return tmp

def hmatch(piece1, piece2):
    if piece1[3]=='H':
        HF = piece2[7]=='F'
        return (piece1[2]==piece2[6]) and HF
    elif piece1[3]=='F':
        HF = piece2[7]=='H'
        return (piece1[2]==piece2[6]) and HF

def vmatch(piece1, piece2):
    if piece1[5]=='H':
        HF = piece2[1]=='F'
        return (piece1[4]==piece2[0]) and HF
    elif piece1[5]=='F':
        HF = piece2[1]=='H'
        return (piece1[4]==piece2[0]) and HF

    
def isSolved(board):
    #horizontal color check
    return (hmatch(board[0],board[1])
    and hmatch(board[1],board[2])
    and hmatch(board[3],board[4])
    and hmatch(board[4],board[5])
    and hmatch(board[6],board[7])
    and hmatch(board[7],board[8])
    #vertical check
    and vmatch(board[0],board[3])
    and vmatch(board[3],board[6])
    and vmatch(board[1],board[4])
    and vmatch(board[4],board[7])
    and vmatch(board[2],board[5])
    and vmatch(board[5],board[8]))

pieces = [posO('BHPFGFOH'), posO('BHPFGFOH'), posO('PFBFOHGH'), posO('OFBHGHPF'), posO('GFPHGHOF'), posO('BFOHBHPF'), posO('BFPHGHOF'), posO('GFOFPHBH'), posO('OFPFGHBH')]
