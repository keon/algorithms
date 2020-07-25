import copy

boardsize = 6
_kmoves = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))


def chess2index(chess, boardsize=boardsize):
    "Convert Algebraic chess notation to internal index format"
    chess = chess.strip().lower()
    x = ord(chess[0]) - ord("a")
    y = boardsize - int(chess[1:])
    return (x, y)


def boardstring(board, boardsize=boardsize):
    r = range(boardsize)
    lines = ""
    for y in r:
        lines += "\n" + ",".join(
            "%2i" % board[(x, y)] if board[(x, y)] else "  " for x in r
        )
    return lines


def knightmoves(board, P, boardsize=boardsize):
    Px, Py = P
    kmoves = set((Px + x, Py + y) for x, y in _kmoves)
    kmoves = set(
        (x, y)
        for x, y in kmoves
        if 0 <= x < boardsize and 0 <= y < boardsize and not board[(x, y)]
    )
    return kmoves


def accessibility(board, P, boardsize=boardsize):
    access = []
    brd = copy.deepcopy(board)
    for pos in knightmoves(board, P, boardsize=boardsize):
        brd[pos] = -1
        access.append((len(knightmoves(brd, pos, boardsize=boardsize)), pos))
        brd[pos] = 0
    return access


def knights_tour(start, boardsize=boardsize, _debug=False):
    board = {(x, y): 0 for x in range(boardsize) for y in range(boardsize)}
    move = 1
    P = chess2index(start, boardsize)
    board[P] = move
    move += 1
    if _debug:
        print(boardstring(board, boardsize=boardsize))
    while move <= len(board):
        P = min(accessibility(board, P, boardsize))[1]
        board[P] = move
        move += 1
        if _debug:
            print(boardstring(board, boardsize=boardsize))
            input("\n%2i next: " % move)
    return board


if __name__ == "__main__":
    while 1:
        boardsize = int(input("\nboardsize: "))
        if boardsize < 5:
            continue
        start = input("Start position: ")
        board = knights_tour(start, boardsize)
        print(boardstring(board, boardsize=boardsize))
