def sum13(nums):
    if not nums:
        return 0

    total = 0
    prev_13 = False

    for num in nums:
        if num == 13:
            prev_13 = True
        elif prev_13:
            prev_13 = False
        else:
            total += num

    return total