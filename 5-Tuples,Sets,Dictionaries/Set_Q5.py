lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

intersection=[i for i in lst1 if i in lst2] #finding common elements
seen=set()
intersection=[i for i in intersection if not(i in seen or seen.add(i))] #removing duplicates

print(intersection)