"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    xCount = sum(i.count(X) for i in board)
    oCount = sum(i.count(O) for i in board)
    if oCount == xCount:
        return X
    else:
        return O
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    setofActions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                setofActions.add((i, j))

    return setofActions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    newBoard[action[0]][action[1]] = player(newBoard)
    return newBoard
    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            return board[row][0]

    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            return board[0][col]

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        return board[0][0]

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        return board[0][2]

    return None
    # raise NotImplementedError


def terminal(board):
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            return True

    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            return True

    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        return True

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        return True

    if all([all(row) for row in board]):
        return True

    return False

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if player(board) == X:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, +math.inf]

    if terminal(board):
        score = utility(board)
        return [-1, -1, score]

    for cell in actions(board):
        x, y = cell[0], cell[1]
        board[x][y] = player(board)
        score = minimax(board)
        board[x][y] = None
        score[0], score[1] = x, y

        if player(board) == X:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best

    # raise NotImplementedError
