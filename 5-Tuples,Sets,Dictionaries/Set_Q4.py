arr=[[1, 2, 2, 4, 3, 6],
    [5, 1, 3, 4],
    [9, 5, 7, 1],
    [2, 4, 1, 3]]
union=set()
for i in arr:
    union.update(i)
print('Union-',union)