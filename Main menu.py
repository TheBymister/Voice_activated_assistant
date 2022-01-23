from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)
        self.startButton = Button(self, text="Start", command=self.clickStartButton)
        self.exitButton = Button(self, text="quit", command=self.clickExitButton)

        # create button, link it to clickExitButton()
        # place button at (0,0)
        #self.exitButton.place(x=0, y=0)
        #self.startButton.place(x=0, y=0)
        self.startButton.pack(anchor=CENTER)

    def clickStartButton(self):
        print("Starting")
        self.exitButton.pack(anchor=CENTER)
        self.startButton.pack_forget()

    def clickExitButton(self):
        print("Quitting")
        self.startButton.pack(anchor=CENTER)
        self.exitButton.pack_forget()
        
root = Tk()
root.resizable(False, False) #Disables resizable window
#root.overrideredirect(True) #Removes window closes button
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()
