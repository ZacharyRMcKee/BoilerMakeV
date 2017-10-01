import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import tkFontChooser
import urllib.request
import urllib.parse
from titlecase import titlecase
import wikipedia

class WikiModule(tk.Frame):
    title = None
    root = None
    summary = None
    url = None
    popup = None
    def __init__(self,master):
        self.title = tk.StringVar()
        self.title.set("Wikipedia")
        self.summary = tk.StringVar()
        self.summary.set(wikipedia.summary("Wikipedia",sentences=4))
        
        root = tk.Frame.__init__(self,master,height=267,width=300,bg="#0000ff")
        header = tk.Label(self,width=43,bg="#00ff00",textvariable=self.title)

        body = tk.Message(self,width=300,bg="#ff0000",textvariable=self.summary)
        header.grid(column=0,row=0)
        body.grid(column=0,row=1)
    def updateModule(self,article):
        # do stuff
        print(article)
        self.title.set(titlecase(article))
        try:
            self.summary.set(wikipedia.summary(article,sentences=4))
        except wikipedia.exceptions.DisambiguationError as e:
            for i in e.options:
                print(i)
            print("Done")
            print(len(e.options))
            self.disambiguation(e.options)






        return
    def select(self,e):
        w = e.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        self.updateModule(value)
        self.popup.destroy()
    def disambiguation(self,options):
        self.popup =  tk.Tk()

        scrollBar = tk.Scrollbar(self.popup)
        scrollBar.pack(side=tk.RIGHT,fill=tk.BOTH)

        listbox = tk.Listbox(self.popup,yscrollcommand=scrollBar.set)
        listbox.pack(side=tk.RIGHT,fill=tk.BOTH,expand=1)
        for i in options:
            listbox.insert(tk.END,i)
        self.popup.minsize(width=300,height=400)
        self.popup.maxsize(width=300,height=400)
        self.popup.title("Disambiguation")
        listbox.bind('<<ListboxSelect>>',self.select)
        
    class StackModule(tk.Frame):
        title = None
        root = None
        body = None
        url = None
        def __init__(self,master):
            query = "Discrete Math"
            root = tk.Frame.__init__(self,master,height=100,width=300,bg="#0000ff")
            header = tk.Label(self,width=43,bg="#00ff00",text=query)
            
            site = Site(StackOverflow,'qB5xmT87jDlGGf*OjXrawQ((')
            site.be_inclusive()
            questionList = site.similar(query)
            question = questionList[0]
            questionID = question.question_id
            question = site.question(questionID)
            answer = question.url
            body = tk.Message(self,width=300,bg="#ff0000",text=str(question)+'\n'+str(answer))
            
            header.grid(column=0,row=0)
            body.grid(column=0,row=1)

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
            def rightClick_Wikipedia(e):
                self.wiki.updateModule(self.text.selection_get())
            e.widget.focus()
            
            nclst=[
                   (' Cut', lambda e=e: rightClick_Cut(e)),
                   (' Copy', lambda e=e: rightClick_Copy(e)),
                   (' Paste', lambda e=e: rightClick_Paste(e)),
                   (' Wikipedia', lambda e=e: rightClick_Wikipedia(e))
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
        self.wiki = WikiModule(webPane)
        self.wiki.grid()
        self.stk = StackModule(webPane)
        self.stk.grid()
        panes.add(textFrame)
        panes.add(webPane,minsize=300)
        panes.grid(column=0,row=0)
        scrollbar = tk.Scrollbar(textFrame)
        self.text = tk.Text(textFrame,width=100, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)
        self.text.pack(side=tk.RIGHT,fill=tk.BOTH,expand=1)

        self.wiki.grid_propagate(0)
        self.stk.grid_propagate(1)
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
