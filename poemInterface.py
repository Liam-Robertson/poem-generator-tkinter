import tkinter as tk
import poetryGenerator as pg

root = tk.Tk()
root.geometry("500x200")
root.title("Poem Generator")

def getPoemNumber(poemNum):
    poemNumOutput = tk.Label(root, text="You have printed: " + str(poemNum.get()) + " poems!")
    poemNumOutput.grid(row=8, column=0, columnspan=2)

def refreshPage(startingPoemLabel, startingPoem, numOfPoemsLabel, numOfPoems, numOfPoemsButton, ReverseLabel):
    startingPoemLabel.grid_forget()
    startingPoem.grid_forget()
    numOfPoems.grid_forget()
    numOfPoemsLabel.grid_forget()
    numOfPoemsButton.grid_forget()
    ReverseLabel.grid_forget()
    
def main():
    myIntVar = tk.IntVar()
    myStrVar = tk.StringVar()
    myStrVar2 = tk.StringVar()

    startingPoemLabel = tk.Label(root, text="Enter the poem you want to start from")
    startingPoemLabel.grid(row=0, column=0, columnspan=2)

    startingPoem = tk.Entry(root, textvariable=myStrVar)
    startingPoem.grid(row=1, column=0)

    numOfPoemsLabel = tk.Label(root, text="Enter number of poems you wish to generate")
    numOfPoemsLabel.grid(row=2, column=0, columnspan=2)

    numOfPoems = tk.Entry(root)
    numOfPoems.grid(row=3, column=0)

    ReverseLabel = tk.Label(root, text="Do you want to reverse the output order of the poems?")
    ReverseLabel.grid(row=5, column=0, columnspan=2)

    reversed = tk.Radiobutton(root, text="Yes", variable=myStrVar2, value=1)
    reversed.grid(row=6, column=0)

    forwards = tk.Radiobutton(root, text="No", variable=myStrVar2, value=2)
    forwards.grid(row=6, column=1)

    filename_lst = pg.createFileList()
    max_values = pg.findMaxValues(filename_lst)

    startingPoemStr = startingPoem.get()

    button_quit = tk.Button(root, text="Submit") #, command= lambda: refreshPage(startingPoemLabel, startingPoem, numOfPoemsLabel, numOfPoems, numOfPoemsButton, ReverseLabel)
    button_quit.grid(row=7, column=0) 

    button_quit = tk.Button(root, text="Exit Program", command=root.quit)
    button_quit.grid(row=9, column=0) 

    root.mainloop()
    print("bing")
    print(startingPoemStr)
    outputFileList = pg.createOutputFileList(filename_lst, startingPoemStr, numOfPoems, max_values)
    print(outputFileList)

if __name__ == "__main__":
    main()
