import tkinter as tk
import os
import datetime 
import sys
from termcolor import colored
import poemFinder as pf

# numOfPoems = 0
# poemOrder = ''
class poetryGenerator:
    def __init__(self, root):
        # Initialising all input objects, properties and labels
        self.root = root
        self.root.geometry("1000x1000")
        self.root.title("Syllabary Poetry Generator")

        self.startingPoem = tk.StringVar()
        self.numOfPoems = tk.IntVar()
        self.poemOrder = tk.StringVar()
        self.poemOrder.set(' ') 
        self.poemNumLabel = tk.Label(self.root, text="How many poems do you want to generate?")
        self.poemNumEntry = tk.Entry(self.root, textvariable=self.numOfPoems, font=('calibre', 10, 'normal'))
        self.startingPoemLabel = tk.Label(self.root, text="What poem do you want to start with?")
        self.startingPoemEntry = tk.Entry(self.root, textvariable=self.startingPoem, font=('calibre', 10, 'normal'))
        self.poemOrderLabel = tk.Label(self.root, text="Would you like to output the poems forwards or in reverse order?")
        self.radioButton1 = tk.Radiobutton(self.root, text="forwards", variable=self.poemOrder, value="forwards")
        self.radioButton2 = tk.Radiobutton(self.root, text="backwards", variable=self.poemOrder, value="backwards")
        self.button = tk.Button(self.root, text="Submit", command=self.submit)
            
    def packFrame(self):
        # Packing all objects so they can be viewed
        self.poemNumLabel.pack()
        self.poemNumEntry.pack()
        self.startingPoemLabel.pack()
        self.startingPoemEntry.pack()
        self.poemOrderLabel.pack()
        self.radioButton1.pack()
        self.radioButton2.pack()
        self.button.pack()
    
    def runPoemFinder(self):
        allPoemsList = pf.createFileList()
        max_values = pf.findMaxValues(allPoemsList)
        selectedPoemsList = pf.createOutputFileList(allPoemsList, self.startingPoem.get(), self.numOfPoems.get(), max_values)
        selectedPoemsList = pf.reverseList(self.poemOrder, selectedPoemsList)
        selectedPoemsDict = pf.readingXML(selectedPoemsList)
        pf.creatingTextDocumentOutput(selectedPoemsDict, selectedPoemsList)
        print("poem order is: " + str(self.poemOrder.get()))

    def submit(self):
        self.runPoemFinder()
        self.root.destroy()
        
def sysStatus(message, useTS=True, color='white'):
    #Cheap way of displaying timed status messages to terminal
    rawtime = datetime.datetime.now()
    timeStamp = rawtime.strftime('%Y-%m-%d %H:%M:%S')

    if useTS:
        #print(timeDisplay + colored(f'  {message}', 'green'))
        print(f'{timeStamp}:     {message}')
    else:
        print(colored(f'{message}', color))

def preRunCleanUp():
    #Clears out the terminal so you can easily view when the latest run was initiated
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')

    sysStatus('Run Started...\n')
    
def main():
    root = tk.Tk()

    syllabaryGenerator = poetryGenerator(root)
    syllabaryGenerator.packFrame()

    root.mainloop()
    
if __name__ == "__main__":
    preRunCleanUp()
    main()
    

