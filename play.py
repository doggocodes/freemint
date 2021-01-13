import chess
import book
import tkinter

pvalue = {
    chess.PAWN: 100,
    chess.ROOK: 480,
    chess.KNIGHT: 330,
    chess.BISHOP: 350,
    chess.QUEEN: 955,
    chess.KING: 20000
}

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

queenEval = [
    -10, -5, -10, 0, 0, 0, -5, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -10, -5, -10, 0, 0, 0, -5, -10,
]

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

#white side pieces
pawn1 = 48
pawn2 = 49
pawn3 = 50
pawn4 = 51
pawn5 = 52
pawn6 = 53
pawn7 = 54
pawn8 = 55
pawn1value = pawnEvalWhite[pawn1] + chess.PAWN
pawn2value = pawnEvalWhite[pawn2] + chess.PAWN
pawn3value = pawnEvalWhite[pawn3] + chess.PAWN
pawn4value = pawnEvalWhite[pawn4] + chess.PAWN
pawn5value = pawnEvalWhite[pawn5] + chess.PAWN
pawn6value = pawnEvalWhite[pawn6] + chess.PAWN
pawn7value = pawnEvalWhite[pawn7] + chess.PAWN
pawn8value = pawnEvalWhite[pawn8] + chess.PAWN

knight1 = 57
knight2 = 62
knight1value = knightEvalWhite[knight1] + chess.KNIGHT
knight2value = knightEvalWhite[knight2] + chess.KNIGHT

bishop1 = 58
bishop2 = 61
bishop1value = bishopEvalWhite[bishop1] + chess.BISHOP
bishop2value = bishopEvalWhite[bishop2] + chess.BISHOP

rook1 = 56
rook2 = 63
rook1value = rookEvalWhite[rook1] + chess.ROOK
rook2value = rookEvalWhite[rook2] + chess.ROOK

queen1 = 59
queen1value = queenevalWhite[queen1] + chess.QUEEN

king1 = 60
king1value = kingevalWhite[king1] + chess.KING



# Computer always moves first for NOW
