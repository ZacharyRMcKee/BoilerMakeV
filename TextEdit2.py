import tkinter as tk

class Application(tk.Frame):
    
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
    
    def createWidgets(self):
        panes = tk.PanedWindow(self,width=1000,height=800)
        text = tk.Text(panes,width=100)
        webPane = tk.Message(panes,width=300,bg="#00FFFF",text="Fuck you! >:C")
        panes.add(text)
        panes.add(webPane)
        panes.grid(column=0,row=0)
    
    def debug(self):
        print("Hi!")


app = Application()
app.master.title('Sample application')
app.master.minsize(width=1000,height=800)
app.master.maxsize(width=1000,height=800)
app.mainloop()
