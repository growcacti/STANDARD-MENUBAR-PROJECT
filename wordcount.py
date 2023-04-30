import tkinter as tk
from tkinter import ttk,Toplevel,Listbox,Scrollbar, END
from string import punctuation
from collections import Counter



class Wordcount(object):


    def  __init__(self, text):
        self.rt = tk.Tk()
       
        self.lb = tk.Listbox(self.rt,height=20,selectmode=tk.EXTENDED)
        self.sc = ttk.Scrollbar(self.rt, orient=tk.VERTICAL, command=self.lb.yview)
        self.lb['yscrollcommand'] = self.sc.set
        self.sc.pack(side=tk.LEFT, expand=True, fill=tk.Y)
        self.lb.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.text = text
        self.text2 =  ''.join(c for c in self.text.lower() if c not in punctuation)
        self.mostcommon_count = Counter(self.text2.split()).most_common()
        self.mc_cnt =  self.mostcommon_count
        self.search_loop()
        self.word = ""
        self.freq = 0
        
    def search_loop(self):
       
        for self.word, self.freq in self.mc_cnt:
            print("{:3d}  {}".format(self.freq, self.word))
            self.lb.insert(END, "{:3d}  {}".format(self.freq, self.word))

        self.mc_cnt_w = sorted(self.mc_cnt)
        self.mc_cnt_fw = sorted(self.mc_cnt_w, key=lambda tup: tup[1], reverse=True)
        
