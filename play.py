
import tkinter
gameend = False

PAWN = 100
ROOK = 480
KNIGHT = 330
BISHOP = 350
QUEEN = 955
KING = 20000

ply = 0

pawnEvalWhite = [
    0, 0, 0, 0, 0, 0, 0, 0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    7, 8, 10, 15, 15, 10, 8, 7,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, -5, -10, 0, 0, -10, -5, 5,
    8, 10, 10, -20, -20, 10, 10, 8,
    0, 0, 0, 0, 0, 0, 0, 0,
]
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEvalWhite = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, -5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]
knightEvalBlack = list(reversed(knightEvalWhite))

bishopEvalWhite = [
    -40, -10, -10, -10, -10, -10, -10, -40,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -40, -10, -10, -10, -10, -10, -10, -40,
]
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0,
]
rookEvalBlack = list(reversed(rookEvalWhite))

queenEvalWhite = [
    -10, -5, -10, 0, 0, 0, -5, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -10, -5, -10, 0, 0, 0, -5, -10,
]

queenEvalBlack = list(reversed(queenEvalWhite))

kingEvalWhite = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, -10, -10, 0, 20, 20,
    20, 30, 10, 0, 0, 10, 30, 20,
]
kingEvalBlack = list(reversed(kingEvalWhite))

kingEvalEndGameWhite = [
    5, 10, 15, 20, 20, 15, 10, 5,
    5, 10, 15, 20, 20, 15, 10, 5,
    0, 0, 20, 30, 30, 20, -10, -30,
    0, 0, 30, 40, 40, 30, -10, -30,
    0, 0, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50
]
kingEvalEndGameBlack = list(reversed(kingEvalEndGameWhite))

# What I meant about crappy UI comes in here. 
# The user will have to input every single position of piece in the starting position, and also the user will need to enter in moves by a lousy system, putting in the order-coordinate of a piece (e.g. 64 instead of h1)
# 16 pawns+pieces for one side in setup

#### Maybe I'm not fully understanding what you're trying to do here, but the "starting position" is always the same, right? Why does the user have to input it?
#### another great place to use a dictionary (starting_white = {"pawn1": 48, "pawn2": 49, ...}) (your eval lines would look like pawnEvalWhite[starting_white["pawn1"] + PAWN)
#### also, is the idea to analyze the game as it's played? if that's the case, I would only have users enter the "change". For instance - if "pawn1" moves to
#### 47 (or whatever), you use the starting_[color] dictionary (or a copy of it) and only update "pawn1". 
#### SR 

#### These are all great opportunities to use for loops - it will condense your code and as long as you test them well, you'll be less prone to error - SR

#white side pieces
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


#black side pieces
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



# this next section dedicated to where a piece can move
if ply < 3:
    pawnmoves = [-8, -16]
else:
    pawnmoves = [-8]

knightmoves = [-17, -15, -10, -6, 6, 10, 15, 17]    

#while gameend == False:
    #pass
