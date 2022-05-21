# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters that are horizontally or vertically adjacent.
# The same letter cell may not be used more than once.

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# "ABCCED" => True
# "SEE" => True
# "ABCB" => False

def word_search(board, word):
    m = len(board)
    n = len(board[0])
    seen = set()
    
    def traverse(r, c, next_letter_index):
        nonlocal m, n
            
        if next_letter_index == len(word):
            return True
        
        seen.add((r,c)) 
        next_letter = word[next_letter_index]
        
        for (next_row, next_col) in [(r, c-1), (r-1, c), (r, c+1), (r+1, c)]:
            if 0 <= next_row < m and 0 <= next_col < n:
                if (next_row, next_col) not in seen:
                    if board[next_row][next_col] == next_letter:
                        if traverse(next_row, next_col, next_letter_index + 1):
                            return True
        
        seen.remove((r,c))
        return False
    
    first_letter = word[0]
    for r in range(m):
        for c in range(n):
            if board[r][c] == first_letter:
                if traverse(r, c, 1):
                    return True
                
    return False

if __name__ == "__main__":
    board = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    word = "ABCCED"
    print(word_search(board, word))
