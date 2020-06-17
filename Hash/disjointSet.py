def isDisjoint(set1, set2):
    seen = set()
    for i in set1:
        seen.add(i)
    for j in set2:
        if seen.__contains__(j):
            return False
        else:
            continue
    return True