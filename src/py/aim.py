pawn1 = 48
pawn2 = 49
pawn3 = 50
pawn4 = 51
pawn5 = 52
pawn6 = 53
pawn7 = 54
pawn8 = 55
pawn1value = pawnEvalWhite[pawn1] + PAWN
pawn2value = pawnEvalWhite[pawn2] + PAWN
pawn3value = pawnEvalWhite[pawn3] + PAWN
pawn4value = pawnEvalWhite[pawn4] + PAWN
pawn5value = pawnEvalWhite[pawn5] + PAWN
pawn6value = pawnEvalWhite[pawn6] + PAWN
pawn7value = pawnEvalWhite[pawn7] + PAWN
pawn8value = pawnEvalWhite[pawn8] + PAWN

knight1 = 57
knight2 = 62
knight1value = knightEvalWhite[knight1] + KNIGHT
knight2value = knightEvalWhite[knight2] + KNIGHT

bishop1 = 58
bishop2 = 61
bishop1value = bishopEvalBlack[bishop1] + BISHOP
bishop2value = bishopEvalBlack[bishop2] + BISHOP

rook1 = 56
rook2 = 63
rook1value = rookEvalWhite[rook1] + ROOK
rook2value = rookEvalWhite[rook2] + ROOK

queen1 = 59
queen1value = queenEvalWhite[queen1] + QUEEN

king1 = 60
king1value = kingEvalWhite[king1] + KING

# Computer always moves first for NOW
#black/opponent side pieces

bpawn1 = 48
bpawn2 = 49
bpawn3 = 50
bpawn4 = 51
bpawn5 = 52
bpawn6 = 53
bpawn7 = 54
bpawn8 = 55
bpawn1value = pawnEvalBlack[bpawn1] + PAWN
bpawn2value = pawnEvalBlack[bpawn2] + PAWN
bpawn3value = pawnEvalBlack[bpawn3] + PAWN
bpawn4value = pawnEvalBlack[bpawn4] + PAWN
bpawn5value = pawnEvalBlack[bpawn5] + PAWN
bpawn6value = pawnEvalBlack[bpawn6] + PAWN
bpawn7value = pawnEvalBlack[bpawn7] + PAWN
bpawn8value = pawnEvalBlack[bpawn8] + PAWN

bknight1 = 57
bknight2 = 62
bknight1value = knightEvalBlack[bknight1] + KNIGHT
bknight2value = knightEvalBlack[bknight2] + KNIGHT

bbishop1 = 58
bbishop2 = 61
bbishop1value = bishopEvalWhite[bbishop1] + BISHOP
bbishop2value = bishopEvalWhite[bbishop2] + BISHOP

brook1 = 56
brook2 = 63
brook1value = rookEvalBlack[brook1] + ROOK
brook2value = rookEvalBlack[brook2] + ROOK

bqueen1 = 59
bqueen1value = queenEvalBlack[bqueen1] + QUEEN

bking1 = 60
bking1value = kingEvalBlack[bking1] + KING


while gameEnd == False:
##---this next section dedicated to where a piece can move
    if bpawn1 + 9 or bpawn2 + 9 or bpawn3 + 9 or bpawn4 + 9 or bpawn5 + 9 or bpawn6 + 9 or bpawn7 + 9 or bpawn8 + 9  ==  pawn1:
        pawn1moves = [-8, -9]
    elif bpawn1 + 9 or bpawn2 + 9 or bpawn3 + 9 or bpawn4 + 9 or bpawn5 + 9 or bpawn6 + 9 or bpawn7 + 9 or bpawn8 + 9  ==  pawn2:
        pawn2moves = [-8, -9]
    elif bpawn1 + 9 or bpawn2 + 9 or bpawn3 + 9 or bpawn4 + 9 or bpawn5 + 9 or bpawn6 + 9 or bpawn7 + 9 or bpawn8 + 9  ==  pawn3:
        pawn3moves = [-8, -9]
    elif bpawn1 + 9 or bpawn2 + 9 or bpawn3 + 9 or bpawn4 + 9 or bpawn5 + 9 or bpawn6 + 9 or bpawn7 + 9 or bpawn8 + 9  ==  pawn4:
        pawn4moves = [-8, -9]
    elif bpawn1 + 9 or bpawn2 + 9 or bpawn3 + 9 or bpawn4 + 9 or bpawn5 + 9 or bpawn6 + 9 or bpawn7 + 9 or bpawn8 + 9  ==  pawn5:
        pawn5moves = [-8, -9]
    elif bpawn1 + 9 or bpawn2 + 9 or bpawn3 + 9 or bpawn4 + 9 or bpawn5 + 9 or bpawn6 + 9 or bpawn7 + 9 or bpawn8 + 9  ==  pawn6:
        pawn6moves = [-8, -9]
    elif bpawn1 + 9 or bpawn2 + 9 or bpawn3 + 9 or bpawn4 + 9 or bpawn5 + 9 or bpawn6 + 9 or bpawn7 + 9 or bpawn8 + 9  ==  pawn7:
        pawn7moves = [-8, -9]
    elif bpawn1 + 9 or bpawn2 + 9 or bpawn3 + 9 or bpawn4 + 9 or bpawn5 + 9 or bpawn6 + 9 or bpawn7 + 9 or bpawn8 + 9  ==  pawn8:
        pawn8moves = [-8, -9]    
    elif bpawn1 + 7 or bpawn2 + 7 or bpawn3 + 7 or bpawn4 + 7 or bpawn5 + 7 or bpawn6 + 7 or bpawn7 + 7 or bpawn8 + 7  ==  pawn1:
        pawn1moves = [-8, -7]
    elif bpawn1 + 7 or bpawn2 + 7 or bpawn3 + 7 or bpawn4 + 7 or bpawn5 + 7 or bpawn6 + 7 or bpawn7 + 7 or bpawn8 + 7  ==  pawn2:
        pawn2moves = [-8, -7]            
    elif bpawn1 + 7 or bpawn2 + 7 or bpawn3 + 7 or bpawn4 + 7 or bpawn5 + 7 or bpawn6 + 7 or bpawn7 + 7 or bpawn8 + 7  ==  pawn3:
        pawn3moves = [-8, -7]
    elif bpawn1 + 7 or bpawn2 + 7 or bpawn3 + 7 or bpawn4 + 7 or bpawn5 + 7 or bpawn6 + 7 or bpawn7 + 7 or bpawn8 + 7  ==  pawn4:
        pawn4moves = [-8, -7]            
    elif bpawn1 + 7 or bpawn2 + 7 or bpawn3 + 7 or bpawn4 + 7 or bpawn5 + 7 or bpawn6 + 7 or bpawn7 + 7 or bpawn8 + 7  ==  pawn5:
        pawn5moves = [-8, -7]
    elif bpawn1 + 7 or bpawn2 + 7 or bpawn3 + 7 or bpawn4 + 7 or bpawn5 + 7 or bpawn6 + 7 or bpawn7 + 7 or bpawn8 + 7  ==  pawn6:
        pawn6moves = [-8, -7]            
    elif bpawn1 + 7 or bpawn2 + 7 or bpawn3 + 7 or bpawn4 + 7 or bpawn5 + 7 or bpawn6 + 7 or bpawn7 + 7 or bpawn8 + 7  ==  pawn7:
        pawn7moves = [-8, -7]
    elif bpawn1 + 7 or bpawn2 + 7 or bpawn3 + 7 or bpawn4 + 7 or bpawn5 + 7 or bpawn6 + 7 or bpawn7 + 7 or bpawn8 + 7  ==  pawn8:
        pawn8moves = [-8, -7]            
    elif ply < 3:
        pawn1moves = [-8, -16]
        pawn2moves = [-8, -16]
        pawn3moves = [-8, -16]
        pawn4moves = [-8, -16]
        pawn5moves = [-8, -16]
        pawn6moves = [-8, -16]
        pawn7moves = [-8, -16]
        pawn8moves = [-8, -16]
 
##------repetitive code in proto here DO NOT REMOVE

    else:
        pawn1moves = [-8]
        pawn2moves = [-8]
        pawn3moves = [-8]
        pawn4moves = [-8]
        pawn5moves = [-8]
        pawn6moves = [-8]
        pawn7moves = [-8]
        pawn8moves = [-8]

    knightmoves = [-17, -15, -10, -6, 6, 10, 15, 17]    

    bishopmoves = [-49, -42, -35, -28, -21, -14, -7, 7, 14, 21, 28, 35, 42, 49, 56, -63, -54, -45, -36, -27, -18, -9, 9, 18, 27, 36, 45, 54, 63]

    rookmoves = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, -56, -48, -40, -32, -24, -16, -8, 8, 16, 24, 32, 40, 48, 56]

    queenmoves = bishopmoves + rookmoves

    kingmoves = [-9, -8, -7, -1, 1, 7, 8, 9] 
