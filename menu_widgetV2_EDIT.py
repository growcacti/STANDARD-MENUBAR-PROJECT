import tkinter as tk
from tkinter import ttk, Toplevel
from tkinter import messagebox as mb
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import font
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
        self.font_menu = tk.Menu(self.menubar)
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
        
        self.add_cascade(label="Font", menu=self.font_menu)
        self.font_menu.add_command(label="FONTBAR", accelerator="Ctrl+B", compound="left", underline=0, command=lambda: FontBar(self.textwidget))
        self.font_menu.add_command(label="=+++", compound="left", underline=0, command=None)
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








class FontBar(ttk.Frame):
    def __init__(self, textwidget):
        super().__init__()
        self.path = os.getcwd()
        self.top = tk.Toplevel()
        self.fram = tk.Frame(self.top, width=150, height=40)
        self.fram.grid(row=0, column=0)
        self.textwidget=textwidget
        
       # Tool Bar & Shortcut Bar Frames
        self.toolbar = tk.Frame(self.fram, background="violet", width=20, height=5)
        self.toolbar.grid(row=1, column=1, columnspan=2, sticky="ew")

        self.shortcutbar = tk.Frame(self.fram, background="plum", height=5, width=80)
        self.shortcutbar.grid(row=0, column=1, columnspan=2, sticky="ew")   
        self.font_config()
    def font_config(self):
        self.toolbar = tk.Canvas(self.fram, bg="seashell")
        self.toolbar.grid(row=1, column=1, columnspan=3, sticky="ew")
        self.toolbar.config(width=300, height=60)
        self.values = [n for n in range(2,120, 2)]
       
        self.font_family = (
            tk.StringVar(self.toolbar)
        )  # string variable for storing value of font options from user
        self.fontbox = ttk.Combobox(
            self.toolbar, width=30, textvariable=self.font_family, state="readonly"
        )  # combobox
        self.fontbox["values"] = list(font.families())
        self.font_family.set("Arial")
        self.fontbox.grid(row=0, column=0)
        # font box ends here

        # font size box
        self.size = tk.IntVar(self.toolbar)
        self.fontsize= ttk.Combobox(self.toolbar, width=14, values=self.values, textvariable=self.size)
        
        self.size.set(12)
        self.fontsize.grid(row=0, column=1)
       

        self.current_font_family = self.font_family
        self.current_font_size = self.size
        self.textwidget.configure(font=("Arial", 12))
        self.fontbox.bind("<<ComboboxSelected>>", lambda event : self.change_font)
        self.fontsize.bind("<<ComboboxSelected>>", lambda event : self.change_font_size)
        self.fontbox.bind("<ButtonRelease-1>", lambda event : self.change_font)

        self.font_btn = tk.Button(self.toolbar, text=" Set Font", bd=3, bg="blue violet", command=lambda : self.change_fonttype(self.fontbox.get(), self.fontsize.get()))
        self.font_btn.grid(row=1, column=0)
        self.font_btn2 = tk.Button(self.toolbar,text="set size Font",bd=3,bg="blue violet",command=lambda : self.change_font_size(self.fontsize.get()))
        self.font_btn2.grid(row=1, column=1)
        self.color_btn= tk.Button(self.toolbar, text="Font color", bd=2, bg="goldenrod", command= lambda: self.change_font_color())
        self.color_btn.grid(row=1, column=2)
        self.bold_btn = tk.Button(self.toolbar, text="B", bd=3, bg="violet red", command=self.change_bold)
        self.bold_btn.grid(row=1, column=3)
        self.bold_btn2 = tk.Button(self.toolbar, text="All B", bd=2, bg="violet red", command=self.changeall_bold)
        self.bold_btn2.grid(row=0, column=3)
        self.italic_btn = tk.Button(self.toolbar, text="i", bd=3, bg="lawn green", command=self.change_italic)
        self.italic_btn.grid(row=1, column=4)
        self.italic_btn2 = tk.Button(self.toolbar, text="All i", bd=3, bg="lawn green", command=self.changeall_italic)
        self.italic_btn2.grid(row=0, column=4)
        self.underline_btn = tk.Button(self.toolbar, text="_", bd=3, bg="yellow", command=self.underline_text)
        self.underline_btn.grid(row=1, column=5)
        self.underline_btn2 = tk.Button(self.toolbar, text="All _", bd=3, bg="yellow", command=self.changeall_underline)
        self.underline_btn2.grid(row=0, column=5)
        self.align_left_btn = tk.Button(self.toolbar, text="LT", bd=3, bg="orange", command=self.align_left)
        self.align_left_btn.grid(row=1, column=6)
        self.align_center_btn = tk.Button(self.toolbar, text="CT", bd=3, bg="cyan", command=self.align_center)
        self.align_center_btn.grid(row=1, column=7)
        self.align_right_btn = tk.Button(self.toolbar, text="RT", bd=3, bg="light pink", command=self.align_right)
        self.align_right_btn.grid(row=1, column=8)
        self.destory_btn = tk.Button(self.toolbar, text="RM FONTBAR", bd=3, bg="light pink", command=self.destory)
        self.destory_btn.grid(row=0, column=8)
        # function to change font family
    def change_font(self,event=None):
        
        self.current_font_family = font_family.get()
        self.textwidget.configure(font=(self.current_font_family, self.current_font_size))
        self.fontsize.bind("<<ComboboxSelected>>", lambda event : self.change_font_size())
        self.fontbox.bind("<<ComboboxSelected>>",lambda event, : self.change_font())
    def change_fonttype(self,type, size):
        self.type = self.fontbox.get()
        self.size = self.fontsize.get()
        self.textwidget.configure(font=(self.type, self.size))
       
    # change font size
    def change_font_size(self, size, event=None):
        self.fontbox.bind("<<ComboboxSelected>>", lambda event: self.change_font_size)
        self.size = size
        if size  == int:
            self.font.size =self.size
        else:    
            self.font_size = self.fontsize.get()
        self.textwidget.configure(font=(self.fontbox.get(), self.font_size))
        self.fontbox.bind("<<ComboboxSelected>>", lambda event: self.change_font_size)

    

    def change_bold(self,event=None):
        """toggle only selected text"""
        try:
            self.current_tags = self.textwidget.tag_names("sel.first")
            if "bold" in self.current_tags:
                self.textwidget.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.textwidget.tag_add("bold", "sel.first", "sel.last")
                bold_font = tk.font.Font(self.textwidget, self.textwidget.cget("font"))
                bold_font.configure(weight="bold")
                self.textwidget.tag_configure("bold", font=bold_font)
        except tk.TclError as ex:
            print(ex)

    # change to italic
    def change_italic(self, event=None):
        """making italic the selected text"""
        try:
            self.current_tags = self.textwidget.tag_names("sel.first")
            if "italic" in self.current_tags:
                self.textwidget.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.textwidget.tag_add("italic", "sel.first", "sel.last")
                italic_font = tk.font.Font(self.textwidget, self.textwidget.cget("font"))
                italic_font.configure(slant="italic")
                self.textwidget.tag_configure("italic", font=italic_font)
        except tk.TclError:
            pass

    def underline_text(self, event=None):
        try:
            self.current_tags = self.textwidget.tag_names("sel.first")
            if "underline" in self.current_tags:
                self.textwidget.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.textwidget.tag_add("underline", "sel.first", "sel.last")
                underline_font = tk.font.Font(self.textwidget, self.textwidget.cget("font"))
                underline_font.configure(underline=1)
                self.textwidget.tag_configure("underline", font=underline_font)
        except tk.TclError:
            pass

    # change font color
    def change_font_color(self, event=None):
        try:
            (rgb, hx) = tk.colorchooser.askcolor()
            self.textwidget.tag_add("color", "sel.first", "sel.last")
            self.textwidget.tag_configure("color", foreground=hx)
            # self.textwidget.tag_configure(rgb, foreground=hx)
        except tk.TclError as ex:
            print(ex)

    # left alignment
    def align_left(self,event=None):
        textwidget_content = self.textwidget.get(1.0, "end")
        self.textwidget.tag_config("left", justify=tk.LEFT)
        self.textwidget.delete(1.0, tk.END)
        self.textwidget.insert(tk.INSERT, textwidget_content, "left")

    # center alignment
    def align_center(self,event=None):
        textwidget_content = self.textwidget.get(1.0, "end")
        self.textwidget.tag_config("center", justify=tk.CENTER)
        self.textwidget.delete(1.0, tk.END)
        self.textwidget.insert(tk.INSERT, textwidget_content, "center")

    # text alignment right
    def align_right(self, event=None):
        textwidget_content = self.textwidget.get(1.0, "end")
        self.textwidget.tag_config("right", justify=tk.RIGHT)
        self.textwidget.delete(1.0, tk.END)
        self.textwidget.insert(tk.INSERT, textwidget_content, "right")

    def changeall_bold(self):
   
   
        self.textwidget.tag_add("bold", "1.0", "end")
        bold_font = tk.font.Font(self.textwidget, self.textwidget.cget("font"))
        bold_font.configure(weight="bold")
        self.textwidget.tag_configure("bold", font=bold_font)
   
    def changeall_italic(self):

        self.textwidget.tag_add("italic", "1.0", "end")
        italic_font = tk.font.Font(self.textwidget, self.textwidget.cget("font"))
        italic_font.configure(slant="italic")
        self.textwidget.tag_configure("italic", font=italic_font)
       
    def changeall_underline(self):

        self.textwidget.tag_add("underline", "1.0", "end")
        underline_font = tk.font.Font(self.textwidget, self.textwidget.cget("font"))
        underline_font.configure(underline=1)
        self.textwidget.tag_configure("underline", font=underline_font)

    def destory(self):
        self.fram.grid_forget()































class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)



if __name__ == "__main__":
    app=App()
    app.mainloop()
