#!/usr/bin/python

# Head ends here


def next_move(posr, posc, board):
    newmove = calculation(posr,posc,board)
    if(newmove != None):
        return newmove
    else:
        for squares in board:
            newmove = calculation(posr+squares,posc,board)
            if(newmove == None):
                continue
            else:
                return posr-(squares+1)
def calucation(posr,posc,board):
    startingfactor = 1
    move = None
    potentialmoves = []
    cleaningfactor = []
    for item in board:
        if(item == board[posr+1] and item == "d"):
            potentialmoves.append(board[posr+1])
            cleaningfactor.append(1)
        if(item == board[posr-1] and item == "d"):
            potentialmoves.append(board[posr-1])
            cleaningfactor.append(1)
        if(item == board[posc+1] and item == "d"):
            potentialmoves.append(board[posc+1])
            cleaningfactor.append(1)
        if(item == board[posc-1] and item == "d"):
            potentialmoves.append(board[posc[-1]])
            cleaningfactor.append(1)
    for moves in potentialmoves:
        for squares in board:
            if(squares == board[potentialmoves+1] and item == "d"):
                cleaningfactor[moves] += 0.50
            if(squares == board[potentialmoves-1] and item == "d"):
                cleaningfactor[moves] += 0.50
            if(squares == board[potentialmoves + 5] and item == "d"):
                cleaningfactor[moves] += 0.50
            if(squares == board[potentialmoves - 5] and item == "d"):
                cleaningfactor[moves] += 0.50
    for factors in cleaningfactor:
        if(cleaningfactor[factors] > startingfactor):
            startingfactor == cleaningfactor[factors]
            move = potentialmoves[factors]
        if(cleaningfactor[factors] <= startingfactor):
            potentialmoves.remove(factors)
            cleaningfactor.remove(factors)
    
            

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
