# Write your code here :-)
chess_board = {"a1": "bking", "a2": "wking", "a3": "wpawn", "a4": "bpawn"}


def isValidChessBoard(board):
    # create valid list of spaces and pieces and max players
    max_white = 16
    max_black = 16
    valid_pieces = [
        "bking",
        "wking",
        "wpawn",
        "bpawn",
        "bbishop",
        "wbishop",
        "brook",
        "wrook",
        "bknight",
        "wknight",
    ]
    valid_spaces = []
    list_a = range(1, 9)
    list_b = ["a", "b", "c", "d", "e", "f", "g", "h"]
    for letter in list_b:
        for num in list_a:
            space = letter + str(num)
            valid_spaces.append(space)
    # count all pieces in dictionary and for each player
    b_pieces_count = 0
    w_pieces_count = 0
    count = {}
    for key in board:
        if board[key] not in count:
            count[key] = 1
        else:
            count[key] += 1
        if board[key].startswith("b") == True:
            b_pieces_count += 1
        elif board[key].startswith("w") == True:
            w_pieces_count += 1
        else:
            return False

    if b_pieces_count or w_pieces_count > 16:
        print("Too many pieces")
        return False
    if count["bking"] != 1 or count["wking"] != 1:
        print("King error")
        return False
    if count["bpawn"] > 8 or count["wpawn"] > 8:
        print("pawn error")
        return False
    if count["wbishop"] > 1 or count["bbishop"] > 1:
        print("bishop error")
        return False
    if count["wrook"] > 1 or count["brook"] > 1:
        print("rook error")
        return False
    if count["wknight"] > 1 or count["bknight"] > 1:
        print("knight error")
        return False
    for key in board(keys):
        if key not in valid_spaces:
            return False


isValidChessBoard(chess_board)
