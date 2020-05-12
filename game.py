from pokemon import Pokemon
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
from PIL import ImageTk, Image, ImageOps
from tkinter.font import Font
from helper import EndFrame
import random
from tkinter.font import Font


INTERVAL = 1500  # 1500ms = 1.5s

# creates new window to work with
window = Tk()
window.title('CIS192 Pokemon Battle')

# sets window size to width x height
window.geometry('500x800')
font = Font(family='Courier', size='16', weight='bold')

# places teal text box
msg_lb = Label(
    window,
    text='',
    bg='#68A0A0',
    fg='white',
    font=font,
    wraplength=450,
    justify=LEFT)
msg_lb.place(x=20, y=225)

# health bars 1: me, 2: opponent
health1 = ttk.Progressbar(
    window,
    style='health.Horizontal.TProgressbar',
    orient='horizontal',
    length=100,
    maximum=100,
    value=100)
health1.place(x=374, y=188)
health2 = ttk.Progressbar(
    window,
    style='health.Horizontal.TProgressbar',
    orient='horizontal',
    length=100,
    maximum=100,
    value=100)
health2.place(x=110, y=64)

# changes style of health bars
s = ttk.Style()
s.theme_use('classic')
s.configure(
    'health.Horizontal.TProgressbar',
    foreground='medium spring green',
    background='medium spring green',
    troughcolor='antiquewhite1',
    borderwidth=0,
    thickness=6)

# end window popup
end_frame = EndFrame(window, health1, health2)


#  helper method for rendering images
def render_image(name, w, h):
    img = Image.open(name)
    img = img.resize((w, h), Image.ANTIALIAS)
    img_render = ImageTk.PhotoImage(img)
    return img_render


# list of backgrounds to cycle through
backgrounds = [
    render_image(
        'backgrounds/ptampons.png',
        495,
        300),
    render_image(
        'backgrounds/pvanpelt.png',
        495,
        300),
    render_image(
        'backgrounds/plove.png',
        495,
        300),
    render_image(
        'backgrounds/plocust.png',
        495,
        300),
    render_image(
        'backgrounds/phuntsman.png',
        495,
        300)]

# creates all pokemon
you = Pokemon(
    'cis student',
    100,
    'you/you.png',
    'you/youb.png',
    'you/youblvl.png',
    'you/youw.png',
    'you/soylent.png',
    'you/officehours.png',
    'you/code.png',
    'you/cry.png')
you.add_move('Soylent', 30, 'u chug chocolate soylent',
             'u land a powerful hit! cis student deals 30 damage')
you.add_move('Office Hours', 20, 'u ask OH for help',
             'TAs help u fight! cis student deals 20 damage.')
you.add_move('Code', 1, 'u attempt to use ML to destroy ur opponent',
             'too bad u only know scratch. cis student deals 1 damage.')
you.add_move('Cry', 0, ':\'( being a cis student is difficult',
             'ur opponent shows no pity for u. cis student deals 0 damage.')

tia = Pokemon(
    'tia',
    100,
    'tia/tia.png',
    'tia/tiab.png',
    'tia/tiablvl.png',
    'tia/tiaw.png',
    'tia/tiktok.png',
    'tia/slytherinsnake.png',
    'tia/aiattack.png',
    'tia/internshipflex.png')
tia.add_move(
    'Tiktok',
    20,
    'tia plays her quarantine tiktok video',
    'opponent is mad that they do not have as many tiktok fans as tia. tia deals 20 damage.')
tia.add_move(
    'Slytherin Snake',
    30,
    'tia lets out wharton\'s snake.',
    'snake bites opponent. tia deals 30 damage.')
tia.add_move(
    'AI Attack',
    20,
    'tia, a cis student, uses AI to figure out opponent\'s weakness',
    'weakness attacked! tia deals 20 damage.')
tia.add_move(
    'Internship Flex',
    0,
    'tia tries to flex her internship on her opponent.',
    'tia forgets she has no internship. tia deals 0 damage.')

maggie = Pokemon(
    'maggie',
    100,
    'maggie/maggie.png',
    'maggie/maggieb.png',
    'maggie/maggieblvl.png',
    'maggie/maggiew.png',
    'maggie/nintendoswitch.png',
    'maggie/teado.png',
    'maggie/chillyphilly.png',
    'maggie/splurge.png')
maggie.add_move(
    'Nintendo Switch',
    20,
    'maggie pulls out animal crossing!',
    'enemy is anguished that they do not have one too :( maggie deals 20 damage.')
maggie.add_move(
    'Tea-do',
    30,
    'maggie is disgusted with teado\'s low quality boba.',
    'frustrated, she hurls tapioca pearls. maggie deals 30 damage.')
maggie.add_move('Chilly Philly', -10, 'maggie summons chilling winds to stop her opponent in their tracks!',
                'but she forgot she cannot handle temperatures below 70 F. bay area weather is too good. maggie deals -10 damage.')
maggie.add_move(
    'Splurge',
    30,
    'maggie steals the enemy\'s wallet!',
    'she steals 100000000$ and buys tickets to every Disney park in the world. maggie deals 30 damage.')

amyg = Pokemon(
    'amyg',
    100,
    'amyg/amyg.png',
    'amyg/amygb.png',
    'amyg/amygblvl.png',
    None,
    None,
    None,
    None,
    None)
amyg.add_move('Universal Fail', 30, 'u failed all your classes',
              'your GPA is now 1.0. amy deals 30 damage.')
amyg.add_move(
    'Internal Transfer',
    20,
    'u are forced to transfer to the college',
    'Amy says: "no more CIS for u." amy deals 20 damage.')
amyg.add_move(
    'Eviction Notice',
    float('inf'),
    'u get kicked out of penn',
    'Kicked out of Penn?? you die. amy deals infinite damage.')
amyg.add_move(
    'Flex',
    30,
    'amy g flexes on u with her salary',
    'Amy says: "most of ur tuition goes towards building my mansion." amy deals 30 damage.')

squirrel = Pokemon(
    'Angry Squirrel',
    100,
    'squirrel/squirrel.png',
    'squirrel/squirrelb.png',
    'squirrel/squirrelblvl.png',
    None,
    None,
    None,
    None,
    None)
squirrel.add_move(
    'Rummage',
    40,
    'angry squirrel rummages through a trashcan for a weapon.',
    'angry squirrel finds a bomb and throws it at u! squirrel deals 40 damage.')
squirrel.add_move(
    'Break-in',
    30,
    'angry squirrel breaks into ur dorm! it\'s the squirrel\'s place now.',
    'you are now homeless. you are devastated. angry squirrel deals 20 damage.')
squirrel.add_move(
    'Golden Shower',
    10,
    'angry squirrel jumps on your face and pees on you! you smell awful!',
    'luckily you are an engineering student and cannot smell the difference. angry squirrel deals 10 damage')
squirrel.add_move(
    'Eat Grape',
    0,
    'angry squirrel finds a grape on the ground and starts to eat.',
    'who knew that squirrels peeled their grapes before eating them? angry squirrel deals 0 damage.')

gs = Pokemon(
    'Goldman Sachs',
    100,
    'gs/gs.png',
    'gs/gsb.png',
    'gs/gsblvl.png',
    None,
    None,
    None,
    None,
    None)
gs.add_move(
    'Rejection Email',
    30,
    'Dear applicant, thank you for your application to Goldman Sachs.',
    'This year\'s applicant pool was extremely strong; In light of this we were unable to offer you a spot. goldman sachs deals 30 damage.')
gs.add_move(
    'Sell Out',
    0,
    'goldman sachs tempts u with a six figure salary!',
    'ur resolve is strong and u refuse to become a snake. goldman sachs deals 0 damage.')
gs.add_move(
    'Career Fair',
    20,
    'goldman sachs is at the career fair!',
    'wharton students trample u as they run to the recruting table. goldman sachs deals 20 damage.')
gs.add_move(
    'Snake',
    30,
    'goldman sachs releases a venomous cobra!',
    'you didn\'t expect them to have literal snakes! goldman sachs deals 30 damage.')

# p1: good guys, p2: bad guys
p1_list = [you, tia, maggie]
p2_list = [amyg, squirrel, gs]

# creates action bar
bot_render = render_image('backgrounds/bartemp1.png', 495, 100)
bot_img = Label(name='bot_img', image=bot_render)
bot_img.image = bot_render
bot_img.place(x=0, y=300)

# insert p1's (You) icon
you_render = render_image(p1_list[0].avatar, 100, 90)
you_img = Label(name='you_img', image=you_render, borderwidth=0)
you_img.image = you_render
you_img.place(x=90, y=115)

# inserts you's name in white and black, and their level
you_textw_render = render_image(p1_list[0].namew_img, 100, 27)
you_textw_img = Label(
    name='you_textw_img',
    image=you_textw_render,
    borderwidth=0,
    bg='#315066')
you_textw_img.place(x=22, y=355)
you_textb_render = render_image(p1_list[0].nameb_img, 70, 20)
you_textb_img = Label(
    name='you_textb_img',
    image=you_textb_render,
    borderwidth=0,
    bg='#f8f8d8')
you_textb_img.place(x=310, y=162)
you_textb_lvl_render = render_image(p1_list[0].nameblvl_img, 13, 15)
you_textb_lvl_img = Label(
    name='you_textb_lvl_img',
    image=you_textb_lvl_render,
    borderwidth=0,
    bg='#f8f8d8')
you_textb_lvl_img.place(x=455, y=165)

# inserts p2's (AmyG) icon
op_render = render_image(p2_list[0].avatar, 80, 100)
op_img = Label(name='op_img', image=op_render, borderwidth=0)
op_img.image = op_render
op_img.place(x=320, y=30)

# inserts amyg's name in black, and their level
op_textb_render = render_image(p2_list[0].nameb_img, 65, 18)
op_textb_img = Label(
    name='op_textb_img',
    image=op_textb_render,
    borderwidth=0,
    bg='#f8f8d8')
op_textb_img.place(x=45, y=38)
op_textb_lvl_render = render_image(p2_list[0].nameblvl_img, 12, 17)
op_textb_lvl_img = Label(
    image=op_textb_lvl_render,
    borderwidth=0,
    bg='#f8f8d8')
op_textb_lvl_img.place(x=190, y=40)


# action performed when attack button is clicked
def attack_click():
    fr = Frame(window, highlightthickness=0, width=495, height=347)
    fr.place(x=0, y=400)

    # inserts attack bottom screen template
    p1_atckimg_render = render_image('attackimagetemplate.png', 495, 347)
    p1_atckimg_img = Label(fr, image=p1_atckimg_render)
    p1_atckimg_img.image = p1_atckimg_render
    p1_atckimg_img.place(x=0, y=0)

    # inserts button for 1st move
    b1_photo = render_image(p1_list[0].attack1_img, 180, 50)
    b1 = Button(
        fr,
        image=b1_photo,
        command=lambda: one_turn(
            fr,
            msg_lb,
            0,
            health1,
            health2,
            end_frame,
            p1_list[0],
            p2_list[0]))
    b1.image = b1_photo
    b1.config(highlightthickness=0)
    b1.place(x=33, y=75)

    # inserts button for 2nd move
    b2_photo = render_image(p1_list[0].attack2_img, 180, 50)
    b2 = Button(
        fr,
        image=b2_photo,
        command=lambda: one_turn(
            fr,
            msg_lb,
            1,
            health1,
            health2,
            end_frame,
            p1_list[0],
            p2_list[0]))
    b2.image = b2_photo
    b2.config(highlightthickness=0)
    b2.place(x=283, y=75)

    # inserts button for 3rd move
    b3_photo = render_image(p1_list[0].attack3_img, 180, 50)
    b3 = Button(
        fr,
        image=b3_photo,
        command=lambda: one_turn(
            fr,
            msg_lb,
            2,
            health1,
            health2,
            end_frame,
            p1_list[0],
            p2_list[0]))
    b3.image = b3_photo
    b3.config(highlightthickness=0)
    b3.place(x=33, y=190)

    # inserts button for 4th move
    b4_photo = render_image(p1_list[0].attack4_img, 180, 50)
    b4 = Button(
        fr,
        image=b4_photo,
        command=lambda: one_turn(
            fr,
            msg_lb,
            3,
            health1,
            health2,
            end_frame,
            p1_list[0],
            p2_list[0]))
    b4.image = b4_photo
    b4.config(highlightthickness=0)
    b4.place(x=283, y=190)


# action performed when canada goose icon is clicked
def bag_cgoose(fr, but, lb, hp1, end_frame, p1, p2, event=None):
    lb.config(text=p1_list[0].name + ' takes out a Canada Goose jacket!')
    lb.after(INTERVAL, lambda: lb.config(text=''))
    lb.after(
        INTERVAL *
        2,
        lambda: lb.config(
            text='you put it on, but quickly realize it doesn\'t do much. at least you\'ll look cool while fighting.'))
    lb.after(INTERVAL * 4, lambda: lb.config(text=''))

    # p2's turn
    y = enemy_attack(lb, hp1, p1_list[0], p2_list[0], event)

    # checks health of p1
    if y <= 0 and len(p1_list) > 1:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! ' +
                p1_list[1].name +
                ' replaces ' +
                p1_list[0].name))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    elif y <= 0:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! '))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    else:
        msg_lb.after(
            INTERVAL * 12,
            lambda: msg_lb.config(
                text="it's your turn now!"))
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=''))
    fr.destroy()


# action performed when phone icon is clicked
def bag_phone(fr, but, lb, hp1, end_frame, p1, p2, event=None):
    lb.config(text=p1_list[0].name + ' takes out an iPhone!')
    lb.after(INTERVAL * 1, lambda: lb.config(text=''))
    lb.after(
        INTERVAL * 2,
        lambda: lb.config(
            text='you go on Facebook. Procrastination feels great! you heal for 10'))
    lb.after(
        INTERVAL *
        2,
        lambda: health1.config(
            value=min(
                100,
                health1['value'] +
                10)))
    p1_list[0].health = min(100, health1['value'] + 10)
    lb.after(INTERVAL * 4, lambda: lb.config(text=''))

    # p2's turn
    y = enemy_attack(lb, health1, p1, p2, event)

    # checks health of p1
    if y <= 0 and len(p1_list) > 1:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! ' +
                p1_list[1].name +
                ' replaces ' +
                p1_list[0].name))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    elif y <= 0:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! '))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    else:
        msg_lb.after(
            INTERVAL * 12,
            lambda: msg_lb.config(
                text="it's your turn now!"))
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=''))
    fr.destroy()


# action performed when wawa is clicked
def bag_wawa(fr, but, lb, hp1, end_frame, p1, p2, event=None):
    lb.config(text=p1.name + ' takes out a moldy Wawa breakfast burrito!')
    lb.after(INTERVAL, lambda: lb.config(text=''))
    lb.after(
        INTERVAL * 2,
        lambda: lb.config(
            text='Nothing hits the spot like wawa. Your health is fully restored.'))
    lb.after(INTERVAL * 2, lambda: health1.config(value=100))
    lb.after(INTERVAL * 4, lambda: lb.config(text=''))
    p1_list[0].health = 100

    # p2's turn
    y = enemy_attack(lb, health1, p1, p2, event)

    # checks health of p1
    if y <= 0 and len(p1_list) > 1:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! ' +
                p1_list[1].name +
                ' replaces ' +
                p1_list[0].name))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    elif y <= 0:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! '))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    else:
        msg_lb.after(
            INTERVAL * 12,
            lambda: msg_lb.config(
                text="it's your turn now!"))
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=''))
    fr.destroy()


# action performed when bag is clicked
def bag_click():
    fr = Frame(window, highlightthickness=0, width=495, height=347)
    fr.place(x=0, y=400)

    # inserts image template for opening bag
    bag_img_render = render_image('bag/bagtemplate.png', 495, 347)
    bag_img_img = Label(fr, image=bag_img_render)
    bag_img_img.image = bag_img_render
    bag_img_img.place(x=0, y=0)

    # inserts canada goose button
    b1_photo = render_image('bag/cgoosep.png', 130, 150)
    b1 = Button(
        fr,
        image=b1_photo,
        name='bag_cgoose',
        command=lambda: bag_cgoose(
            fr,
            b1,
            msg_lb,
            health1,
            end_frame,
            p1_list[0],
            p2_list[0]))
    b1.image = b1_photo
    b1.config(highlightthickness=0)
    b1.place(x=200, y=30)

    # inserts phone button
    b2_photo = render_image('bag/phonep.png', 80, 150)
    b2 = Button(
        fr,
        image=b2_photo,
        name='bag_phonep',
        command=lambda: bag_phone(
            fr,
            b2,
            msg_lb,
            health1,
            end_frame,
            p1_list[0],
            p2_list[0]))
    b2.image = b2_photo
    b2.config(highlightthickness=0)
    b2.place(x=375, y=30)

    # inserts wawa button
    b3_photo = render_image('bag/wawap.png', 180, 80)
    b3 = Button(
        fr,
        image=b3_photo,
        name='bag_wawa',
        command=lambda: bag_wawa(
            fr,
            b3,
            msg_lb,
            health1,
            end_frame,
            p1_list[0],
            p2_list[0]))
    b3.image = b3_photo
    b3.config(highlightthickness=0)
    b3.place(x=250, y=200)


# action performed when clicking on a party member
def party_click_helper(p1, fr):
    # active fighter is swapping out
    msg_lb.config(text=p1_list[0].name + ' is swapping out!')
    msg_lb.after(INTERVAL * 1, lambda: msg_lb.config(text=""))

    # reorders list so active fighter is first
    p0_temp = p1_list[0]
    p1_index = p1_list.index(p1)
    p1_list[0] = p1
    p1_list[p1_index] = p0_temp

    # destroys and replaces p1 image and text
    window.winfo_children()[6].destroy()
    you_render = render_image(p1_list[0].avatar, 100, 90)
    you_img = Label(name='you_img', image=you_render, highlightthickness=0)
    you_img.image = you_render
    you_img.place(x=90, y=115)
    you_img.lower(belowThis='.you_textw_img')
    window.winfo_children()[7].destroy()
    you_textw_render = render_image(p1_list[0].namew_img, 100, 27)
    you_textw_img = Label(
        name='you_textw_img',
        image=you_textw_render,
        borderwidth=0,
        bg='#315066')
    you_textw_img.image = you_textw_render
    you_textw_img.place(x=22, y=355)
    you_textw_img.lower(belowThis='.you_textb_img')
    window.winfo_children()[8].destroy()
    you_textb_render = render_image(p1_list[0].nameb_img, 70, 20)
    you_textb_img = Label(
        name='you_textb_img',
        image=you_textb_render,
        borderwidth=0,
        bg='#f8f8d8')
    you_textb_img.image = you_textb_render
    you_textb_img.place(x=310, y=162)
    you_textb_img.lower(belowThis='.you_textb_lvl_img')
    window.winfo_children()[9].destroy()
    you_textb_lvl_render = render_image(p1_list[0].nameblvl_img, 13, 15)
    you_textb_lvl_img = Label(
        name='you_textb_lvl_img',
        image=you_textb_lvl_render,
        borderwidth=0,
        bg='#f8f8d8')
    you_textb_lvl_img.image = you_textb_lvl_render
    you_textb_lvl_img.place(x=455, y=165)
    you_textb_lvl_img.lower(belowThis='.op_img')

    # text box and health bar update
    msg_lb.config(text=p1_list[0].name + ' steps up!')
    health1.config(value=p1_list[0].health)
    msg_lb.after(INTERVAL * 1, lambda: msg_lb.config(text=""))
    msg_lb.after(
        INTERVAL * 2,
        lambda: msg_lb.config(
            text='is this a great strategy, or a grave mistake?'))
    msg_lb.after(INTERVAL * 3, lambda: msg_lb.config(text=""))
    msg_lb.after(
        INTERVAL * 4,
        lambda: msg_lb.config(
            text='the enemy takes advantage of the time it took to switch in and swiftly attacks!'))
    msg_lb.after(INTERVAL * 5, lambda: msg_lb.config(text=""))

    # p2's turn
    y = enemy_attack(msg_lb, health1, p1_list[0], p2_list[0])

    # checks health of p1
    if y <= 0 and len(p1_list) > 1:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! ' +
                p1_list[1].name +
                ' replaces ' +
                p1_list[0].name))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    elif y <= 0:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! '))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    else:
        msg_lb.after(
            INTERVAL * 12,
            lambda: msg_lb.config(
                text="it's your turn now!"))
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=''))

    # deletes party frame
    fr.destroy()


# action performed when phone icon is clicked
def party_click():
    # bring up party frame
    fr = Frame(window, highlightthickness=0, width=495, height=347)
    fr.place(x=0, y=400)

    # inserts party image template
    party_img_render = render_image('party/partytemplate.png', 495, 347)
    party_img_img = Label(fr, image=party_img_render)
    party_img_img.image = party_img_render
    party_img_img.place(x=0, y=0)

    # creates buttons of members in party
    if len(p1_list) >= 2:
        b1_photo = render_image(
            'party/' +
            p1_list[1].name +
            'profile.png',
            200,
            300)
        b1 = Button(
            fr,
            image=b1_photo,
            name=p1_list[1].name +
            '_profile',
            command=lambda: party_click_helper(
                p1_list[1],
                fr))
        b1.image = b1_photo
        b1.config(highlightthickness=0)
        b1.place(x=30, y=45)

    if len(p1_list) is 3:
        b2_photo = render_image(
            'party/' +
            p1_list[2].name +
            'profile.png',
            200,
            300)
        b2 = Button(
            fr,
            image=b2_photo,
            name=p1_list[2].name +
            '_profile',
            command=lambda: party_click_helper(
                p1_list[2],
                fr))
        b2.image = b2_photo
        b2.config(highlightthickness=0)
        b2.place(x=270, y=45)


def change_background():
    # insert top background
    top_render = backgrounds[0]
    backgrounds.remove(top_render)
    backgrounds.append(top_render)
    top_img = Label(name='top_img', image=top_render)
    top_img.image = top_render
    top_img.place(x=0, y=0)
    top_img.lower()


# insert top background
change_background()


# action performed when flee button is clicked
def flee_click():
    # change background
    window.winfo_children()[0].destroy()
    change_background()

    msg_lb.config(text='You tried to run away, but your opponents follow you!')
    msg_lb.after(INTERVAL, lambda: msg_lb.config(text=''))
    msg_lb.after(
        INTERVAL * 2,
        lambda: msg_lb.config(
            text='Your opponent corners you and attacks!'))
    msg_lb.after(INTERVAL * 3, lambda: msg_lb.config(text=''))

    # p2's turn
    y = enemy_attack(msg_lb, health1, p1_list[0], p2_list[0])

    # checkes health of p1
    if y <= 0 and len(p1_list) > 1:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! ' +
                p1_list[1].name +
                ' replaces ' +
                p1_list[0].name))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    elif y <= 0:
        msg_lb.after(
            INTERVAL *
            12,
            lambda: msg_lb.config(
                text=p1_list[0].name +
                ' fainted! '))
        window.after(INTERVAL * 12, remove_p1)
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
        msg_lb.after(
            INTERVAL * 14,
            lambda: msg_lb.config(
                text="it's your turn now!"))
    else:
        msg_lb.after(
            INTERVAL * 12,
            lambda: msg_lb.config(
                text="it's your turn now!"))
        msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=''))


# creates attack button
atck_photo = render_image('attack.png', 90, 30)
atck = Button(window, image=atck_photo, command=attack_click)
atck.place(x=275, y=320)

# creates bag button
bag_photo = render_image('bag.png', 70, 30)
bag = Button(window, image=bag_photo, command=bag_click)
bag.place(x=395, y=320)

# creates party button
party_photo = render_image('party.png', 70, 30)
party = Button(window, image=party_photo, command=party_click)
party.place(x=275, y=355)

# creates flee button
flee_photo = render_image('flee.png', 70, 30)
flee = Button(window, image=flee_photo, command=flee_click)
flee.place(x=395, y=355)


# called when p2 health reaches 0
def remove_p2():
    op_img = window.winfo_children()[10].destroy()
    p2_list.pop(0)
    if len(p2_list) > 0:
        op_render = render_image(p2_list[0].avatar, 80, 100)
        op_img = Label(name='new_op_img', image=op_render, borderwidth=0)
        op_img.image = op_render
        op_img.place(x=320, y=30)
        op_img.lower(belowThis='.op_textb_img')
        op_textb_render = render_image(p2_list[0].nameb_img, 65, 18)
        op_textb_img = Label(
            name='op_textb_img',
            image=op_textb_render,
            borderwidth=0,
            bg='#f8f8d8')
        op_textb_img.image = op_textb_render
        op_textb_img.place(x=45, y=38)
        op_textb_lvl_render = render_image(p2_list[0].nameblvl_img, 12, 17)
        op_textb_lvl_img = Label(
            image=op_textb_lvl_render,
            borderwidth=0,
            bg='#f8f8d8')
        op_textb_lvl_img.image = op_textb_lvl_render
        op_textb_lvl_img.place(x=190, y=40)
        health2.config(value=100)
        msg_lb.config(text=p2_list[0].name + ' appears! it\'s your turn now!')
    # checks for victory condition
    else:
        congrats_render = render_image('congrats.png', 500, 800)
        congrats_img = Label(name='congrats_img', image=congrats_render)
        congrats_img.image = congrats_render
        congrats_img.place(x=0, y=0)
        end_frame.lb.config(text='you win!')
        end_frame.yes.config(text='another round?')
        end_frame.lift()
        end_frame.after(
            2500, lambda: end_frame.place(
                x=100, y=50, width=300, height=200))


# called when p1's health reaches 0
def remove_p1():
    window.winfo_children()[6].destroy()
    p1_list.pop(0)
    if len(p1_list) > 0:
        you_render = render_image(p1_list[0].avatar, 100, 90)
        you_img = Label(name='you_img', image=you_render)
        you_img.image = you_render
        you_img.place(x=90, y=115)
        you_img.lower(belowThis='.you_textw_img')
        window.winfo_children()[7].destroy()
        you_textw_render = render_image(p1_list[0].namew_img, 100, 27)
        you_textw_img = Label(
            name='you_textw_img',
            image=you_textw_render,
            borderwidth=0,
            bg='#315066')
        you_textw_img.image = you_textw_render
        you_textw_img.place(x=22, y=355)
        you_textw_img.lower(belowThis='.you_textb_img')
        window.winfo_children()[8].destroy()
        you_textb_render = render_image(p1_list[0].nameb_img, 70, 20)
        you_textb_img = Label(
            name='you_textb_img',
            image=you_textb_render,
            borderwidth=0,
            bg='#f8f8d8')
        you_textb_img.image = you_textb_render
        you_textb_img.place(x=310, y=162)
        you_textb_img.lower(belowThis='.you_textb_lvl_img')
        window.winfo_children()[9].destroy()
        you_textb_lvl_render = render_image(p1_list[0].nameblvl_img, 10, 15)
        you_textb_lvl_img = Label(
            name='you_textb_lvl_img',
            image=you_textb_lvl_render,
            borderwidth=0,
            bg='#f8f8d8')
        you_textb_lvl_img.image = you_textb_lvl_render
        you_textb_lvl_img.lower(belowThis='.op_img')
        you_textb_lvl_img.place(x=455, y=165)

        # configures health bar
        health1.config(value=p1_list[0].health)
    # checks for defeat condition
    else:
        toobad_render = render_image('toobad.png', 500, 800)
        toobad_img = Label(name='toobad_img', image=toobad_render)
        toobad_img.image = toobad_render
        toobad_img.place(x=0, y=0)
        end_frame.lb.config(text='you lose :(')
        end_frame.yes.config(text='try again')
        end_frame.lift()
        end_frame.after(
            2500, lambda: end_frame.place(
                x=100, y=50, width=300, height=200))


# helper method used in one_turn for p1's attack, returns p2's new health
def player_attack(lb, move, health, p1, p2, event=None):
    t = p1_list[0].name + ' used ' + p1_list[0].move_list[move].name + \
        "! " + p1_list[0].move_list[move].desc1
    msg_lb.config(
        text=t,
        font=Font(
            family="Courier",
            size="16",
            weight="bold"))
    lb.after(INTERVAL * 1, lambda: msg_lb.config(text=""))
    lb.after(
        INTERVAL * 2,
        lambda: msg_lb.config(
            text=p1_list[0].move_list[move].desc2))  # 1000ms
    h = health['value'] - p1_list[0].move_list[move].damage
    lb.after(INTERVAL * 2, lambda: health.config(value=max(0, h)))
    lb.after(INTERVAL * 3, lambda: msg_lb.config(text=""))
    return h


# helper method used in one_turn for p2's attack, returns p1's health
def enemy_attack(lb, hp1, p1, p2, event=None):

    t1 = [
        p2_list[0].name +
        ' uses ' +
        p2_list[0].move_list[0].name +
        "! " +
        p2_list[0].move_list[0].desc1,
        p2_list[0].name +
        ' uses ' +
        p2_list[0].move_list[1].name +
        "! " +
        p2_list[0].move_list[1].desc1,
        p2_list[0].name +
        ' uses ' +
        p2_list[0].move_list[2].name +
        "! " +
        p2_list[0].move_list[2].desc1,
        p2_list[0].name +
        ' uses ' +
        p2_list[0].move_list[3].name +
        "! " +
        p2_list[0].move_list[3].desc1]

    t2 = [p2_list[0].move_list[0].desc2, p2_list[0].move_list[1].desc2,
          p2_list[0].move_list[2].desc2, p2_list[0].move_list[3].desc2]

    n = random.randint(0, len(t1) - 1)
    lb.after(INTERVAL * 6, lambda: lb.config(text=t1[n]))
    lb.after(INTERVAL * 8, lambda: lb.config(text=""))
    lb.after(INTERVAL * 9, lambda: lb.config(text=t2[n]))
    h = hp1.cget("value") - p2_list[0].move_list[n].damage
    p1_list[0].health = h
    lb.after(INTERVAL * 9, lambda: health1.config(value=max(0, h)))
    lb.after(INTERVAL * 11, lambda: lb.config(text=""))
    return h


# action performed when one of the attack moves are clicked
def one_turn(fr, lb, move, hp1, hp2, end_frame, p1, p2, event=None):
    # p1 attacks
    x = player_attack(lb, move, hp2, p1_list[0], p2_list[0], event)
    if x <= 0:
        lb.after(
            INTERVAL *
            6,
            lambda: lb.config(
                text=p2_list[0].name +
                ' fainted!'))
        lb.after(INTERVAL * 7, lambda: lb.config(text=""))
        window.after(INTERVAL * 8, remove_p2)

    # p1 attacks
    else:
        y = enemy_attack(lb, hp1, p1_list[0], p2_list[0])
        if y <= 0 and len(p1_list) > 1:
            msg_lb.after(
                INTERVAL *
                12,
                lambda: msg_lb.config(
                    text=p1_list[0].name +
                    ' fainted! ' +
                    p1_list[1].name +
                    ' replaces ' +
                    p1_list[0].name))
            window.after(INTERVAL * 12, remove_p1)
            msg_lb.after(INTERVAL * 13, lambda: msg_lb.config(text=""))
            msg_lb.after(
                INTERVAL * 14,
                lambda: msg_lb.config(
                    text="it's your turn now!"))
        elif y <= 0:
            msg_lb.after(
                INTERVAL *
                12,
                lambda: msg_lb.config(
                    text=p1_list[0].name +
                    ' fainted! '))
            window.after(INTERVAL * 12, remove_p1)
            lb.after(INTERVAL * 13, lambda: lb.config(text=""))
            lb.after(
                INTERVAL * 14,
                lambda: lb.config(
                    text="it's your turn now!"))
        else:
            lb.after(
                INTERVAL * 12,
                lambda: lb.config(
                    text="it's your turn now!"))
            lb.after(INTERVAL * 13, lambda: lb.config(text=''))
    # deletes attack frame after click
    fr.destroy()


# creates intro image
intro_render = render_image("intro.png", 500, 800)
intro_img = Label(name='intro_img', image=intro_render, borderwidth=0)
intro_img.image = intro_render
intro_img.lift()
intro_img.place(x=0, y=0)


def destroy_intro(intro_img, begin):
    intro_img.destroy()
    begin.destroy()


begin = Button(
    window,
    text='BEGIN',
    font=Font(
        family='Courier',
        size='30',
        weight='bold'),
    borderwidth=0,
    bg='#ffe3a9',
    width=8,
    height=2,
    command=lambda: destroy_intro(
        intro_img,
        begin))
begin.place(x=180, y=398)


window.mainloop()
