def check_win(board_state, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for condition in win_conditions:
        if board_state[condition[0]] == board_state[condition[1]] == board_state[condition[2]] == symbol:
            return True
    return False


def is_board_full(board_state):
    return "" not in board_state


def minimax(board_state, depth, is_maximizing, user_symbol, opponent_symbol):
    if check_win(board_state, user_symbol):
        return 1
    if check_win(board_state, opponent_symbol):
        return -1
    if is_board_full(board_state):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(len(board_state)):
            if board_state[i] == "":
                board_state[i] = user_symbol
                score = minimax(board_state, depth + 1, False, user_symbol, opponent_symbol)
                board_state[i] = ""
                best_score = max(score, best_score)
        return best_score

    else:
        best_score = float('inf')
        for i in range(len(board_state)):
            if board_state[i] == "":
                board_state[i] = opponent_symbol
                score = minimax(board_state, depth + 1, True, user_symbol, opponent_symbol)
                board_state[i] = ""
                best_score = min(score, best_score)
        return best_score


def find_best_move(board_state, user_symbol):
    """
    Finds the best move using the Minimax algorithm.
    :param board_state: Current board as a list (e.g., ["", "", "X", "O", "", "", "", "", ""])
    :param user_symbol: The symbol of the user (e.g., "X")
    :param opponent_symbol: The symbol of the opponent (e.g., "O")
    :return: Index of the best move
    """
    if user_symbol == "X":
        opponent_symbol = "O"
    else:
        opponent_symbol = "X"

    best_score = -float('inf')
    best_move = None

    for i in range(len(board_state)):
        if board_state[i] == "":  # Check available spots
            board_state[i] = user_symbol  # Make the move
            score = minimax(board_state, 0, False, user_symbol, opponent_symbol)
            board_state[i] = ""  # Undo the move
            if score > best_score:
                best_score = score
                best_move = i
    print(f"Chosen square : {best_move}")
    return best_move
