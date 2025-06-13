import functools

list_2D=[[1,2,3],
         [4,5,6],
         [7,8,9]]

list_1D=(functools.reduce(lambda x,y:x+y,list_2D))
print(list_1D)