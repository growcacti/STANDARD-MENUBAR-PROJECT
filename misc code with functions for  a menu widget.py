def change_font(event=None):
   
    current_font_family = font_family.get()
    text.configure

# change font size
def change_font_size(event=None):
   
    current_font_size = font_size.get()
    text.configure(font=(current_font_family, current_font_size))

# change to bold
"""def change_bold(event=None):
    text_property = tk.font.Font(font = text['font'])
    if text_property.actual()['weight'] == "normal":
        text.configure(font = (current_font_family,current_font_size, "bold"))
    if text_property.actual()["weight"] == "bold":
        text.configure(font = (current_font_family,current_font_size, "normal"))"""

def change_bold(event=None):
    """toggle only selected text"""
    try:
        current_tags = text.tag_names("sel.first")
        if "bold" in current_tags:
            text.tag_remove("bold", "sel.first", "sel.last")
        else:
            text.tag_add("bold", "sel.first", "sel.last")
            bold_font = tk.font.Font(text, text.cget("font"))
            bold_font.configure(weight="bold")
            text.tag_configure("bold", font=bold_font)
    except tk.TclError:
        pass

# change to italic
def change_italic(event=None):
    """making italic the selected text"""
    try:
        current_tags = text.tag_names("sel.first")
        if "italic" in current_tags:
            text.tag_remove("italic", "sel.first", "sel.last")
        else:
            text.tag_add("italic", "sel.first", "sel.last")
            italic_font = tk.font.Font(text, text.cget("font"))
            italic_font.configure(slant="italic")
            text.tag_configure("italic", font=italic_font)
    except tk.TclError:
        pass

def underline_text(event=None):
    try:
        current_tags = text.tag_names("sel.first")
        if "underline" in current_tags:
            text.tag_remove("underline", "sel.first", "sel.last")
        else:
            text.tag_add("underline", "sel.first", "sel.last")
            underline_font = tk.font.Font(text, text.cget("font"))
            underline_font.configure(underline=1)
            text.tag_configure("underline", font=underline_font)
    except tk.TclError:
        pass

# change font color
def change_font_color(event=None):
    try:
        (rgb, hx) = tk.colorchooser.askcolor()
        text.tag_add("color", "sel.first", "sel.last")
        text.tag_configure("color", foreground=hx)
    except tk.TclError:
        pass

# left alignment
def align_left(event=None):
    text_content = text.get(1.0, "end")
    text.tag_config("left", justify=tk.LEFT)
    text.delete(1.0, tk.END)
    text.insert(tk.INSERT, text_content, "left")

# center alignment
def align_center(event=None):
    text_content = text.get(1.0, "end")
    text.tag_config("center", justify=tk.CENTER)
    text.delete(1.0, tk.END)
    text.insert(tk.INSERT, text_content, "center")

# text alignment right
def align_right(event=None):
    text_content = text.get(1.0, "end")
    text.tag_config("right", justify=tk.RIGHT)
    text.delete(1.0, tk.END)
    text.insert(tk.INSERT, text_content, "right")

font_box.bind("<<ComboboxSelected>>", change_font)
font_size_box.bind("<<ComboboxSelected>>", change_font_size)
