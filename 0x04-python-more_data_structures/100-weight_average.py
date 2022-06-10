def weight_average(my_list=[]):
    score = 0
    weight = 0
    if not my_list:
        return 0

    for j in my_list:
        score += j[0] * j[1]
        weight += j[1]
