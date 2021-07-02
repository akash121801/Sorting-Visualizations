  
import time

def insertion_sort(data, drawData, tick):
	for i in range(1, len(data)):
		j = i
		while(j > 0 and data[j] < data[j-1]):
			drawData(data, ['red' if x == j or x == j + 1 else 'gray' for x in range(len(data))])
			time.sleep(tick)
			data[j], data[j-1] = data[j-1], data[j]
			j -=1

		drawData(data, ['white' if x < i else 'gray' for x in range(len(data))])
		time.sleep(tick)
