import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter import messagebox as mb
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import filedialog

from tkinter import Button, Frame, Entry, END, Canvas

from tkinter.scrolledtext import ScrolledText 

import sys
import os



class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)
        self.parent= parent
        self.textwidget = ScrolledText(self.parent, height=50, width=100, bg='white',bd=10)
        self.textwidget.grid(row=10, column=0,sticky="nsew")
        self.canvas = tk.Canvas(self.parent, width=100, height=10,bg='lavender')
        self.canvas.grid(row=25, column=0)
        self.menubar = tk.Menu(self.parent, tearoff=False)
        self.file_menu = tk.Menu(self.menubar)
        self.edit_menu = tk.Menu(self.menubar)
        self.view_menu = tk.Menu(self.menubar)
        self.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", underline=1, command=lambda : self.clear())
        self.file_menu.add_command(label="Open", underline=1, command=lambda: self.open_file())
        self.file_menu.add_command(label="Save", underline=1, command=lambda:self.save_file())
        self.file_menu.add_command(label="readlines", underline=1, command=lambda : self.readlines())
        self.file_menu.add_command(label="-----", underline=1, command=self.quit)
        self.file_menu.add_command(label="-------", underline=1, command=self.quit)
        self.file_menu.add_command(label="Exit", underline=1, command=self.quit)
        
        self.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Select All", accelerator="Ctrl+A", compound="left", underline=0, command=lambda: self.textwidget.event_generate("<<SelectAll>>"))
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X", compound="left", underline=0, command=lambda: self.textwidget.event_generate("<<Cut>>"))
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C", compound="left", underline=0,  command=lambda: self.textwidget.event_generate('<<Copy>>'))
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V", compound="left", underline=0, command=lambda: self.textwidget.event_generate("<<Paste>>"))
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", compound="left", underline=0, command=lambda: self.undo())
        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", compound="left", underline=0, command=lambda : self.redo())
        self.edit_menu.add_command(label="Find", accelerator="Ctrl+F", compound="left", underline=0, command=lambda :self.find())
        self.edit_menu.add_command(label="Replace", accelerator="Ctrl+Z", compound="left", underline=0, command=lambda : self.replace())
        self.edit_menu.add_command(label="cleartags", accelerator="Ctrl+Z", compound="left", underline=0, command=lambda : self.cleartags())
        self.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Backgrounbd Color", compound="left", underline=0,  command=lambda: self.change_bg())
        self.view_menu.add_command(label="Foreground Color",compound="left", underline=0, command=lambda: self.change_fg())
        self.view_menu.add_command(label="Highlight Line",compound="left", underline=0, command=lambda: self.highlight_line())
        self.view_menu.add_command(label="Foreground Color",compound="left", underline=0, command=lambda: self.change_fg())
        


        self.char_detect()
       
    def cleartags(self):
        self.textwidget.tag_config('found', foreground ='black', background = 'white')

    def undo(self):
        try:
            
            self.textwidget.edit_undo()
        except:
            print("No previous action")
    def redo(self):
        try:
            self.textwidget.edit_redo()
        except:
            print("No previous action")

    def select_all(self, event=None):
        self.textwidget.tag_add("sel", "1.0", tk.END)
        return "break"


    def copy(self, event=None):
        self.clipboard_clear()
        text = self.textwidget.get("sel.first", "sel.last")
        self.clipboard_append(text)

    def cut(self, event):
        self.copy()
        self.delete("sel.first", "sel.last")

    def paste(self, event):
        text = self.selection_get(selection='CLIPBOARD')
        self.insert('insert', text)



    def quit(self):
        sys.exit(0)


    def clear(self):

        self.textwidget.delete("1.0", tk.END)
    def cleare1(self):
        self.e1.delete(0, END)
   

    def change_bg(self):
       
        (triple, hexstr) = askcolor()
        if hexstr:
            self.textwidget.config(bg=hexstr)


    def change_fg(self):
       
        (triple, hexstr) = askcolor()
        
        if hexstr:
            self.textwidget.config(fg=hexstr)


    def command(self):
        pass


    def open_file(self):
       
        '''Open a file for editing.'''
        filepath = askopenfilename(filetypes=[("Python Scripts", "*.py"),("Text Files", "*.txt"),('All Files', '*.*')])
        if not filepath:
            return
        self.textwidget.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            self.textwidget.insert(tk.END, text)
       
    def save_file(self):
       
        filepath = asksaveasfilename(
            defaultextension='py',
            filetypes=[('All Files', '*.*')],
        )
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            text = self.textwidget.get(1.0, tk.END)
            output_file.write(text)

    def readlines(self):
        filepath = askopenfilename(
            filetypes=[("All Files", "*.*")]
        )
        if not filepath:
            return
        self.textwidget.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.readlines()
            self.textwidget.insert(tk.END, text)
            return filepath2


    def ggtxt(self, textwidget):
        gettxt = self.tx.get("1.0", tk.END)
        self.textwidget.insert(tk.END, gettxt)

   


       
    def edit2(self, name):
        runpy.run_path(path_name="name")
    def find(self):
        top=Toplevel()
        label1 = tk.Label(top, text = "Find").grid(row=1, column=1) 
        entry1 =tk.Entry(top, width=15, bd=12, bg = "cornsilk")
        entry1.grid(row=2, column=1)
       
        def finder():
            # remove tag 'found' from index 1 to END
            self.textwidget.tag_remove('found', '1.0', END)
            entry = entry1.get()
      
         
            if (entry1):
                idx = '1.0'
                while 1:
                    # searches for desired string from index 1
                    idx = self.textwidget.search(entry, idx, nocase = 1,
                                    stopindex = END)
                     
                    if not idx: break
                     
                    # last index sum of current index and
                    # length of text
                    lastidx = '% s+% dc' % (idx, len(entry))
                     
         
                    # overwrite 'Found' at idx
                    self.textwidget.tag_add('found', idx, lastidx)
                    idx = lastidx
     
            # mark located string as red
             
                self.textwidget.tag_config('found',background="purple", foreground ='yellow')
              
        self.find_btn = tk.Button(top, text="Find", bd=8,command=finder)
        self.find_btn.grid(row=8, column=1)
        entry1.focus_set() 
    

    def replace(self):
        top=Toplevel()
        label1 = tk.Label(top, text = "Find").grid(row=1, column=1) 
        entry1 =tk.Entry(top, width=15, bd=12, bg = "cornsilk")
        entry1.grid(row=2, column=1)
        label2 = tk.Label(top, text = "Replace With ").grid(row=3, column=1)
        entry2 = tk.Entry(top, width=15, bd=12, bg = "seashell")
        entry2.grid(row=5, column=1)
        def replacer():
            # remove tag 'found' from index 1 to END
            self.textwidget.tag_remove('found', '1.0', END)
             
            # returns to widget currently in focus
            self.fin = entry1.get()
            self.repl = entry2.get()
             
            if (self.fin and self.repl):
                idx = '1.0'
                while 1:
                    # searches for desired string from index 1
                    idx = self.textwidget.search(self.fin, idx, nocase = 1,
                                    stopindex = END)
                    print(idx)
                    if not idx: break
                     
                    # last index sum of current index and
                    # length of text
                    lastidx = '% s+% dc' % (idx, len(self.fin))
         
                    self.textwidget.delete(idx, lastidx)
                    self.textwidget.insert(idx, self.repl)
         
                    lastidx = '% s+% dc' % (idx, len(self.repl))
                     
                    # overwrite 'Found' at idx
                    self.textwidget.tag_add('found', idx, lastidx)
                    idx = lastidx
     
            # mark located string as red
            self.textwidget.tag_config('found', foreground ='green', background = 'yellow')
        self.replace_btn = tk.Button(top, text="Find & Replace", bd=8,command=replacer)
        self.replace_btn.grid(row=8, column=1)
        entry1.focus_set()
##
##    def rowcol(self,ev=None):
##        top = Toplevel()
##        count = self.textwidget.count("1.0", "end")
##        e1=tk.Entry(top,bd=12,bg="light yellow")
##        e1.grid(row=1, column=1)
##        e1.insert(0, count)
##       
    def char_detect(self):
        pass
##        top = Toplevel()
##        count = len(self.textwidget.get("1.0", "end"))
##        e1=tk.Entry(top,bd=12,bg="light yellow")
##        e1.grid(row=1, column=1)
##        e1.insert(0,count)
##        print(count)
    def highlight_line(self,interval=100):
        self.textwidget.tag_remove("active_line", "1.0", tk.END)
        self.textwidget.tag_add("active_line", "insert linestart", "insert lineend+12c")
        self.textwidget.after(interval, self.toggle_highlight)

    def toggle_highlight(self, event=None):

        val = hltln.get()

        undo_highlight() if not val else highlight_line()


    
    def undo_highlight(self):

          self.textwidget.tag_remove("active_line", "1.0", tk.END)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)

if __name__ == "__main__":
    app=App()
    app.mainloop()
