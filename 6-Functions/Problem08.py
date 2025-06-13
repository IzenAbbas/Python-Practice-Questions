def histogram(L):
    l_bound = (min(L) // 10) * 10 + 1
    u_bound = ((max(L) // 10) + 1) * 10

    result = {}

    for i in range(l_bound, u_bound-10, 10):
        count = sum(1 for x in L if i <= x <= i + 9)
        result[f"{i}-{i+9}"] = count

    print(result)


L=[13,42,15,37,22,39,41,50]
histogram(L)