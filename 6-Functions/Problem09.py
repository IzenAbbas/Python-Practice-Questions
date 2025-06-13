def nearest_coordinate(c,qp):
    min_dist=((c[0][0]-qp[0])**2 + (c[0][1]-qp[1])**2)**0.5
    point=list(c[0])

    for i in range(1,len(c)):
        temp_dist=((c[i][0]-qp[0])**2 + (c[i][1]-qp[1])**2)**0.5
        if  temp_dist<min_dist:
            min_dist=temp_dist
            point=list(c[i])

    return tuple(point)

            


coordinates=[(2,2),(3,3),(4,4),(1,1),(0,0)]
query_point=(0,0)

print(nearest_coordinate(coordinates,query_point))