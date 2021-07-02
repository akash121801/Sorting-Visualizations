import time

def Partition(data, left, right, drawData, tick):
    i = (left-1)         # index of smaller element
    pivot = data[right] # pivot

    drawData(data, getColorArray(len(data), left, right, i, i))
  
    for j in range(left, right):
        if data[j] <= pivot:
            drawData(data, getColorArray(len(data), left, right, i, j, True))
            time.sleep(tick)
            i = i+1
            data[i], data[j] = data[j], data[i]
        
        drawData(data, getColorArray(len(data), left, right, i, j))
        time.sleep(tick)

    drawData(data, getColorArray(len(data), left, right, i,right, True))
    time.sleep(tick) 
    data[i+1], data[right] = data[right], data[right]   
    return (i+1)


def quick_sort(data, left, right, drawData, tick):
	if(left < right):
		partition = Partition(data, left, right, drawData, tick)
		##left partition
		quick_sort(data, left, partition, drawData, tick)

		##right partition
		quick_sort(data, partition + 1, right, drawData, tick)


def getColorArray(dataLen, head, tail, border, curr, isSwapping = False):
	colorArray = []
	for i in range(dataLen):
		#base coloring
		if i>= head and i <= tail:
			colorArray.append('gray')
		else:
			colorArray.append('white')

		if(i == tail):
			colorArray[i] = 'blue'
		elif(i == border):
			colorArray[i] = 'red'
		elif(i == curr):
			colorArray[i] = 'yellow'

		if (isSwapping):
			if(i == border or i == curr):
				colorArray[i] = 'green'

	return colorArray
   