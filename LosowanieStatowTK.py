from tkinter import *
from random import randint


root = Tk()
root.title('Losowanie Statystyk')
root.geometry('150x300')
val = [0, 0, 0, 0, 0, 0]
remember_throw = []
sum = 0
rest = 0


def losuj():
    global rest
    global sum
    rest = 0
    sum = 0
    while sum < 65:
        sum = 0
        for i in range(6):
            value = randint(1,6) + randint(1,6) + randint(1,6)
            val[i] = value
            sum = sum + value

    label_str_val = Label(root, text=val[0])
    label_dex_val = Label(root, text=val[1])
    label_con_val = Label(root, text=val[2])
    label_int_val = Label(root, text=val[3])
    label_wis_val = Label(root, text=val[4])
    label_cha_val = Label(root, text=val[5])
    label_sum_val = Label(root, text=sum)
    label_rest_val = Label(root, text=rest)
    label_str_val.grid(row=1, column=2)
    label_dex_val.grid(row=2, column=2)
    label_con_val.grid(row=3, column=2)
    label_int_val.grid(row=4, column=2)
    label_wis_val.grid(row=5, column=2)
    label_cha_val.grid(row=6, column=2)
    label_sum_val.grid(row=7, column=2)
    label_rest_val.grid(row=8, column=2)


def add(x):
    global rest
    if 18 > val[x] and rest > 0:
        val[x] = val[x] + 1
        rest = rest - 1

    label_str_val = Label(root, text=val[0])
    label_dex_val = Label(root, text=val[1])
    label_con_val = Label(root, text=val[2])
    label_int_val = Label(root, text=val[3])
    label_wis_val = Label(root, text=val[4])
    label_cha_val = Label(root, text=val[5])
    label_rest_val = Label(root, text=rest)
    label_str_val.grid(row=1, column=2)
    label_dex_val.grid(row=2, column=2)
    label_con_val.grid(row=3, column=2)
    label_int_val.grid(row=4, column=2)
    label_wis_val.grid(row=5, column=2)
    label_cha_val.grid(row=6, column=2)
    label_rest_val.grid(row=8, column=2)



def sub(x):
    global rest
    if val[x] > 3 and rest >= 0:
        val[x] = val[x] - 1
        rest = rest + 1

    label_str_val = Label(root, text=val[0])
    label_dex_val = Label(root, text=val[1])
    label_con_val = Label(root, text=val[2])
    label_int_val = Label(root, text=val[3])
    label_wis_val = Label(root, text=val[4])
    label_cha_val = Label(root, text=val[5])
    label_rest_val = Label(root, text=rest)
    label_str_val.grid(row=1, column=2)
    label_dex_val.grid(row=2, column=2)
    label_con_val.grid(row=3, column=2)
    label_int_val.grid(row=4, column=2)
    label_wis_val.grid(row=5, column=2)
    label_cha_val.grid(row=6, column=2)
    label_rest_val.grid(row=8, column=2)


def remember():
    global remember_throw
    global last_sum
    global last_rest
    remember_throw = val.copy()
    print(remember_throw)
    last_sum = sum
    print(last_sum)
    last_rest = rest
    print(rest)


def load():
    val = remember_throw.copy()
    sum = last_sum
    rest = last_rest

    label_str_val = Label(root, text=val[0])
    label_dex_val = Label(root, text=val[1])
    label_con_val = Label(root, text=val[2])
    label_int_val = Label(root, text=val[3])
    label_wis_val = Label(root, text=val[4])
    label_cha_val = Label(root, text=val[5])
    label_sum_val = Label(root, text=sum)
    label_rest_val = Label(root, text=rest)
    label_str_val.grid(row=1, column=2)
    label_dex_val.grid(row=2, column=2)
    label_con_val.grid(row=3, column=2)
    label_int_val.grid(row=4, column=2)
    label_wis_val.grid(row=5, column=2)
    label_cha_val.grid(row=6, column=2)
    label_sum_val.grid(row=7, column=2)
    label_rest_val.grid(row=8, column=2)


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
label_rest.grid(row=8, column=0)
label_rest_val.grid(row=8, column=2)

# Buttons
sub_str = Button(root, text='-', command=lambda: sub(0), width=3)
add_str = Button(root, text='+', command=lambda: add(0), width=3)
sub_dex = Button(root, text='-', command=lambda: sub(1), width=3)
add_dex = Button(root, text='+', command=lambda: add(1), width=3)
sub_con = Button(root, text='-', command=lambda: sub(2), width=3)
add_con = Button(root, text='+', command=lambda: add(2), width=3)
sub_int = Button(root, text='-', command=lambda: sub(3), width=3)
add_int = Button(root, text='+', command=lambda: add(3), width=3)
sub_wis = Button(root, text='-', command=lambda: sub(4), width=3)
add_wis = Button(root, text='+', command=lambda: add(4), width=3)
sub_cha = Button(root, text='-', command=lambda: sub(5), width=3)
add_cha = Button(root, text='+', command=lambda: add(5), width=3)

losuj_btn = Button(root, text='Losuj', command=losuj)

remember_btn = Button(root, text='Zapamiętaj', command=remember)
load_btn = Button(root, text='Wczytaj', command=load)

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
losuj_btn.grid(row=9, columnspan=4, sticky=W + E)
remember_btn.grid(row=10, column=0, columnspan=2, sticky=W+E)
load_btn.grid(row=10, column=2, columnspan=2, sticky=W+E)


# Mainloop
root.mainloop()