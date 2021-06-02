import copy
def create_tree_set(L):
    pos = L.index(1,2)
    lone = L[1:pos]
    ltwo = L[pos:]
    ltwo.insert(0,0)
    for x in range(len(lone)):
        lone[x] = lone[x] - 1
        print(lone)
    return [lone, ltwo]
    """
    if max(lone) > max(ltwo):
            p = len(lone) - 1
            q = lone.index(lone[p] - 1)
    elif len(lone) > len(ltwo):
            p = len(lone) - 1
            q = lone.index(lone[p] - 1)
    else:

        return output_one
    """
if __name__ == '__main__':
    print(create_tree_set([0,1,2,3,3,1,2,1,1,1]))
    print("testing")