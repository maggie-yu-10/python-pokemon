import tkinter as tk
import random
INTERVAL = 1000  # 1000ms = 1s


def player_attack(lb, text, damage, health, event=None):
    lb.config(text=text)
    lb.after(INTERVAL * 1, lambda: lb.config(text='Gutmann PH -%d' % damage))  # 1000ms
    lb.after(INTERVAL * 1, lambda: health.config(value=max(0, health['value'] - damage)))


def enemy_attack(lb, health, event=None):

    t1 = ['u failed all your classes',
          'u are forced to transfer to college',
          'u got kicked out']

    t2 = ['your PH -30',
          'your PH -20',
          'you die']
    damages = [20, 30, float('inf')]

    n = random.randint(0, len(t1) - 1)
    lb.after(INTERVAL * 2, lambda: lb.config(text=t1[n]))
    lb.after(INTERVAL * 3, lambda: lb.config(text=t2[n]))
    lb.after(INTERVAL * 3, lambda: health.config(value=max(0, health['value'] - damages[n])))

    if n == 2:
        lb.after(INTERVAL * 4, lambda: lb.config(text='plz choose another character from your party'))

def is_end(hp1, hp2, end_frame):
    if hp2['value'] == 0:
        end_frame.lb.config(text='you win')
        end_frame.yes.config(text='another round?')

    elif hp1['value'] == 0:
        end_frame.lb.config(text='you lose')
        end_frame.yes.config(text='another character?')

    end_frame.place(x=100, y=50, width=300, height=200)


def one_turn(lb, text, damage, hp1, hp2, end_frame, event=None):
    player_attack(lb, text, damage, hp2, event)
    enemy_attack(lb, hp1, event)
    lb.after(INTERVAL * 5, lambda: is_end(hp1, hp2, end_frame))


class EndFrame(tk.Frame):
    def __init__(self, master, hp1, hp2):
        super().__init__(master=master, bg='white', highlightbackground='black', highlightthickness=5)
        self.lb = tk.Label(self, text='you win', font=('Times New Roman', 20, 'bold'), bg='white', height=4)
        self.lb.pack(fill=tk.BOTH, expand=True)

        self.yes = tk.Button(self, text='another round?', font=('Times New Roman', 20),
                             bg='grey', height=2, relief=tk.FLAT, command=self.replay)
        self.yes.pack(fill=tk.BOTH, expand=True)

        self.hp1 = hp1
        self.hp2 = hp2

    def replay(self):
        self.hp1.config(value=100)
        self.hp2.config(value=100)
        self.place_forget()

