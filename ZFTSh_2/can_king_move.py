def can_king_move(x1, y1, x2, y2):
    if x1 == x2 and  (y2 == y1 +1 or y2 == y1 - 1):
        return True
    if (x2 == x1-1 or x2 == x1+1) and (y2 == y1 or y2 == y1+1 or y2 == y1 - 1):
        return True
    if  y1 == y2 and (x2 == x1 + 1 or x2 == x1 - 1):
        return True

    return False
print(can_king_move(1,1,2,3))