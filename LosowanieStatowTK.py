from tkinter import *
from random import randint


root = Tk()
root.title('Losowanie Statystyk')
root.geometry('400x400')
val = [0,0,0,0,0,0]
sum = 0
rest = 0

def losuj():
    sum = 0
    rest = 0
    while sum < 70:
        sum = 0
        for i in range(0,6):
            value = randint(1,6) + randint(1,6) + randint(1,6)
            val[i] = value
            sum = sum + value

    label_str_val = Label(root, text=val[0])
    label_dex_val = Label(root, text=val[1])
    label_con_val = Label(root, text=val[2])
    label_int_val = Label(root, text=val[3])
    label_wis_val = Label(root, text=val[4])
    label_cha_val = Label(root, text=val[5])
    label_str.grid(row=1, column=0)
    label_str_val.grid(row=1, column=2)
    label_dex.grid(row=2, column=0)
    label_dex_val.grid(row=2, column=2)
    label_con.grid(row=3, column=0)
    label_con_val.grid(row=3, column=2)
    label_int.grid(row=4, column=0)
    label_int_val.grid(row=4, column=2)
    label_wis.grid(row=5, column=0)
    label_wis_val.grid(row=5, column=2)
    label_cha.grid(row=6, column=0)
    label_cha_val.grid(row=6, column=2)
    label_sum_val = Label(root, text=sum)
    label_sum_val.grid(row=7, column=2)


def add(x):
    if rest > 0 and x < 18:
        x = x + 1
        rest = rest - 1

def sub(x):
    if x > 3:
        x = x - 1
        rest = rest + 1


# Labele
mainlabel = Label(root, text='Twoje Statystyki')
label_str = Label(root, text='Siła')
label_dex = Label(root, text='Zręczność')
label_con = Label(root, text='Kondycja')
label_int = Label(root, text='Inteligencja')
label_wis = Label(root, text='Mądrość')
label_cha = Label(root, text='Charyzma')
label_str_val = Label(root, text=val[0])
label_dex_val = Label(root, text=val[1])
label_con_val = Label(root, text=val[2])
label_int_val = Label(root, text=val[3])
label_wis_val = Label(root, text=val[4])
label_cha_val = Label(root, text=val[5])
label_sum = Label(root, text='Suma:')
label_sum_val = Label(root, text=sum)
label_rest = Label(root, text='Pozostało:')
label_rest_val = Label(root, text=rest)


# Grid-Labels
mainlabel.grid(row=0, columnspan=4)
label_str.grid(row=1, column=0)
label_str_val.grid(row=1, column=2)
label_dex.grid(row=2, column=0)
label_dex_val.grid(row=2, column=2)
label_con.grid(row=3, column=0)
label_con_val.grid(row=3, column=2)
label_int.grid(row=4, column=0)
label_int_val.grid(row=4, column=2)
label_wis.grid(row=5, column=0)
label_wis_val.grid(row=5, column=2)
label_cha.grid(row=6, column=0)
label_cha_val.grid(row=6, column=2)
label_sum.grid(row=7, column=0)
label_sum_val.grid(row=7, column=2)
label_rest.grid(row=9, column=0)
label_rest_val.grid(row=9, column=2)

# Buttons
sub_str = Button(root, text='-', command=None, state=DISABLED)
add_str = Button(root, text='+', command=None, state=DISABLED)
sub_dex = Button(root, text='-', command=None, state=DISABLED)
add_dex = Button(root, text='+', command=None, state=DISABLED)
sub_con = Button(root, text='-', command=None, state=DISABLED)
add_con = Button(root, text='+', command=None, state=DISABLED)
sub_int = Button(root, text='-', command=None, state=DISABLED)
add_int = Button(root, text='+', command=None, state=DISABLED)
sub_wis = Button(root, text='-', command=None, state=DISABLED)
add_wis = Button(root, text='+', command=None, state=DISABLED)
sub_cha = Button(root, text='-', command=None, state=DISABLED)
add_cha = Button(root, text='+', command=None, state=DISABLED)

losuj_btn = Button(root, text='Losuj', command=losuj)

# Grid - Buttons
sub_str.grid(row=1, column=1)
add_str.grid(row=1, column=3)
sub_dex.grid(row=2, column=1)
add_dex.grid(row=2, column=3)
sub_con.grid(row=3, column=1)
add_con.grid(row=3, column=3)
sub_int.grid(row=4, column=1)
add_int.grid(row=4, column=3)
sub_wis.grid(row=5, column=1)
add_wis.grid(row=5, column=3)
sub_cha.grid(row=6, column=1)
add_cha.grid(row=6, column=3)
losuj_btn.grid(row=8, columnspan=4)


# Mainloop
root.mainloop()