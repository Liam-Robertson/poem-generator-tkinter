import tkinter as tk
import poetryGenerator as pg

root = tk.Tk()
root.geometry("500x200")
root.title("Poem Generator")

def getPoemNumber(poemNum):
    poemNum.get()
    poemNumOutput = tk.Label(root, text="You have printed: " + str(poemNum.get()) + " poems!")
    poemNumOutput.grid(row=3, column=0, columnspan=2)
    pg.tooBigMethod()
    


def main():
    fileList = pg.createFileList
    
    poemNumLabel = tk.Label(root, text="Enter number of poems you wish to generate")
    poemNumLabel.grid(row=0, column=0, columnspan=2)

    poemNum = tk.Entry(root)
    poemNum.grid(row=1, column=0)

    poemVar = poemNum.get()
    print(poemVar)

    poemNumButton = tk.Button(root, text="Insert Number of Poems", command=getPoemNumber)
    poemNumButton.grid(row=2, column=0)

    button_quit = tk.Button(root, text="Exit Program", command=root.quit)
    button_quit.grid(row=4, column=0) 

    root.mainloop()
    

if __name__ == "__main__":
    main()
