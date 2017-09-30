from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
 
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()
 
def saveAs():
    f = asksaveasfile(defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oh No!", message="Unable to save file...")

def undo():
    	if not stack:
    		return
    	previous = stack.pop()
    	previous.undo()
def openFile():
    global filename
    file = askopenfile(parent=root,title='Select a File')
    filename = file.name
    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    file.close()    

def rightClick(e):
    try:
        def rightClick_Copy(e, apnd=0):
            e.widget.event_generate('<Control-c>')
        def rightClick_Cut(e):
            e.widget.event_generate('<Control-x>')
        def rightClick_Paste(e):
            e.widget.event_generate('<Control-v>')
        e.widget.focus()
        
        nclst=[
               (' Cut', lambda e=e: rightClick_Cut(e)),
               (' Copy', lambda e=e: rightClick_Copy(e)),
               (' Paste', lambda e=e: rightClick_Paste(e)),
               ]
        rmenu = Menu(None, tearoff=0, takefocus=0)

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
      
root = Tk()
 #scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=BOTH)


root.title("MonkeyCode Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)



text = Text(root, width=400, height=400, yscrollcommand=scrollbar.set)

scrollbar.config(command=text.yview)
if __name__ == '__main__':
    root.bind('<Button-3>',rightClick)
text.pack()
 
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label="Undo", command=openFile)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=openFile)
editmenu.add_command(label="Copy", command=saveFile)
editmenu.add_command(label="Paste", command=saveAs)
editmenu.add_command(label="Delete", command=root.quit)
editmenu.add_separator()
editmenu.add_command(label="Copy", command=saveFile)
editmenu.add_command(label="Copy", command=saveFile)
editmenu.add_command(label="Paste", command=saveAs)
editmenu.add_separator()
editmenu.add_command(label="Select All", command=openFile)
editmenu.add_command(label="Time & Date", command = openFile)
menubar.add_cascade(label="Edit", menu=editmenu)

root.config(menu=menubar)
root.mainloop()