import pokemon
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps
window = Tk()
window.title("CIS192 Pokemon Battle")

# sets window size to width x height
window.geometry('500x650')

# creates text
# lbl = Label(window, text = "Hello")
# lbl.grid(column=0, row=0)


# insert top background
top = Image.open("backgrounds/template1.png")
top = top.resize((495, 300), Image.ANTIALIAS)
top_render = ImageTk.PhotoImage(top)
top_img = Label(image=top_render)
top_img.image = top_render
top_img.place(x=0, y=0)

# insert bottom screen
bot = Image.open("backgrounds/bartemp1.png")
bot = bot.resize((495, 100), Image.ANTIALIAS)
bot_render = ImageTk.PhotoImage(bot)
bot_img = Label(image=bot_render)
bot_img.image = bot_render
bot_img.place(x=0, y=300)

# You in battle
you = Image.open("you.png")
you = you.resize((100, 90), Image.ANTIALIAS)
you_render = ImageTk.PhotoImage(you)
you_img = Label(image=you_render)
you_img.image = you_render
you_img.place(x=90, y=115)

#insert cisstudenttext
you_textw = Image.open("cisstudentw.png")
you_textw = you_textw.resize((100, 27), Image.ANTIALIAS)
you_textw_render = ImageTk.PhotoImage(you_textw)
you_textw_img = Label(image=you_textw_render, borderwidth=0, bg='#315066')
you_textw_img.place(x=22, y=355)
you_textb = Image.open("cisstudentb.png")
you_textb = you_textb.resize((70, 20), Image.ANTIALIAS)
you_textb_render = ImageTk.PhotoImage(you_textb)
you_textb_img = Label(image=you_textb_render, borderwidth=0, bg='#f8f8d8')
you_textb_img.place(x=310, y=162)
you_textb_lvl = Image.open("cisstudentblvl.png")
you_textb_lvl = you_textb_lvl.resize((5, 15), Image.ANTIALIAS)
you_textb_lvl_render = ImageTk.PhotoImage(you_textb_lvl)
you_textb_lvl_img = Label(image=you_textb_lvl_render, borderwidth=0, bg='#f8f8d8')
you_textb_lvl_img.place(x=455, y=165)


# Amy G in battle
amyg = Image.open("amyg.png")
amyg = amyg.resize((80, 100), Image.ANTIALIAS)
amyg_render = ImageTk.PhotoImage(amyg)
amyg_img = Label(image=amyg_render)
amyg_img.image = amyg_render
amyg_img.place(x=320, y=30)

# insert amygtext
amyg_textb = Image.open("amygb.png")
amyg_textb = amyg_textb.resize((65, 18), Image.ANTIALIAS)
amyg_textb_render = ImageTk.PhotoImage(amyg_textb)
amyg_textb_img = Label(image=amyg_textb_render, borderwidth=0, bg='#f8f8d8')
amyg_textb_img.place(x=45, y=38)
amyg_textb_lvl = Image.open("amygblvl.png")
amyg_textb_lvl = amyg_textb_lvl.resize((12, 17), Image.ANTIALIAS)
amyg_textb_lvl_render = ImageTk.PhotoImage(amyg_textb_lvl)
amyg_textb_lvl_img = Label(image=amyg_textb_lvl_render, borderwidth=0, bg='#f8f8d8')
amyg_textb_lvl_img.place(x=190, y=40)

# creates attack button
atck_img = Image.open("attack.png")
atck_img = atck_img.resize((90, 30), Image.ANTIALIAS)
atck_photo = ImageTk.PhotoImage(atck_img)
atck = Button(window, image=atck_photo, command=cisstudent_attack1)
atck.place(x=275, y=320)

#creates bag button
bag_img = Image.open("bag.png")
bag_img = bag_img.resize((70, 30), Image.ANTIALIAS)
bag_photo = ImageTk.PhotoImage(bag_img)
bag = Button(window, image=bag_photo)
bag.place(x=395, y=320)

# creates party button
party_img = Image.open("party.png")
party_img = party_img.resize((70, 30), Image.ANTIALIAS)
party_photo = ImageTk.PhotoImage(party_img)
party = Button(window, image=party_photo)
party.place(x=275, y=355)

# creates flee button
flee_img = Image.open("flee.png")
flee_img = flee_img.resize((70, 30), Image.ANTIALIAS)
flee_photo = ImageTk.PhotoImage(flee_img)
flee = Button(window, image=flee_photo)
flee.place(x=395, y=355)

# health bars 1: me, 2: opponent
s = ttk.Style()
s.theme_use('classic')
s.configure("health.Horizontal.TProgressbar", foreground='medium spring green', background='medium spring green', troughcolor='antiquewhite1', borderwidth=0, thickness=6)
health1 = ttk.Progressbar(window, style="health.Horizontal.TProgressbar", orient="horizontal", length=100, maximum=100, value=100)
health1.place(x=374, y=188)
# health1['value'] = 10
health2 = ttk.Progressbar(window, style="health.Horizontal.TProgressbar", orient="horizontal", length=100, maximum=100, value=100)
health2.place(x=110, y=64)


# txt = scrolledtext.ScrolledText(window, width=40, height=10)
# txt.grid(row=3, column=0)
# txt.insert(INSERT, "One day in Philadelphia, a CIS major walks signs up for CIS192")
# delta = 500 
# delay = 0
# for i in range(len(txt) + 1):
    # s = txt[:i]
    # update_text = lambda s=s: canvas.itemconfigure(canvas_text, text=s)
    # canvas.after(delay, update_text)
    # delay += delta
# TROUGH_COLOR = 'SystemButtonFace'
# BAR_COLOR = 'green'
# style.configure("bar.Horizontal.TProgressbar", troughcolor=TROUGH_COLOR, bordercolor=TROUGH_COLOR, background=BAR_COLOR, lightcolor=BAR_COLOR, darkcolor=BAR_COLOR)
# ttk.Progressbar(window, style="green.Horizontal.TProgressbar", orient="horizontal", length=100, mode="determinate", maximum=4, value=1).place(x=200, y=200)

# bar.place(x=200, y=200)



window.mainloop()