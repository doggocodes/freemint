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

knightEval = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, -5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]

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

#white
piece1 = input("enter in piece abb")
piece1loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece1, "on order-coord", piece1loc)
piece2 = input("enter in piece abb")
piece2loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece2, "on order-coord", piece2loc)
piece3 = input("enter in piece abb")
piece3loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece3, "on order-coord", piece3loc)
piece4 = input("enter in piece abb")
piece4loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece4, "on order-coord", piece4loc)
piece5 = input("enter in piece abb")
piece5loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece5, "on order-coord", piece5loc)
piece6 = input("enter in piece abb")
piece6loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece6, "on order-coord", piece6loc)
piece7 = input("enter in piece abb")
piece7loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece7, "on order-coord", piece7loc)
piece8 = input("enter in piece abb")
piece8loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece8, "on order-coord", piece8loc)
piece9 = input("enter in piece abb")
piece9loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece9, "on order-coord", piece9loc)
piece10 = input("enter in piece abb")
piece10loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece10, "on order-coord", piece10loc)
piece11 = input("enter in piece abb")
piece11loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece11, "on order-coord", piece11loc)
piece12 = input("enter in piece abb")
piece12loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece12, "on order-coord", piece12loc)
piece13 = input("enter in piece abb")
piece13loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece13, "on order-coord", piece13loc)
piece14 = input("enter in piece abb")
piece14loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece14, "on order-coord", piece14loc)
piece15 = input("enter in piece abb")
piece15loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece15, "on order-coord", piece15loc)
piece16 = input("enter in piece abb")
piece16loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", piece16, "on order-coord", piece16loc)

# black pieces
bpiece1 = input("enter in piece abb")
bpiece1loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece1, "on order-coord", bpiece1loc)
bpiece2 = input("enter in piece abb")
bpiece2loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece2, "on order-coord", bpiece2loc)
bpiece3 = input("enter in piece abb")
bpiece3loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece3, "on order-coord", bpiece3loc)
bpiece4 = input("enter in piece abb")
bpiece4loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece4, "on order-coord", bpiece4loc)
bpiece5 = input("enter in piece abb")
bpiece5loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece5, "on order-coord", bpiece5loc)
bpiece6 = input("enter in piece abb")
bpiece6loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece6, "on order-coord", bpiece6loc)
bpiece7 = input("enter in piece abb")
bpiece7loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece7, "on order-coord", bpiece7loc)
bpiece8 = input("enter in piece abb")
bpiece8loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece8, "on order-coord", bpiece8loc)
bpiece9 = input("enter in piece abb")
bpiece9loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece9, "on order-coord", bpiece9loc)
bpiece10 = input("enter in piece abb")
bpiece10loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece10, "on order-coord", bpiece10loc)
bpiece11 = input("enter in piece abb")
bpiece11loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece11, "on order-coord", bpiece11loc)
bpiece12 = input("enter in piece abb")
bpiece12loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece12, "on order-coord", bpiece12loc)
bpiece13 = input("enter in piece abb")
bpiece13loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece13, "on order-coord", bpiece13loc)
bpiece14 = input("enter in piece abb")
bpiece14loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece14, "on order-coord", bpiece14loc)
bpiece15 = input("enter in piece abb")
bpiece15loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece15, "on order-coord", bpiece15loc)
bpiece16 = input("enter in piece abb")
bpiece16loc = input("enter in the order-coord of the piece (eg. 64 for h1, 32 for h5)")
print("Confirmation: You have inputted a", bpiece16, "on order-coord", bpiece16loc)

