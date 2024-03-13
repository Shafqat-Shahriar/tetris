from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rockk_Sissor_Smash")
root.geometry("600x600")
root.resizable(0,0)
# root.iconbitmap("icon.ico")

#======Functions=====


scr_player = 0    # starting point set to zero of both players
scr_comp = 0

def score(result):
    global scr_player
    global scr_comp
    if result == "You win!":
        canvas_scoreboard1.delete('all')
        scr_player += 1
        canvas_scoreboard1.create_text(25,20, text=scr_player, fill='white', font=('Bebas', 30))
    if result == "You lose!":
        canvas_scoreboard2.delete('all')
        scr_comp += 1
        canvas_scoreboard2.create_text(25,20, text=scr_comp, fill='black', font=('Bebas', 30))

def rock(a):
    comp = random.choice(["rock", "paper", "scissor"])
    show_picked(a, comp)
    images_picked(a, comp)
    if comp == a:
        show_result("It's a tie!")
    elif comp == "paper":
        show_result("You lose!")
    elif comp == "scissor":
        show_result("You win!")

def paper(b):
    comp = random.choice(["rock", "paper", "scissor"])
    show_picked(b, comp)
    images_picked(b, comp)
    if comp == b:
        show_result("It's a tie!")
    elif comp == "scissor":
        show_result("You lose!")
    elif comp == "rock":
        show_result("You win!")

def scissor(c):
    comp = random.choice(["rock", "paper", "scissor"])
    show_picked(c, comp)
    images_picked(c, comp)
    if comp == c:
        show_result("It's a tie!")
    elif comp == "rock":
        show_result("You lose!")
    elif comp == "paper":
        show_result("You win!")

def show_picked(player, comp):
    canvas_screen1.delete('all')
    canvas_screen2.delete('all')
    player = canvas_screen1.create_text(90,200, text=player.upper(), fill="#302e2f", font=('Bebas', 25))
    comp = canvas_screen2.create_text(90,200, text=comp.upper(), fill="#302e2f", font=('Bebas', 25))  # says rock paper scissor

def show_result(e):
    canvas_screen3.delete('all')
    canvas_screen3.create_text(65,10, text=e, fill='white', font=('Bebas', 20))
    score(e)


def images_picked(player, comp):
    if player == "rock":
        canvas_screen1.create_image(0,2, anchor=NW, image=player_rock)
    elif player == "paper":
        canvas_screen1.create_image(0,2, anchor=NW, image=player_paper)
    elif player == "scissor":
        canvas_screen1.create_image(0,2, anchor=NW, image=player_scissor)
    if comp == "rock":
        canvas_screen2.create_image(0,2, anchor=NW, image=comp_rock)
    elif comp == "paper":
        canvas_screen2.create_image(0,2, anchor=NW, image=comp_paper)
    elif comp == "scissor":
        canvas_screen2.create_image(0,2, anchor=NW, image=comp_scissor)

def reset_game():
    canvas_scoreboard1.delete('all')
    canvas_scoreboard2.delete('all')
    canvas_screen1.delete('all')
    canvas_screen2.delete('all')
    canvas_screen3.delete('all')
    global scr_player
    global scr_comp
    scr_player = 0
    scr_comp = 0
    canvas_scoreboard1.create_text(25,20, text=scr_player, fill='white', font=('Bebas', 30))
    canvas_scoreboard2.create_text(25,20, text=scr_comp, fill='black', font=('Bebas', 30))


#======Images=========
"""
player_rock = ImageTk.PhotoImage(Image.open('rock.png'))
player_paper = ImageTk.PhotoImage(Image.open('paper.png'))
player_scissor = ImageTk.PhotoImage(Image.open('scissor.png'))
comp_rock = ImageTk.PhotoImage(Image.open('rock.png'))
comp_paper = ImageTk.PhotoImage(Image.open('paper.png'))
comp_scissor = ImageTk.PhotoImage(Image.open('scissor.png'))
"""


# s_logo = ImageTk.PhotoImage(Image.open('logo.png'))
scoreboard = ImageTk.PhotoImage(Image.open('scoreboard.png'))
scoreboard1 = ImageTk.PhotoImage(Image.open('scoreboard1.png'))
bg = ImageTk.PhotoImage(Image.open('bg.png'))
rock_button = ImageTk.PhotoImage(Image.open('rock_button.png'))
paper_button = ImageTk.PhotoImage(Image.open('paper_button.png'))
scissor_button = ImageTk.PhotoImage(Image.open('scissor_button.png'))
new_game = ImageTk.PhotoImage(Image.open('new_game.png'))
quit_game = ImageTk.PhotoImage(Image.open('quit_game.png'))



#=================== Resize =========================
# Resize the logo image
s_logo= Image.open('logo.png')
s_logo = s_logo.resize((200, 170), Image.ANTIALIAS)

# Convert the resized image into a PhotoImage
logo = ImageTk.PhotoImage(s_logo)



# Resize player rock image
player_rock_img = Image.open('rock.png')
player_rock_img = player_rock_img.resize((210, 176), Image.ANTIALIAS)
player_rock = ImageTk.PhotoImage(player_rock_img)

# Resize player paper image
player_paper_img = Image.open('paper.png')
player_paper_img = player_paper_img.resize((210, 176), Image.ANTIALIAS)
player_paper = ImageTk.PhotoImage(player_paper_img)

# Resize player scissor image
player_scissor_img = Image.open('scissor.png')
player_scissor_img = player_scissor_img.resize((210, 176), Image.ANTIALIAS)
player_scissor = ImageTk.PhotoImage(player_scissor_img)

# Resize comp rock image
comp_rock_img = Image.open('rock.png')
comp_rock_img = comp_rock_img.resize((210, 176), Image.ANTIALIAS)
comp_rock = ImageTk.PhotoImage(comp_rock_img)

# Resize comp paper image
comp_paper_img = Image.open('paper.png')
comp_paper_img = comp_paper_img.resize((210, 176), Image.ANTIALIAS)
comp_paper = ImageTk.PhotoImage(comp_paper_img)

# Resize comp scissor image
comp_scissor_img = Image.open('scissor.png')
comp_scissor_img = comp_scissor_img.resize((210, 176), Image.ANTIALIAS)
comp_scissor = ImageTk.PhotoImage(comp_scissor_img)





#=======CanvasWidgets====
canvas_main = Canvas(root, width = 600, height = 600)
canvas_main.place(x=-2, y=0)
canvas_main.create_image(0,0, anchor = NW, image = bg)
canvas_main.create_image(90,115, anchor = NW, image = scoreboard1)
canvas_main.create_image(12,70, anchor = NW, image = scoreboard)
canvas_main.create_image(405,0, anchor = NW, image = logo)
canvas_main.create_text(110,98, text='Shafqat', fill='black', font=('Bebas',9))
canvas_main.create_text(295,98, text='COMPUTER', fill='black', font=('Bebas',9))

canvas_screen1 = Canvas(root, bg='#618685', width=180, height=220, highlightbackground='#143d59') #         #709dff
canvas_screen1.place(x=10, y=167)
canvas_screen2 = Canvas(root, bg='#fefbd8', width=180, height=220, highlightbackground='#143d59')  #    #ff2e2a
canvas_screen2.place(x=205, y=167)
canvas_screen3 = Canvas(root, bg='#2d292a', width=130, height=25, highlightthickness=0)
canvas_screen3.place(x=140, y=130)



#================ Scoreboard ====================

canvas_scoreboard1 = Canvas(root, bg='black', width=50, height=40, highlightbackground='#D3D3D3')
canvas_scoreboard1.place(x=143, y=78)
canvas_scoreboard2 = Canvas(root, bg='white', width=50, height=40, highlightbackground='#D3D3D3')
canvas_scoreboard2.place(x=195, y=78)
canvas_scoreboard1.create_text(30,20, text=scr_player, fill='white', font=('Bebas',30))
canvas_scoreboard2.create_text(30,20, text=scr_player, fill='black', font=('Bebas',30))

#======Button======
button1 = Button(canvas_main, bg='#e8bf23', border=1, image=rock_button, command=lambda: rock("rock")).place(x=5, y=400)
button2 = Button(canvas_main, bg='#2ed755', border=1, image=paper_button, command=lambda: paper("paper")).place(x=205, y=400)
button3 = Button(canvas_main, bg='#03a8fd', border=1, image=scissor_button, command=lambda: scissor("scissor")).place(x=100, y=465)

button4 = Button(canvas_main, bg='#03a8fd', border=1, image=new_game, command=reset_game).place(x=40, y=550)
button5 = Button(canvas_main, bg='#ff6546', border=1, image=quit_game, command=root.quit).place(x=220, y=550)




root.mainloop()
