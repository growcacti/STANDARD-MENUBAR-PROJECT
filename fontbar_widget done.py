import tkinter as tk
from tkinter import ttk

from tkinter import font
from tkinter import filedialog, messagebox, Toplevel, Frame, Scrollbar,Canvas 
import tkinter.scrolledtext as st
from tkinter import *
import tkinter.colorchooser
import os, pathlib
import glob
import time
import runpy

teststr = (
"""


# Python program to replace text in a file
x = input("enter text to be replaced:")
y = input("enter text that will replace:")
 
# file.txt should be replaced with
# the actual text file name
f = open("file.txt", "r+")
 
# each sentence becomes an element in the list l
l = f.readlines()
 
# acts as a counter to know the
# index of the element to be replaced
c = 0
for i in l:
    if x in i:
 
        # Replacement carries the value
        # of the text to be replaced
        Replacement = i.replace(x, y)
 
        # changes are made in the list
        l = Replacement
    c += 1
 
# The pre existing text in the file is erased
f.truncate(0)
 
# the modified list is written into
# the file thereby replacing the old text
f.writelines(l)
f.close()
print("Text successfully replaced")

Output:
Enter text to be replaced: Geeks
Enter text that will replace: Geekforgeeks
Text successfully replaced
Method 3: Using the OS module to replace the file with new text
We use the os module to rename a new file with the original file name. In this method instead of editing the already existing file, we instead create a new file with the modified content and then delete the old file and rename the new file.

# Program to replace text in a file
import os
x = input("Enter text that will replace the existing text:")
f = open("file.txt", "r+")
f1 = open("new.txt", "r+")
 
f1.write(x)
os.remove("file.txt")
os.rename("new.txt", "file.txt")
f1.close()
 
print("File replaced")

Output:
Enter text that will replace the existing text: geeks
File replaced
Method 4: Using fileinput.input()
The fileinput.input() method gets the file as the input line by line and is mainly utilized for appending and updating the data in the given file. The fileinput and sys module need to be imported to the current Python code in order to run the code without any errors. The following code uses the fileinput.input() function for replacing the text in a line in Python.

import sys
import fileinput
 
x = input("Enter text to be replaced:")
y = input("Enter replacement text")
 
for l in fileinput.input(files = "file.txt"):
    l = l.replace(x, y)
    sys.stdout.write(l)

Output:
Enter text to be replaced: Geeks
Enter replacement text: Geeksforgeeks
""")







class FontBar(tk.Tk):
    def __init__(self, parent,teststr):
        super().__init__()
        self.path = os.getcwd()
        self.parent = parent
        self.fram = tk.Frame(self.parent, width=150, height=40)
        self.fram.grid(row=0, column=0)
        self.text= st.ScrolledText(self.parent, height=55, width=100)
        self.text.grid(row=10,column=0)
        self.text.insert("1.0", teststr)
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
        self.text.configure(font=("Arial", 12))
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
        self.text.configure(font=(self.current_font_family, self.current_font_size))
        self.fontsize.bind("<<ComboboxSelected>>", lambda event : self.change_font_size())
        self.fontbox.bind("<<ComboboxSelected>>",lambda event, : self.change_font())
    def change_fonttype(self,type, size):
        self.type = self.fontbox.get()
        self.size = self.fontsize.get()
        self.text.configure(font=(self.type, self.size))
       
    # change font size
    def change_font_size(self, size, event=None):
        self.fontbox.bind("<<ComboboxSelected>>", lambda event: self.change_font_size)
        self.size = size
        self.current_font_size = self.fontsize.get()
        self.text.configure(font=(self.fontbox.get(), self.size))
        self.fontbox.bind("<<ComboboxSelected>>", lambda event: self.change_font_size)

    

    def change_bold(self,event=None):
        """toggle only selected text"""
        try:
            self.current_tags = self.text.tag_names("sel.first")
            if "bold" in self.current_tags:
                self.text.tag_remove("bold", "sel.first", "sel.last")
            else:
                self.text.tag_add("bold", "sel.first", "sel.last")
                bold_font = tk.font.Font(self.text, self.text.cget("font"))
                bold_font.configure(weight="bold")
                self.text.tag_configure("bold", font=bold_font)
        except tk.TclError as ex:
            print(ex)

    # change to italic
    def change_italic(self, event=None):
        """making italic the selected text"""
        try:
            self.current_tags = self.text.tag_names("sel.first")
            if "italic" in self.current_tags:
                self.text.tag_remove("italic", "sel.first", "sel.last")
            else:
                self.text.tag_add("italic", "sel.first", "sel.last")
                italic_font = tk.font.Font(self.text, self.text.cget("font"))
                italic_font.configure(slant="italic")
                self.text.tag_configure("italic", font=italic_font)
        except tk.TclError:
            pass

    def underline_text(self, event=None):
        try:
            self.current_tags = self.text.tag_names("sel.first")
            if "underline" in self.current_tags:
                self.text.tag_remove("underline", "sel.first", "sel.last")
            else:
                self.text.tag_add("underline", "sel.first", "sel.last")
                underline_font = tk.font.Font(self.text, self.text.cget("font"))
                underline_font.configure(underline=1)
                self.text.tag_configure("underline", font=underline_font)
        except tk.TclError:
            pass

    # change font color
    def change_font_color(self, event=None):
        try:
            (rgb, hx) = tk.colorchooser.askcolor()
            self.text.tag_add("color", "sel.first", "sel.last")
            self.text.tag_configure("color", foreground=hx)
            # self.text.tag_configure(rgb, foreground=hx)
        except tk.TclError as ex:
            print(ex)

    # left alignment
    def align_left(self,event=None):
        text_content = self.text.get(1.0, "end")
        self.text.tag_config("left", justify=tk.LEFT)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.INSERT, text_content, "left")

    # center alignment
    def align_center(self,event=None):
        text_content = self.text.get(1.0, "end")
        self.text.tag_config("center", justify=tk.CENTER)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.INSERT, text_content, "center")

    # text alignment right
    def align_right(self, event=None):
        text_content = self.text.get(1.0, "end")
        self.text.tag_config("right", justify=tk.RIGHT)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.INSERT, text_content, "right")

    def changeall_bold(self):
   
   
        self.text.tag_add("bold", "1.0", "end")
        bold_font = tk.font.Font(self.text, self.text.cget("font"))
        bold_font.configure(weight="bold")
        self.text.tag_configure("bold", font=bold_font)
   
    def changeall_italic(self):

        self.text.tag_add("italic", "1.0", "end")
        italic_font = tk.font.Font(self.text, self.text.cget("font"))
        italic_font.configure(slant="italic")
        self.text.tag_configure("italic", font=italic_font)
       
    def changeall_underline(self):

        self.text.tag_add("underline", "1.0", "end")
        underline_font = tk.font.Font(self.text, self.text.cget("font"))
        underline_font.configure(underline=1)
        self.text.tag_configure("underline", font=underline_font)

    def destory(self):
        self.fram.grid_forget()
       
    text_change = False

    def changed(self, event=None):
        pass
       
##        if text.edit_modified():
##            self.text_change = text_change
##            words = len(self.text.get(1.0, "end-1c").split())
##            characters = len(self.text.get(1.0, "end-1c"))
##            self.status.config(text=f"Characters : {characters} Words : {words}")
##            self.text.edit_modified(False)
##
##    self.text.bind("<<Modified>>", changed)
##    

def main():
    root = tk.Tk()
    app = FontBar(root,teststr)
    app.mainloop()


if __name__ == '__main__':
    main()







