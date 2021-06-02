"""
Created on 6/2/21

@author: fayfayning
"""

def center_tree(n):
    tree = range(n)
    if len(tree) % 2 == 1:
        count = int((len(tree) - 1) / 2)
        new_tree = [i for i in range(count, 0, -1)]
        new_tree.extend(range(count + 1))
    else:
        count = int(len(tree) / 2)
        new_tree = [i for i in range(count, 0, -1)]
        new_tree.extend(range(count))
    return new_tree


def find_pq(tree):
    for i in range(len(tree) - 1, -1, -1):
        if tree[i] != 1:
            p = i
            lp = tree[i]
            break
    for i in range(p - 1, -1, -1):
        if tree[i] == lp - 1:
            return [p + 1, i + 1]

def get_si(i, tree, vals):
    if i < vals[0]:
        return tree[i-1]
    else:
        return get_si(i - (vals[0] - vals[1]), tree, vals)

def comp_lex(tree1, tree2):
    tree1 = [str(i) for i in tree1]
    tree2 = [str(i) for i in tree2]
    string1 = "".join(tree1)
    string2 = "".join(tree2)
    if (string1 == string2):
        return 0
    if min(string1, string2) == string1:
        return -1
    else:
        return 1

    """
    for i in range(len(tree1)):
        if i >= tree1
        diff = tree1[i] - tree2[i]
        if diff[i] == 0:
            continue
        else:
            return diff[i]
    """

def free_check(tree, n):
    if tree.count(1) == 1:
        return False
    ind_1 = tree.index(1)
    m = tree.index(1, ind_1 + 1)
    L1 = [tree[i] - 1 for i in range(1, m)]
    L2 = [tree[i] for i in range(m, n)]
    L2.insert(0, tree[0])
    if max(L2) < max(L1):
        return False
    if max(L2) == max(L1):
        if len(L1) > len(L2):
            return False
    if len(L1) == len(L2):
        if comp_lex(L1, L2) > 0:
            return False
    return True

def l_height(tree):
    ind_1 = tree.index(1)
    m = tree.index(1, ind_1 + 1)
    left = tree[0:m]
    return max(left) -1

    """
    val = tree[0]        
        for i in range(1, len(tree)):
        if tree[i] <= val:
            return i - 1
        else:
            val = tree[i]
    """

def skip(tree, vals):
    if tree.count(1) == 1:
        return tree
    ind_1 = tree.index(1)
    m = tree.index(1, ind_1 + 1)
    L1 = [tree[i] - 1 for i in range(1, m)]
    vals = find_pq(L1)
    tree2 = [get_si(i+1, tree, vals) for i in range(n)]
    if tree[vals[0]] > 2:
        h = max(L1)
        tree2 = tree2[:len(tree2) - (h + 1)]
        tree2.extend(range(1, h + 2))
    return tree2

if __name__ == '__main__':

    n = 5
    free = []
    tree = center_tree(n) #don't add initial tree because there is no second 1
    j = 0
    while sum(tree) != len(tree) - 1 and j <= 5:
        print(tree, free_check(tree, n))
        vals = find_pq(tree)
        tree = [get_si(i + 1, tree, vals) for i in range(n)]
        if free_check(tree, n):
            free.append(tree)
        else:
            tree = skip(tree, vals)
    print(tree, free_check(tree, n))

    print("fin", len(free))

"""
print(*tree, sep = " ")
"""