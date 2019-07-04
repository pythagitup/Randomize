from tkinter import *
from random import shuffle
import tkinter.font

root = Tk()
root.title('Random Group Generator')

#Make fonts bigger, group font for group headings
default_font = tkinter.font.nametofont("TkDefaultFont")
default_font.configure(size=24)
group_font = tkinter.font.nametofont("TkHeadingFont")
group_font.configure(size=24, weight='bold')

#Starting values
blanklist = ['', '', '', '', '']
blankstr = '\n'.join(blanklist)
group1 = StringVar()
group2 = StringVar()
group3 = StringVar()
group4 = StringVar()
group5 = StringVar()
group6 = StringVar()
group1.set(blankstr)
group2.set(blankstr)
group3.set(blankstr)
group4.set(blankstr)
group5.set(blankstr)
group6.set(blankstr)

grplst1 = []
grplst2 = []
grplst3 = []
grplst4 = []
grplst5 = []
grplst6 = []

#Load class period
def load():
    with open('Period' + period.get() + '.txt', 'r') as roster:
        stuff = roster.read().splitlines()
        split(stuff)
        a = '\n'.join(grplst1)
        b = '\n'.join(grplst2)
        c = '\n'.join(grplst3)
        d = '\n'.join(grplst4)
        e = '\n'.join(grplst5)
        f = '\n'.join(grplst6)
        group1.set(a)
        group2.set(b)
        group3.set(c)
        group4.set(d)
        group5.set(e)
        group6.set(f)
               
#Split class into groups
def split(thing):
    grplst1.clear()
    grplst2.clear()
    grplst3.clear()
    grplst4.clear()
    grplst5.clear()
    grplst6.clear()
    groups = {0: grplst1, 1: grplst2, 2: grplst3, 3: grplst4, 4: grplst5, 5: grplst6}
    for i in range(len(thing)):
        rem = i%6
        groups[rem].append(thing[i])

#Randomize function
def randomize():
    stuff = grplst1 + grplst2 + grplst3 + grplst4 + grplst5 + grplst6
    shuffle(stuff)
    split(stuff)
    a = '\n'.join(grplst1)
    b = '\n'.join(grplst2)
    c = '\n'.join(grplst3)
    d = '\n'.join(grplst4)
    e = '\n'.join(grplst5)
    f = '\n'.join(grplst6)
    group1.set(a)
    group2.set(b)
    group3.set(c)
    group4.set(d)
    group5.set(e)
    group6.set(f)

#Create frame for options/button
topframe = Frame(root)
topframe.grid(row=0, columnspan=3)

#Selection for class period
period = StringVar()
p2 = Radiobutton(topframe, text='2nd', indicatoron=0, variable=period, value='2', command=load)
p3 = Radiobutton(topframe, text='3rd', indicatoron=0, variable=period, value='3', command=load)
p4 = Radiobutton(topframe, text='4th', indicatoron=0, variable=period, value='4', command=load)
p5 = Radiobutton(topframe, text='5th', indicatoron=0, variable=period, value='5', command=load)

p2.pack(side=LEFT, padx=10)
p3.pack(side=LEFT, padx=10)
p4.pack(side=LEFT, padx=10)
p5.pack(side=LEFT, padx=10)

#Create frames for each group
frame1 = Frame(root, bg='#f4cccc')
frame2 = Frame(root, bg='#c9daf8')
frame3 = Frame(root, bg='#fce5cd')
frame4 = Frame(root, bg='#d9ead3')
frame5 = Frame(root, bg='#fff2cc')
frame6 = Frame(root, bg='#d9d2e9')

frame1.grid(row=1, column=0, sticky=NS)
frame2.grid(row=1, column=1, sticky=NS)
frame3.grid(row=1, column=2, sticky=NS)
frame4.grid(row=3, column=0, pady=10, sticky=NS)
frame5.grid(row=3, column=1, pady=10, sticky=NS)
frame6.grid(row=3, column=2, pady=10, sticky=NS)

#Create label for each group
grp1 = Label(frame1, text='Group 1', font='TkHeadingFont', bg='#f4cccc')
grp1.pack()
grp2 = Label(frame2, text='Group 2', font='TkHeadingFont', bg='#c9daf8')
grp2.pack()
grp3 = Label(frame3, text='Group 3', font='TkHeadingFont', bg='#fce5cd')
grp3.pack()
grp4 = Label(frame4, text='Group 4', font='TkHeadingFont', bg='#d9ead3')
grp4.pack()
grp5 = Label(frame5, text='Group 5', font='TkHeadingFont', bg='#fff2cc')
grp5.pack()
grp6 = Label(frame6, text='Group 6', font='TkHeadingFont', bg='#d9d2e9')
grp6.pack()

#Label with members of each group
members1 = Label(frame1, textvariable=group1, bg='#f4cccc')
members1.pack()
members2 = Label(frame2, textvariable=group2, bg='#c9daf8')
members2.pack()
members3 = Label(frame3, textvariable=group3, bg='#fce5cd')
members3.pack()
members4 = Label(frame4, textvariable=group4, bg='#d9ead3')
members4.pack()
members5 = Label(frame5, textvariable=group5, bg='#fff2cc')
members5.pack()
members6 = Label(frame6, textvariable=group6, bg='#d9d2e9')
members6.pack()

#Button to call randomize function
randbutt = Button(topframe, text='Randomize!', command=randomize)
randbutt.pack(side=RIGHT, padx=10, pady=10)

root.mainloop()