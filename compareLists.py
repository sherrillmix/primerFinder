#could do something smarter here if slow
def mergeSortedArrays(x,y):
    merged=x+y
    merged.sort()
    return merged

def mergeMultipleArrays(x):
    out=[]
    #use mergeSortedArrays here if it is optimized
    for thisArray in x:
        out=out+thisArray
    out.sort()
    return(out)


    
def findDistanceToClosest(x,y):
    yPos=0
    #x.sort() #assume sorted
    #y.sort() #assume sorted
    nY=len(y)
    out=[float('inf')]*len(x)
    for xPos in range(len(x)):
        while y[yPos]<=x[xPos] and yPos+1<nY:
            yPos+=1
        if y[yPos]>x[xPos]:
            out[xPos]=y[yPos]-x[xPos]-1 #first base minus last base
    return out
        
