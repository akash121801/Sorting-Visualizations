from tkinter import *
from tkinter import ttk
import random
from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort

window= Tk()
window.title('Sorting Algorithms Visualized')
window.maxsize(900, 600)
window.config(bg='black')

#Variables
selected_alg= StringVar()
data=[]

#frame and base layout

def drawData(data, colorArr):
    canvas.delete('all')
    c_width=600
    c_height=380
    x_width=c_width / (len(data) + 1)
    offset=30
    spacing=10
    normalizedData= [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):

        x0 =i * x_width + offset + spacing
        y0=c_height-height * 340

        x1= (i+1) * x_width + offset
        y1=c_height
        


        canvas.create_rectangle(x0, y0, x1, y1, fill= colorArr[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text= str(data[i]))
    
    window.update_idletasks()



def Generate():
    global data
    print('Alg Selected: ' + selected_alg.get())
    minVal=int(minEntry.get())
    
    maxVal=int(maxEntry.get())
    
    size=int(sizeEntry.get())
    
    data=[]

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    
    drawData(data, ['blue' for x in range(len(data))])

def StartAlgorithm(): 
    global data
    print("Starting Algorithm...")

    if(algmenu.get() == 'Quick Sort'):
        quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
        drawData(data, ['green' for x in range(len(data))])
    
    elif(algmenu.get()=='Bubble Sort'):
        bubble_sort(data, drawData, speedScale.get())
    elif(algmenu.get()=='Selection Sort'):
        selection_sort(data, drawData, speedScale.get())
    elif(algmenu.get() == 'Insertion Sort'):
        insertion_sort(data, drawData, speedScale.get())
    elif(algmenu.get() == 'Merge Sort'):
        merge_sort(data, drawData, speedScale.get())

    drawData(data, ['green' for x in range(len(data))])
   


UI_frame=Frame(window, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5)

canvas= Canvas(window, width=600, height=380)
canvas.grid(row=1, column=0, padx=10, pady=5)



#UI Section
Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algmenu= ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Selection Sort', 'Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort'])
algmenu.grid(row=0, column=1, padx=5, pady=5) 
algmenu.current(0)

speedScale= Scale(UI_frame, from_=.1, to=2.0, length=200, digits=2, resolution=.2, orient=HORIZONTAL, label="Select Speed[s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='Blue').grid(row=0, column=3, padx=5, pady=5, sticky=W)


sizeEntry= Scale(UI_frame, from_=3, to=25, length=200, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5, sticky=W)


minEntry= Scale(UI_frame, from_=0, to=10, length=200, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)


maxEntry= Scale(UI_frame, from_=10, to=100, length=200, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5, sticky=W)





Button(UI_frame, text="Generate", command=Generate, bg='White').grid(row=1, column=3, padx=5, pady=5, sticky=W)


window.mainloop()