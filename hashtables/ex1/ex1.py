def get_indices_of_item_weights(weights, length, limit):
    weight = {}
    check_for_dups = False
    dups = {}

    for i in range(0, length):
        current = weights[i]
        weight[current] = i
        target = limit - current
        if target in weight:
            if current > target:
                return (i, weight[target])
            elif current < target:
                return (i, weight[target])
            elif target == current:
                if check_for_dups is False:
                    check_for_dups = True
                    dups[current] = i
                elif check_for_dups is True:
                    return (i, dups[current])
    # Your code here

    return None