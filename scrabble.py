import sys
import math

board = ["5", "because", "first", "these","could", "which", "hicquwh"]

letter = ["hicquwh"]

score = { 
        "1" : "e, a, i, o, n, r, t, l, s, u", 
        "2" : "d, g", 
        "3" : "b, c, m, p", 
        "4" : "f, h, v, w, y", 
        "5" : "k", 
        "8" : "j, x", 
        "10" : "q, z"}


board.remove("hicquwh")
print(board)

for i in range(len(board)):
    result = []
    if score != board:
        result = board.pop()
    print(result)
