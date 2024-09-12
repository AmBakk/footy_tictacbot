def evaluate_board(board, player):
    """
    Evaluates the current state of the board and returns the score for the given player.
    """
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return 10
        elif board[i] == board[i + 1] == board[i + 2] != '-':
            return -10

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return 10
        elif board[i] == board[i + 3] == board[i + 6] != '-':
            return -10

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return 10
    elif board[0] == board[4] == board[8] != '-':
        return -10
    if board[2] == board[4] == board[6] == player:
        return 10
    elif board[2] == board[4] == board[6] != '-':
        return -10

    # No winner yet
    return 0


def minimax(board, depth, is_maximizing, player):
    """
    Implements the minimax algorithm to find the best move for the given player.
    """
    score = evaluate_board(board, player)
    if score == 10:
        return score
    if score == -10:
        return score
    if depth == 0:
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = player
                score = minimax(board, depth - 1, False, 'O' if player == 'X' else 'X')
                board[i] = '-'
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = 'O' if player == 'X' else 'X'
                score = minimax(board, depth - 1, True, player)
                board[i] = '-'
                best_score = min(best_score, score)
        return best_score


def get_best_move(board, player):
    """
    Finds the best move for the given player using the minimax algorithm.
    """
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == '-':
            board[i] = player
            score = minimax(board, 9, False, 'O' if player == 'X' else 'X')
            board[i] = '-'
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
