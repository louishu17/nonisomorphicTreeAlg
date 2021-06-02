"""
Created on 6/2/21

@author: fayfayning
"""

def center_tree(n):
    tree = range(n)
    if len(tree) % 2 == 1:
        count = int((len(tree) - 1) / 2)
        new_tree = [i for i in range(0, count + 1)]
        new_tree.extend(range(1, count + 1))
    else:
        count = int(len(tree) / 2)
        new_tree = [i for i in range(0, count + 1)]
        new_tree.extend(range(1, count))
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
    print(i)
    if i < vals[0]:
        return tree[i-1]
    else:
        #make not recursion so it's more efficient
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

def skip(tree, vals):
    if tree.count(1) == 1:
        return tree
    ind_1 = tree.index(1)
    m = tree.index(1, ind_1 + 1)
    L1 = [tree[i] - 1 for i in range(1, m)]
    vals = find_pq(L1)
    print(vals)
    tree2 = [get_si(i + 1, tree, vals) for i in range(n)]
    if tree[vals[0]] > 2:
        ind_1_2 = tree2.index(1)
        m_2 = tree2.index(1, ind_1_2 + 1)
        L1_2 = [tree2[i] -1 for i in range(1, m_2)]
        h = max(L1_2)
        tree2 = tree2[:len(tree2) - (h + 1)]
        tree2.extend(range(1, h + 2))
    return tree2

def run_free(n):
    free = []
    tree = center_tree(n)  # don't add initial tree because there is no second 1
    if free_check(tree, n):
        free.append(tree)
    while sum(tree) != len(tree) - 1:
        #print(tree, free_check(tree, n))
        vals = find_pq(tree)
        tree = [get_si(i + 1, tree, vals) for i in range(n)]
        if free_check(tree, n):
            free.append(tree)
        else:
            tree = skip(tree, vals)
            if free_check(tree, n):
                free.append(tree)
    #print(tree, free_check(tree, n))
    #print(len(free))
    return len(free)

if __name__ == '__main__':

    n = 14
    #run_free(n)

    lst = []
    for i in range(3, n + 1):
        lst.append(run_free(i))
    print(lst)

"""
print(*tree, sep = " ")

def l_height(tree):
    ind_1 = tree.index(1)
    m = tree.index(1, ind_1 + 1)
    left = tree[1:m]
    return max(left)

    val = tree[0]        
        for i in range(1, len(tree)):
        if tree[i] <= val:
            return i - 1
        else:
            val = tree[i]
"""