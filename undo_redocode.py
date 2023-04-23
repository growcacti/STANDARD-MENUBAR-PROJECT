
class CEntry(tk.Entry):
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self._undo_stack = deque(maxlen=100)
        self._redo_stack = deque(maxlen=100)
        self.bind("<Control-z>", self.undo)
        self.bind("<Control-y>", self.redo)
        # traces whenever the Entry's contents are changed
        self.tkvar = tk.StringVar()
        self.config(textvariable=self.tkvar)
        self.trace_id = self.tkvar.trace("w", self.on_changes)
        self.reset_undo_stacks()
        # USE THESE TO TURN TRACE OFF THEN BACK ON AGAIN
        # self.tkvar.trace_vdelete("w", self.trace_id)
        # self.trace_id = self.tkvar.trace("w", self.on_changes)

    def undo(self, event=None):  # noqa
        if len(self._undo_stack) <= 1:
            return
        content = self._undo_stack.pop()
        self._redo_stack.append(content)
        content = self._undo_stack[-1]
        self.tkvar.trace_vdelete("w", self.trace_id)
        self.delete(0, tk.END)
        self.insert(0, content)
        self.trace_id = self.tkvar.trace("w", self.on_changes)

    def redo(self, event=None):  # noqa
        if not self._redo_stack:
            return
        content = self._redo_stack.pop()
        self._undo_stack.append(content)
        self.tkvar.trace_vdelete("w", self.trace_id)
        self.delete(0, tk.END)
        self.insert(0, content)
        self.trace_id = self.tkvar.trace("w", self.on_changes)

    def on_changes(self, a=None, b=None, c=None):  # noqa
        self._undo_stack.append(self.tkvar.get())
        self._redo_stack.clear()

    def reset_undo_stacks(self):
        self._undo_stack.clear()
        self._redo_stack.clear()
        self._undo_stack.append(self.tkvar.get())
