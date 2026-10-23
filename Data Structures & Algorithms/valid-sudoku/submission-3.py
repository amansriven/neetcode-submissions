class Solution:
    # square 0, 3, 6 start at col 0
    # square 1, 4, 7 start at col 3
    # square 2, 5, 8 start at col 6
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for rows
        for i in range(9):
            seen = set()
            for x in board[i]:
                if x != '.':
                    if x in seen:
                        return False
                    seen.add(x)
        
        # for cols
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])

        # for squares
        for i in range(9):
            seen = set()
            row = (i // 3) * 3
            col = (i % 3) * 3
            for r in range(3):
                for c in range(3):
                    x = board[row + r][col + c]
                    if x != '.':
                        if x in seen:
                            return False
                        seen.add(x)
        
        return True

