import time

def merge_sort(data, drawData, tick):
    return merge_sort_alg(data,0, len(data)-1, drawData, tick)


def merge_sort_alg(data, left, right, drawData, tick):
    if left < right:
        middle= (left + right) //2
        merge_sort_alg(data, left, middle, drawData, tick)
        merge_sort_alg(data, middle+1, right, drawData, tick)
        merge(data, left, middle, right, drawData, tick)



def merge(data, left, middle, right, drawData, tick):
    drawData(data, getColorArr(len(data), left, middle, right))
    time.sleep(tick)

    leftSide=data[0 : middle+1]
    rightSide=data[middle + 1: right + 1]
    leftIndex= rightIndex=0

    for dataIndex in range(left, right +1):
        if (leftIndex < len(leftSide) and rightIndex < len(rightSide)):
            if leftSide[leftIndex] <= rightSide[rightIndex]:
                data[dataIndex]=leftSide[leftIndex]
                leftIndex +=1
            else: 
                data[dataIndex]=rightSide[rightIndex]
                rightIndex+=1
        elif leftIndex < len(leftSide):
            data[dataIndex]=leftSide[leftIndex]
            leftIndex +=1
        else:
            data[dataIndex]= rightSide[rightIndex]
            rightIndex +=1
  
    drawData(data, ['green' if x>=left and x<=right else 'white' for x in range(len(data))])
    time.sleep(tick)

def getColorArr(length, left, middle, right):
    colorArr=[]
     
    for i in range(length):
        if i >= left and i<=right:
            if i >=left and i<=middle:
                colorArr.append('Yellow')
            else:
                colorArr.append('Pink')
        else:
            colorArr.append('White')
    
    return colorArr         


