#!/usr/bin/python3
"""
Below is a program to solve the N queens problem
Prints all possible solutions
N must be an int greater or equal to 4.
"""

import sys


def nqueens():
    """
    Main function to handle input
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

    chessbd = [[0 for colmn in range(sizen)] for row in range(sizen)]
    solvenqueens(chessbd, 0, sizen)


def solvenqueens(chessbd, col, sizen):
    """
    solves the N queens problem
    user called the program with the wrong number of args,
    print Usage: nqueens N

    """
    if col == sizen:
        print_board(chessbd)
        return True

    respns = False
    for k in range(sizen):
        if is_safe(chessbd, k, col, sizen):
            chessbd[k][col] = 1
            respns = solvenqueens(chessbd, col + 1, sizen) or respns
            chessbd[k][col] = 0
    return respns


def is_safe(chessbd, row, col, sizen):
    """
    Checks if a queen can be placed at the given position on the chessboard
    without being attacked.
    """
    for k in range(col):
        if chessbd[row][k] == 1:
            return False

    for k, l in zip(range(row, -1, -1), range(col, -1, -1)):
        if chessbd[k][l] == 1:
            return False

    for k, l in zip(range(row, sizen, 1), range(col, -1, -1)):
        if chessbd[k][l] == 1:
            return False

    return True


def print_board(chessbd):
    """
    Prints the board with queens' positions
    prints them in the required format
    print every possible solution to the problem
    """
    queenspos = []
    for k in range(len(chessbd)):
        for l in range(len(chessbd)):
            if chessbd[k][l] == 1:
                queenspos.append([k, l])
    print(queenspos)


if __name__ == "__main__":
    nqueens()