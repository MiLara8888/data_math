from tkinter import *
from datetime import *


def func():
    m = int(enmo.get())
    y = int(enyear.get())
    d = int(enday.get())
    t = entime.get()
    if ':' in t:
        t = t.split(':')
    else:
        t = t.split(' ')
    n = datetime.today().strftime("%Y-%m-%d %H:%M")
    n = datetime.now()
    k = datetime(y, m, d, int(t[0]), int(t[1]))
    res = k - n

    min = str(res).split(':')
    if min[0][0] == '-':
        result['text'] = 'Важное событие \nуже завершилось...'
    else:
        result['text'] = f"До важного события осталось: \n {res.days}-Д : {int((res.seconds) // 3600)}-Ч : {min[1]} : М"


root = Tk()
root.geometry('445x350+750+80')
root["bg"] = "#A4E8CD"
root.title('Вычисление времени до важного события')
result = Label(root, text='', font='arial 20', bg='#A4E8CD', fg='#205A43')
mo = Label(root, text='Введите месяц:', font='arial 16', bg='#BFEEDB', fg='#205A43')
year = Label(root, text='Введите год:', font='arial 16', bg='#BFEEDB', fg='#205A43')
day = Label(root, text='Введите день:', font='arial 16', bg='#BFEEDB', fg='#205A43')
time = Label(root, text='Введите время:', font='arial 16', bg='#BFEEDB', fg='#205A43')
entime = Entry(root, borderwidth='5', width='6', bg='#D8F6EA', font='arial 17', fg='#205A43')
enday = Entry(root, borderwidth='5', width='6', bg='#D8F6EA', font='arial 17', fg='#205A43')
enmo = Entry(root, borderwidth='5', width='6', bg='#D8F6EA', font='arial 17', fg='#205A43')
enyear = Entry(root, borderwidth='5', width='6', bg='#D8F6EA', font='arial 17', fg='#205A43')
head = Label(root, text='Вычисляем остаток времени до важного события', font='arial 14', bg='#2AC185', fg='#1F4636')
but = Button(root, text='ВПЕРЁД!', bg='#1A3C2E', fg='#00FF9A', font='arial 14', height=2, width=25, command=func)

but.grid(column=1, row=6, columnspan=3)
head.grid(column=1, row=1, columnspan=3)
result.grid(column=1, row=7, columnspan=3, rowspan=3)

enyear.grid(column=2, row=2)
year.grid(column=1, row=2, padx=5, pady=5)
mo.grid(column=1, row=3, padx=5, pady=5)
enmo.grid(column=2, row=3)
day.grid(column=1, row=4, padx=5, pady=5)
enday.grid(column=2, row=4)
time.grid(column=1, row=5, padx=5, pady=5)
entime.grid(column=2, row=5)

root.mainloop()
