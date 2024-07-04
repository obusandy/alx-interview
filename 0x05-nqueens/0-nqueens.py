#!/usr/bin/python3
"""
A program to solve the N queens problem.
N must be an integer greater or equal to 4
Usage: nqueens N
"""

import sys


def nqueens():
    """
    below is the Main function of n queens
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        sizen = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if sizen < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for colmn in range(sizen)] for row in range(sizen)]
    solvepositn(board, 0, sizen)


def solvepositn(board, colmn, sizen):
    """
    solves the N queens problem by placing queens on the board
    solves the nqueen
    """
    if colmn == sizen:
        print_board(board)
        return True

    respns = False
    for i in range(sizen):
        if is_safe(board, i, colmn, sizen):
            board[i][colmn] = 1
            respns = solvepositn(board, colmn + 1, sizen) or respns
            board[i][colmn] = 0
    return respns


def is_safe(board, row, colmn, sizen):
    """
    Checks if a queen can be placed at the given pos on the board
    without being attacked.
    """
    for i in range(colmn):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(colmn, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, sizen, 1), range(colmn, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_board(board):
    """
    Prints the board with queens' positions
    prints in the the required format
    """
    queenspot = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                queenspot.append([i, j])
    print(queenspot)


if __name__ == "__main__":
    nqueens()
