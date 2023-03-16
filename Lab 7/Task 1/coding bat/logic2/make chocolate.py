def make_chocolate(small, big, goal):
    big_bars_needed = goal // 5
    
    if big_bars_needed <= big:
        small_bars_needed = goal - big_bars_needed * 5
        if small_bars_needed <= small:
            return small_bars_needed
    elif goal - big * 5 <= small:
        return goal - big * 5

    return -1