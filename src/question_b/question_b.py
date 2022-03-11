def get_sum_of_events(num):
    i = num
    sum = 0
    while i > 0:
        if ((i % 2) == 0):
            sum += i
        i -= 1
    return sum