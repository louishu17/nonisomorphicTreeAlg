import copy


def create_tree_set(k):
    p = k - 1
    q = p
    output_one = []
    current_s = [*range(0, k)]
    output_one.append(copy.copy(current_s))
    while max(current_s) != 1:
        q -= 1
        current_s[p] = q
        add = copy.deepcopy(current_s)
        output_one.append(add)
        if q == 1:
            p -= 1
            q = p
    print(len(output_one))
    #for x in output:
    return output_one


if __name__ == '__main__':
    print(create_tree_set(6))
