import tkinter as tk
import random
import time

def swap(bar1, bar2):
   b1 = C.coords(bar1)
   b2 = C.coords(bar2)

   b1M = b2[0]-b1[0]       #.coords() gave us coordinates in a list which we can manipulate to make the movements
   b2M = b1[2]-b2[2]

   go = True

   #animation of the actual swap
   while go ==True:
       C.move(bar1,b1M,0)
       C.move(bar2,b2M,0)
       root.update()
       time.sleep(.01)
       go=False

def swapVals(ind1,ind2):
    global values
    global barList
    # values swap
    temp = values[ind1]
    values[ind1] = values[ind2]
    values[ind2] = temp

    temp2 = barList[ind1]
    barList[ind1] = barList[ind2]
    barList[ind2] = temp2


def part(low,high ):
    global values
    global barList
    pivot = values[high]
    pivotBar = barList[high]
    C.itemconfig(barList[high], fill='green')

    i = low -1

    for k in range(low,high):
        if values[k]>=pivot:
            i=i+1
            swapVals(i,k)
            swap(barList[i],barList[k])  #CHANGED
    swapVals(i+1,high)
    swap(barList[high],barList[i+1])
    return i+1


def quickSort(low, high):
    global values
    global barList
    if low<high:
        pi = part(low, high)
        quickSort(low, pi-1)
        quickSort(pi+1, high)

def selection():
    global barList
    global values

    for i in range(len(values)):
        minVal = i
        for j in range(i + 1, len(values)):
            if (values[j] > values[minVal]):
                minVal = j
        swapVals(minVal,i)
        swap(barList[minVal], barList[i])

def bubble():
    global values
    global barList

    for i in range(len(values)-1):
        for k in range(len(values)-i-1):
            if(values[k] < values[k+1]):
                swapVals(k,k+1)
                swap(barList[k],barList[k+1])

def insertion():
    global values
    global barList

    for i in range(len(values)):
        pivot = values[i]
        pivotBar = barList[i]
        C.itemconfig(pivotBar, fill='yellow')
        pos = i

        while pos > 0 and values[pos-1]<pivot:
            values[pos] = values[pos-1]
            barList[pos], barList[pos - 1] = barList[pos - 1], barList[pos]
            swap(barList[pos], barList[pos - 1])
            pos-=1
        values[pos] = pivot
        barList[pos] = pivotBar
        swap(barList[pos], pivotBar)

def generate():
    global barList
    global values
    global smInd
    C.delete('all')
    barstart = 7  #coordinates
    barend = 15
    barList = []
    values =[]

    for bar in range(0, 60):
        randomY = random.randint(1, 250)
        values.append(randomY)
        bar = C.create_rectangle(barstart, randomY, barend, 350, fill='blue')
        barList.append(bar)  #list of numberrs we need to sort
        barstart += 10
        barend += 10

    smallest = max(values)
    smInd = values.index(smallest) #setting min value bar to be red
    C.itemconfig(barList[smInd],fill='red')
root = tk.Tk()
root.title('Sorting Algorithims Visualizer')
root.geometry('700x500')

C = tk.Canvas(root, width = '650', height='450')    #canvas to display the contents
C.grid(column=0,row=0, columnspan=60)


#buttons:
shuffle = tk.Button(root, text='Shuffle', command=generate,width=10,height=1)
shuffle.grid(column=2,row=1)

selection = tk.Button(root, text='Selection Sort', command=selection,width=10,height=1)
selection.grid(column=3,row=1)

bubble = tk.Button(root, text='Bubble Sort', command=bubble,width=10,height=1)
bubble.grid(column=4,row=1)

insertion = tk.Button(root, text='Insertion Sort', command=insertion,width=10,height=1)
insertion.grid(column=5,row=1)

quick = tk.Button(root, text='QuickSort', command=lambda: quickSort(0,59),width=10,height=1)
quick.grid(column=6,row=1)


generate()


root.mainloop()
