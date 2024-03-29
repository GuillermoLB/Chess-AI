#import java.text.DecimalFormat;
#import java.util.ArrayList;
#import java.util.Random;

import sys
import random
from Position import Position
from State import *


# all the pieces
wPawn = 0
wRook = 1
wBishop = 2
wKnight = 3
wQueen = 4
wKing = 5
bPawn = 6
bRook = 7
bBishop = 8
bKnight = 9
bQueen = 10
bKing = 11
empty = 12

# number of pieces
diffPieces = 12

# name (and letter) of each piece
names = ["wPawn", "wRook", "wBishop", "wkNnight", "wQueen", "wKing", "bPawn", "bRook", "bBishop", "bkNightight", "bQueen", "bKing"]
letters = ["P","R","B","N","Q","K","p","r","b","n","q","k"," "]
# Note we use h for Horse instead of Knight
# Note we add " " for empty cell

# Get color piece
def getColorPiece(piece):

    if ((piece >=0) and (piece<=5)):
    	return 0 #white
    elif ((piece>5) and (piece<=11)):
    	return 1 #black
    else:
    	print("\n** Error, wrong piece code\n")
    	sys.exit(0)
    return -1  #never arrives here, just to avoid compilation error


# This method generates a problem instance.
# @param n size of the board
# @param p probability for each piece to be included
# @param seed to initiate the random generator (for reproducibility)
# @param agent the type of piece who will "play" the game (always white)
# @return the initial state (board and agent)

# def getProblemInstance(n, p, seed, agent): 
# 	numPieces = [8,2,2,2,1,1,8,2,2,2,1,1]
# 	board = [[empty for i in range(n)] for j in range(n)]

# 	random.seed(seed)

# 	# adjusting the number of possible  pieces according to board's size
# 	f = (n*n)/64.0

# 	for i in range(len(numPieces)):
# 		numPieces[i] = round(numPieces[i]*f)   
# 	numPieces[agent] -= 1

# 	allPositions = getAllBoardPositions(n)

# 	# placing our agent in the first row, we know these are the first n elements in allPositions
# 	r = random.randint(0,n-1)
# 	agentPos = allPositions.pop(r)
# 	board[agentPos.row][agentPos.col] = agent
			
# 	# placing the rest of pieces
# 	pos = None
# 	for piece in range(diffPieces):
# 		for j in range(numPieces[piece]):
# 			if (random.random()<=p):
# 				r = random.randint(0,len(allPositions)-1)
# 				pos = allPositions.pop(r)
# 				board[pos.row][pos.col] = piece
			
# 	# Creating the instance, i.e., the state
# 	return State(board, agentPos, agent)



#
# fill (by rows) an ArrayList with all the possible coordinates
# 
# @param n size of the board
#

def getAllBoardPositions(n):
	return [Position(r,c) for r in range(n) for c in range(n)]
	

#
# Print a state (board + agent)
#

def printBoard(state):
	#DecimalFormat df = new DecimalFormat("00");
	size = len(state.m_board[0])
	if (size>50):
		print("**Error, board too large to be text-printed ...\n")
		sys.exit(0)

	# upper row
	print("   ", end="")
	for c in range(size):
		print("% 2d " % (c), end="")
	print("")

	print("  ", end="")
	for c in range(size):
		print("---", end="")
	print("--")

	# board
	for r in range(size):
		print("% 2d|" % (r), end="")
		for c in range(size): 
			# if ((r==state.m_agentPos.row) and (c==state.m_agentPos.col)):
			# 	print("*" + letters[state.m_board[r][c]]+"|", end="")
			# else:
			print(" " + letters[state.m_board[r][c]]+"|", end="")
		# botton row
		print("  ")
		for c in range(size): 
			print("---", end="")
		print("--")


# /**
# * This method generates a random board problem to play chess.
# * @param p probability for each piece to be included
# * @param seed to initiate the random generator (for reproducibility)
# * @return the initial state (board)
# */
def getChessInstancePosition(p, seed):
	numPieces = [8,2,2,2,1,1,8,2,2,2,1,1]
	n = 8
	board = [[empty for i in range(n)] for j in range(n)]
	random.seed(seed)

	allPositions = getAllBoardPositions(n)

	# Placing the king
	r = random.randint(0,n*n)
	agentPos = allPositions.pop(r)
	board[agentPos.row][agentPos.col] = Utils.wKing
	numPieces[Utils.wKing] = -1
	r = random.randint(0,(n*n)-1)
	agentPos = allPositions.pop(r)
	board[agentPos.row][agentPos.col] = Utils.bKing
	numPieces[Utils.bKing] = -1

	# placing the rest of pieces
	pos = None
	for piece in range(diffPieces):
		for j in range(numPieces[piece]):
			if (random.random()<=p):
				r = random.randint(0,len(allPositions)-1)
				pos = allPositions.pop(r)
				board[pos.row][pos.col] = piece
			
	# Creating the instance, i.e., the state
	return State(board)	

def getChessInstance(p, seed):
	n = 8
	board = [[empty for i in range(n)] for j in range(n)]
	for i in range(n):
		board[1][i] = Utils.wPawn
		board[n-2][i] = Utils.bPawn
	# //white pieces
	board[0][0] = Utils.wRook; board[0][1] = Utils.wKnight; board[0][2]=Utils.wBishop
	board[0][n-1] = Utils.wRook; board[0][n-2] = Utils.wKnight; board[0][n-3]=Utils.wBishop
	board[0][3] = Utils.wKing; board[0][4]=Utils.wQueen
	# //black pieces
	board[n-1][0] = Utils.bRook; board[n-1][1] = Utils.bKnight; board[n-1][2]=Utils.bBishop
	board[n-1][n-1] = Utils.bRook; board[n-1][n-2] = Utils.bKnight; board[n-1][n-3]=Utils.bBishop
	board[n-1][3] = Utils.bKing; board[n-1][4]=Utils.bQueen
	# // Creating the instance, i.e., the state
	return State(board)
	






# main to test the methods

if __name__ == '__main__':

	st = getChessInstance(1.0, 2024)
	# print(st.m_board)
		
	printBoard(st)
