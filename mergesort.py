def tolist(x):
    return [int(i) for i in str(x)]
def mergesort(x):
    if len(x)==1:
        return x
    left=x[0:round(len(x)/2)]
    right=x[round(len(x)/2):]

    return merge(mergesort(left),mergesort(right))

def merge(left,right):
    c=[]
    while len(left)>0 and len(right)>0:
        if left[0]>right[0]:
            c.append(right[0])
            del right[0]
        else:
            c.append(left[0])
            del left[0]
    while len(left)>0:
        c.append(left[0])
        del left[0]
    while len(right)>0:
        c.append(right[0])
        del right[0]
    return c
    

print (mergesort(tolist(42214)))


