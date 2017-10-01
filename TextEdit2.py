import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import tkFontChooser
import urllib.request
import urllib.parse

import wikipedia

class WikiModule(tk.Frame):
    title = None
    root = None
    body = None
    url = None
    def __init__(self,master):
        root = tk.Frame.__init__(self,master,height=267,width=300,bg="#0000ff")
        header = tk.Label(self,width=43,bg="#00ff00",text="Robert Taylor Homes")

        body = tk.Message(self,width=300,bg="#ff0000",text=wikipedia.summary("Robert Taylor Homes",sentences=4))
        header.grid(column=0,row=0)
        body.grid(column=0,row=1)
    def updateModule(self,article):
        # do stuff
        return





class Application(tk.Frame):
    filename = None
    root = None
    menuIbar = None
    text = None
    wiki = None
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



    def rightClick(self,e):
        try:
            def rightClick_Copy(e, apnd=0):
                e.widget.event_generate('<Control-c>')
            def rightClick_Cut(e):
                e.widget.event_generate('<Control-x>')
            def rightClick_Paste(e):
                e.widget.event_generate('<Control-v>')
            def rightClick_Youtube(e):
                query_string = urllib.parse.urlencode({"search_query" : (e)})
                html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
                search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
                e= "http://www.youtube.com/watch?v=" + search_results[0]
                winston.withdraw()
                winston.clipboard_append(e)
                winston.update()
                
                
            e.widget.focus()
            
            nclst=[
                   (' Cut', lambda e=e: rightClick_Cut(e)),
                   (' Copy', lambda e=e: rightClick_Copy(e)),
                   (' Paste', lambda e=e: rightClick_Paste(e)),
                   (' Youtube', lambda e=e: rightClick_Youtube(e))
                   ]
            rmenu = tk.Menu(None, tearoff=0, takefocus=0)

            for (txt, cmd) in nclst:
                rmenu.add_command(label=txt, command=cmd)

            rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")
        except TclError:
            print (' - rClick menu, something wrong')
            pass

        return "break"

    def rClickbinder(r):
        try:
            for b in [ 'Text', 'Entry', 'Listbox', 'Label']: #
                r.bind_class(b, sequence='<Button-3>',
                             func=rClicker, add='')
        except TclError:
            print (' - rClickbinder, something wrong')
            pass
          
    def createWidgets(self):

        panes = tk.PanedWindow(self,width=1000,height=900)
        textFrame = tk.Frame(panes,width=600)
        
        #summary = wikipedia.summary("section 8 housing",sentences=5)
        webPane = tk.Frame(panes,bg="#333333")
        #webPane = tk.Message(panes,width=300,bg="#00FFFF",text=summary)
        wiki = WikiModule(webPane)
        wiki.grid()
        panes.add(textFrame)
        panes.add(webPane,minsize=300)
        panes.grid(column=0,row=0)
        scrollbar = tk.Scrollbar(textFrame)
        self.text = tk.Text(textFrame,width=100, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)
        self.text.pack(side=tk.RIGHT,fill=tk.BOTH,expand=1)

        wiki.grid_propagate(0)
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
app.master.title('NoteMaker')
app.master.minsize(width=1000,height=801)
app.master.maxsize(width=1000,height=801)



if __name__ == '__main__':
    app.master.bind('<Button-3>',app.rightClick)

app.master.config(menu=app.menubar)
app.mainloop()
