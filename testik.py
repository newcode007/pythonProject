def transform_list(N):
    transform=[n for n in N if n>0]
    return transform


N=[1,5,6,-7,-9,10,-150]
k=transform_list(N)
print(k)