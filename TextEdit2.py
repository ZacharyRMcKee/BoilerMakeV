import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import tkFontChooser

class Application(tk.Frame):
    filename = None
    root = None
    menubar = None
    text = None
    def __init__(self, master=None):
        global root
        root = tk.Frame.__init__(self,master)
        self.grid()
        self.createWidgets()
        self.filename = "Untitled.txt"
    def newFile(self): 
        self.filename = "Untitled.txt" 
        self.text.delete(0.0, tk.END) 
    
    def saveFile(self): 
        t = self.text.get(0.0, tk.END) 
        f = open(self.filename, 'w') 
        f.write(t) 
        f.close() 

    def saveAs(self): 
        f = asksaveasfile(defaultextension='.txt') 
        t = self.text.get(0.0, tk.END) 
        try: 
            f.write(t.rstrip()) 
        except: 
            showerror(title="Oh No!", message="Unable to save file...") 
      

    def openFile(self): 
        file = askopenfile(parent=root,title='Select a File') 
        self.filename = file.name 
        t = file.read() 
        self.text.delete(0.0, tk.END) 
        self.text.insert(0.0, t) 
        file.close() 

    def createWidgets(self):

        panes = tk.PanedWindow(self,width=1000,height=800)
        textFrame = tk.Frame(panes,width=700)
        webPane = tk.Message(panes,width=300,bg="#00FFFF",text="Fuck you! >:C")
        

        panes.add(textFrame)
        panes.add(webPane)
        panes.grid(column=0,row=1)
        scrollbar = tk.Scrollbar(textFrame)
        self.text = tk.Text(textFrame,width=100, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)
        self.text.pack(side=tk.RIGHT,fill=tk.BOTH,expand=1)

        scrollbar.config(command=self.text.yview)



        self.menubar = tk.Menu(self)
        filemenu = tk.Menu(self.menubar)

        filemenu.add_command(label="New", command=self.newFile) 
        filemenu.add_command(label="Open", command=self.openFile) 
        filemenu.add_command(label="Save", command=self.saveFile) 
        filemenu.add_command(label="Save As", command=self.saveAs) 
        # some more code...
        fontbar = tk.Menu(self.menubar)
        #fontbar.add_command(label="Font Size", command=self.fontSize)
        #fontbar.add_command(label="Font Type", command=self.fontType)
        #fontbar.add_command(label="Font Color", command=self.fontColor)
            
        filemenu.add_separator() 
        filemenu.add_command(label="Quit", command=self.quit) 
        self.menubar.add_cascade(label="File", menu=filemenu)
        #menubar.add_cascade(label="Change Font", menu=fontbar)
        #app.config(menu=menubar)

        
        editmenu = tk.Menu(self.menubar)
        editmenu.add_command(label="Undo", command=self.openFile)
        editmenu.add_separator()
        editmenu.add_command(label="Cut", command=self.openFile)
        editmenu.add_command(label="Copy", command=self.saveFile)
        editmenu.add_command(label="Paste", command=self.saveAs)
        editmenu.add_command(label="Delete", command=self.quit)
        editmenu.add_separator()
        editmenu.add_command(label="Copy", command=self.saveFile)
        editmenu.add_command(label="Copy", command=self.saveFile)
        editmenu.add_command(label="Paste", command=self.saveAs)
        editmenu.add_separator()
        editmenu.add_command(label="Select All", command=self.openFile)
        editmenu.add_command(label="Time & Date", command = self.openFile)
        self.menubar.add_cascade(label="Edit", menu=editmenu)

        
app = Application()
app.master.title('Sample application')
app.master.minsize(width=1000,height=800)
app.master.maxsize(width=1000,height=800)

app.master.config(menu=app.menubar)
app.mainloop()
