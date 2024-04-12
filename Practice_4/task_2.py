def is_subset(set1, set2):
    if set1 == set2: return False
    return set1.issubset(set2)


set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0}

print(is_subset(set1, set2))