
def swap(i, j, lst):
    return lst[:min(i, j)] + lst[max(i, j)] + lst[min(i, j) + 1:max(i, j)] + lst[min(i, j)] + lst[max(i, j):]

def permutations(lst, permut=[]):

    if len(lst) <= 1:
        return lst

    for i in range(len(lst)):
        permuted = swap(0, i, lst)

    return lst[0] + permuted + permutations(lst[1:]))