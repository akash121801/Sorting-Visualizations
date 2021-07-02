import time

def selection_sort(data, drawData, tick):
	for i in range(len(data) - 1):
		minIndex = i
		for j in range(i + 1, len(data)):
			if(data[j] < data[minIndex]):
				drawData(data, ['blue' if x == minIndex else 'gray' for x in range(len(data))])
				time.sleep(tick)
				minIndex = j
				
		drawData(data, ['green' if x == i or x == minIndex else 'gray' for x in range(len(data))])
		time.sleep(tick)
		data[i], data[minIndex] = data[minIndex], data[i]

