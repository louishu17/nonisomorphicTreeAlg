def create_si(tree, p, q):
    ret = []
    i = 1
    while i <= len(tree):
        if i < p:
            ret.append(tree[i - 1])
        else:
            ret.append(ret[i - (p - q) - 1])
        i += 1
    return ret


def check(tree, n):
    m = tree.index(1, 2)
    L1 = [tree[i] - 1 for i in range(1, m)]
    L2 = [tree[i] for i in range(m, n)]
    L2.insert(0,0)
    if max(L2) >= max(L1):
        if len(L2) >= max(L1):
            if ''.join([str(elem) for elem in L2]) >= \
                    ''.join([str(elem) for elem in L1]):
                return True
    return False


def height(tree):
    m = tree.index(1, 2)
    return max(tree[0:m]) - 1


def getp(tree):
    for x in reversed(range(0, len(tree))):
        if tree[x] != 1:
            p = x + 1
            break
    return p


def getq(tree, p):
    for x in reversed(range(0, len(tree))):
        if x < p:
            if tree[x] < tree[p - 1]:
                return x + 1


def algo2(tree, n):
    m = tree.index(1, 2)
    L1 = [tree[i] - 1 for i in range(1, m)]
    L2 = [tree[i] for i in range(m, n)]
    L2.insert(0, 0)
    p = getp(L1)
    q = getq(L1, p)
    print(p,q)
    newTree = create_si(tree,p,q)
    """check here to end of function with big brain logic"""
    if tree[p] > 2:
        h = max(L1)
        newTree = newTree[:len(newTree) - (h + 1)]
        newTree.extend(range(1, h + 2))
    return newTree


def createTrees(n, tree):
    free = []
    free.append(tree)
    while max(tree) != 1:
        p = getp(tree)
        q = getq(tree, p)
        tree = create_si(tree, p, q)
        if check(tree, n):
            free.append(tree)
        else:
            tree = algo2(tree, n)
            if check(tree, n):
                free.append(tree)
    return free


if __name__ == '__main__':
    print(createTrees(7, [0,1,2,3,1,2,3]))
    print(len(createTrees(7, [0,1,2,3,1,2,3])))

