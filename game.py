from pokemon import Pokemon
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps

from helper import one_turn, EndFrame

window = Tk()
window.title("CIS192 Pokemon Battle")

# sets window size to width x height
window.geometry('500x800')

s = ttk.Style()
s.theme_use('classic')
s.configure("health.Horizontal.TProgressbar", foreground='medium spring green', background='medium spring green', troughcolor='antiquewhite1', borderwidth=0, thickness=6)

# creates text
# lbl = Label(window, text = "Hello")
# lbl.grid(column=0, row=0)

# creates all pokemon
you = Pokemon(name="you", level=5, basehealth=100, health=100, atck=80, defense=80, speed=50)
you.add_move("Soylent", 0, 2, 1, 1)
you.add_move("Office Hours", 0, 1, 1, 2)
you.add_move("Code", 30, 1, 1, 1)
you.add_move("Cry", 0, 1, 1, 1)

def render_image(name):
    img = Image.open(name)
    img_render = ImageTk.PhotoImage(img)
    return img_render

# Pokemon 1 and Pokemon 2
def attack_click():
    # if p1.getName is "you":
    p1_atckimg = Image.open("attackimagetemplate.png")
    p1_atckimg = p1_atckimg.resize((495, 347), Image.ANTIALIAS)
    p1_atckimg_render = ImageTk.PhotoImage(p1_atckimg)
    p1_atckimg_img = Label(image=p1_atckimg_render)
    p1_atckimg_img.image = p1_atckimg_render
    p1_atckimg_img.place(x=0, y=400)

    b1_img = Image.open("you/soylent.png")
    b1_img = b1_img.resize((180, 50), Image.ANTIALIAS)
    b1_photo = ImageTk.PhotoImage(b1_img)
    b1 = Button(image=b1_photo, command=lambda: one_turn(msg_lb, 'Your move: soylent',
                                                         10, health1, health2, end_frame))
    b1.image = b1_photo
    b1.config(highlightthickness=0)
    b1.place(x=33, y=475)

    b2_img = Image.open("you/officehours.png")
    b2_img = b2_img.resize((180, 50), Image.ANTIALIAS)
    b2_photo = ImageTk.PhotoImage(b2_img)
    b2 = Button(window, image=b2_photo, command=lambda: one_turn(msg_lb, 'Your move: Force Amy to attend OH',
                                                                 10, health1, health2, end_frame))
    b2.image = b2_photo
    b2.config(highlightthickness=0)
    b2.place(x=283, y=475)

    b3_img = Image.open("you/code.png")
    b3_img = b3_img.resize((180, 50), Image.ANTIALIAS)
    b3_photo = ImageTk.PhotoImage(b3_img)
    b3 = Button(image=b3_photo, command=lambda: one_turn(msg_lb, 'Your move: Make Amy Code CS homework',
                                                         20, health1, health2, end_frame))
    b3.image = b3_photo
    b3.config(highlightthickness=0)
    b3.place(x=33, y=590)

    b4_img = Image.open("you/cry.png")
    b4_img = b4_img.resize((180, 50), Image.ANTIALIAS)
    b4_photo = ImageTk.PhotoImage(b4_img)
    b4 = Button(window, image=b4_photo, command=lambda: one_turn(msg_lb, 'Your move: Cry to Amy about college life',
                                                                 5, health1, health2, end_frame))
    b4.image = b4_photo
    b4.config(highlightthickness=0)
    b4.place(x=283, y=590)

    cancel_img = Image.open("cancel.png")
    cancel_img = cancel_img.resize((400, 40), Image.ANTIALIAS)
    cancel_photo = ImageTk.PhotoImage(cancel_img)
    cancel = Button(window, image=cancel_photo, command=quit)
    cancel.image = cancel_photo
    cancel.config(highlightthickness=0)
    cancel.place(x=45, y=703)


    '''b1_img_render = render_image("you/soylent.png")
    b1 = Button(height=25, width=190, image=b1_img_render)
    b1.image = render_image("you/soylent.png")
    b1.place(x=25, y=450)
    b2 = Button(window, height=25, width=190, image=render_image("you/officehours.png"))
    b3 = Button(window, height=25, width=190, image=render_image("you/code.png"))
    b4 = Button(window, height=25, width=190, image=render_image("you/cry.png"))

    b2.place(x=250, y=350)
    b3.place(x=25, y=400)
    b4.place(x=250, y=400)'''

tia = Pokemon(name="tia", level=10, basehealth=100, health=100, atck=50, defense=50, speed=50)
# maggie = Pokemon(name="maggie", level=10, basehealth=100, health=100, atck=50, defense=50, speed=50)
# amyg = Pokemon(name="amyg", level=99, basehealth=200, health=200, atck=30, defense=30, speed=1)
# squirrel = Pokemon(name="squirrel", level=2, basehealth=50, health=50, atck=300, defense=1, speed=100)
# gs = Pokemon(name="gs", level=15, basehealth=100, health=100, atck=90, defense=70, speed=40)


# insert top background
top = Image.open("./backgrounds/template1.png")
top = top.resize((495, 300), Image.ANTIALIAS)
top_render = ImageTk.PhotoImage(top)
top_img = Label(image=top_render)
top_img.image = top_render
top_img.place(x=0, y=0)

# insert bottom screen
bot = Image.open("./backgrounds/bartemp1.png")
bot = bot.resize((495, 100), Image.ANTIALIAS)
bot_render = ImageTk.PhotoImage(bot)
bot_img = Label(image=bot_render)
bot_img.image = bot_render
bot_img.place(x=0, y=300)

# You in battle
you = Image.open("./you/you.png")
you = you.resize((100, 90), Image.ANTIALIAS)
you_render = ImageTk.PhotoImage(you)
you_img = Label(image=you_render)
you_img.image = you_render
you_img.place(x=90, y=115)

#insert youtext
you_textw = Image.open("./you/youw.png")
you_textw = you_textw.resize((100, 27), Image.ANTIALIAS)
you_textw_render = ImageTk.PhotoImage(you_textw)
you_textw_img = Label(image=you_textw_render, borderwidth=0, bg='#315066')
you_textw_img.place(x=22, y=355)
you_textb = Image.open("./you/youb.png")
you_textb = you_textb.resize((70, 20), Image.ANTIALIAS)
you_textb_render = ImageTk.PhotoImage(you_textb)
you_textb_img = Label(image=you_textb_render, borderwidth=0, bg='#f8f8d8')
you_textb_img.place(x=310, y=162)
you_textb_lvl = Image.open("./you/youblvl.png")
you_textb_lvl = you_textb_lvl.resize((5, 15), Image.ANTIALIAS)
you_textb_lvl_render = ImageTk.PhotoImage(you_textb_lvl)
you_textb_lvl_img = Label(image=you_textb_lvl_render, borderwidth=0, bg='#f8f8d8')
you_textb_lvl_img.place(x=455, y=165)


# Amy G in battle
amyg = Image.open("./amyg.png")
amyg = amyg.resize((80, 100), Image.ANTIALIAS)
amyg_render = ImageTk.PhotoImage(amyg)
amyg_img = Label(image=amyg_render)
amyg_img.image = amyg_render
amyg_img.place(x=320, y=30)

# insert amygtext
amyg_textb = Image.open("./amygb.png")
amyg_textb = amyg_textb.resize((65, 18), Image.ANTIALIAS)
amyg_textb_render = ImageTk.PhotoImage(amyg_textb)
amyg_textb_img = Label(image=amyg_textb_render, borderwidth=0, bg='#f8f8d8')
amyg_textb_img.place(x=45, y=38)
amyg_textb_lvl = Image.open("./amygblvl.png")
amyg_textb_lvl = amyg_textb_lvl.resize((12, 17), Image.ANTIALIAS)
amyg_textb_lvl_render = ImageTk.PhotoImage(amyg_textb_lvl)
amyg_textb_lvl_img = Label(image=amyg_textb_lvl_render, borderwidth=0, bg='#f8f8d8')
amyg_textb_lvl_img.place(x=190, y=40)

# creates attack button
atck_img = Image.open("./attack.png")
atck_img = atck_img.resize((90, 30), Image.ANTIALIAS)
atck_photo = ImageTk.PhotoImage(atck_img)
# TODO: FIX THIS
atck = Button(window, image=atck_photo, command=attack_click)
atck.place(x=275, y=320)

#creates bag button
bag_img = Image.open("./bag.png")
bag_img = bag_img.resize((70, 30), Image.ANTIALIAS)
bag_photo = ImageTk.PhotoImage(bag_img)
bag = Button(window, image=bag_photo)
bag.place(x=395, y=320)

# creates party button
party_img = Image.open("./party.png")
party_img = party_img.resize((70, 30), Image.ANTIALIAS)
party_photo = ImageTk.PhotoImage(party_img)
party = Button(window, image=party_photo)
party.place(x=275, y=355)

# creates flee button
flee_img = Image.open("./flee.png")
flee_img = flee_img.resize((70, 30), Image.ANTIALIAS)
flee_photo = ImageTk.PhotoImage(flee_img)
flee = Button(window, image=flee_photo)
flee.place(x=395, y=355)

# health bars 1: me, 2: opponent
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

msg_lb = Label(window, text='', bg='#68A0A0', fg='white', font=('Times New Roman', 20), wraplength=450, justify='left')
msg_lb.place(x=20, y=220)

end_frame = EndFrame(window, health1, health2)


window.mainloop()