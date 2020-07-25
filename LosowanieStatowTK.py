from tkinter import *
from random import randint

# tkinter window
root = Tk()
root.title('Losowanie Statystyk')
root.geometry('250x300')

# lists
attributes_list = ["Siła", "Zręczność", "Kondycja", "Inteligencja", "Mądrość", "Charyzma"]
btn_list = ["+", '-', "Losuj!", "Zapamiętaj", "Wczytaj"]

# starting values
attributes_values_list = [0, 0, 0, 0, 0, 0]
remember_throw = []
sum = 0
rest = 0


# Labels - def
def attributes_labels():
    Label(root, text='Twoje Statystyki').grid(row=0, columnspan=4)
    for i in range(6):
        Label(root, text=attributes_list[i], width=15).grid(row=i+1, column=0)
    Label(root, text='Suma:').grid(row=7, column=0)
    Label(root, text='Pozostało:').grid(row=8, column=0)


# Values - def
def attributes_values():
    for i in range(6):
        Label(root, text=attributes_values_list[i], width=10).grid(row=i+1, column=2)
    Label(root, text=sum).grid(row=7, column=2)
    Label(root, text=rest).grid(row=8, column=2)


def add(x):
    global rest
    global attributes_values_list
    if 18 > attributes_values_list[x] and rest > 0:
        attributes_values_list[x] = attributes_values_list[x] + 1
        rest = rest - 1

    attributes_labels()
    attributes_values()


def sub(x):
    global rest
    global attributes_values_list
    if attributes_values_list[x] > 3 and rest >= 0:
        attributes_values_list[x] = attributes_values_list[x] - 1
        rest = rest + 1

    attributes_labels()
    attributes_values()


def buttons():
    ### lambda z jakiegos powodu zapamiętuje ostatnią wartość 'i' i odnosi ją do wszystkich guzików - do poprawy
    for i in range(6):
        Button(root, text=btn_list[1], command=lambda: sub(i), width=3).grid(row=i+1, column=1)
        Button(root, text=btn_list[0], command=lambda: add(i), width=3).grid(row=i+1, column=3)
    Button(root, text=btn_list[2], command=losuj).grid(row=9, columnspan=4, sticky=W + E)
    Button(root, text=btn_list[3], command=remember).grid(row=10, column=0, columnspan=2, sticky=W + E)
    Button(root, text=btn_list[4], command=load).grid(row=10, column=2, columnspan=2, sticky=W + E)


def losuj():
    global rest
    global sum
    global attributes_values_list
    rest = 0
    sum = 0
    while sum < 65:
        sum = 0
        for i in range(6):
            value = randint(1,6) + randint(1,6) + randint(1,6)
            attributes_values_list[i] = value
            sum = sum + value

    attributes_values()


def remember():
    global remember_throw
    global last_sum
    global last_rest
    remember_throw = attributes_values_list.copy()
    last_sum = sum
    last_rest = rest


def load():
    global attributes_values_list
    global rest
    global sum
    attributes_values_list = remember_throw.copy()
    sum = last_sum
    rest = last_rest

    attributes_labels()
    attributes_values()


# Labele
attributes_labels()
attributes_values()

# Buttons
buttons()

# Mainloop
root.mainloop()