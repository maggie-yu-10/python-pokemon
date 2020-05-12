import tkinter as tk

# used to display end message


class EndFrame(tk.Frame):
    def __init__(self, master, hp1, hp2):
        super().__init__(
            master=master,
            bg='white',
            highlightbackground='black',
            highlightthickness=5)
        self.lb = tk.Label(
            self,
            text='you win',
            font=(
                'Times New Roman',
                20,
                'bold'),
            bg='white',
            height=4)
        self.lb.pack(fill=tk.BOTH, expand=True)

        self.yes = tk.Button(
            self,
            text='try again',
            font=(
                'Times New Roman',
                20),
            bg='grey',
            height=2,
            relief=tk.FLAT,
            command=None)
        self.yes.pack(fill=tk.BOTH, expand=True)

        self.hp1 = hp1
        self.hp2 = hp2
