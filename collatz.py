from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def pruefen():
    if number.get() < 1:
        messagebox.showwarning(message="Bitte eine Zahl größer als 1 eingeben!", title="Warnung!")
    else:
        rechnen()
        

def rechnen():
    count.set(0)
    zahlen.set("")
    while number.get() > 1:
        count.set(count.get()+1)
        zahlen.set(zahlen.get()+str(number.get())+", ")
        if number.get()%2==0:
            number.set(number.get()//2)
        else:
            number.set(number.get()*3+1)
    else:
        zahlen.set(zahlen.get()+"1")
        result = Toplevel()
        result.title("Durchlaeufe")
        result.geometry("-490+380")
        result_l1 = ttk.Label(result, text="Durchlaeufe: ").grid(row=0, column=0, sticky=E)
        result_l2 = ttk.Label(result, textvariable=count).grid(row=0, column=1, sticky=W)
        result_l3 = ttk.Label(result, text="Zahlen: ").grid(row=1, column=0, sticky=E)
        result_l4 = ttk.Label(result, textvariable=zahlen).grid(row=1, column=1, sticky=W)


root = Tk()
root.title("Collatz")
root.geometry("280x50-490+300")

number=IntVar()
count=IntVar()
zahlen=StringVar()

number_entry = ttk.Entry(root, textvariable=number)
number_entry.focus()
number_entry.grid(row=0, column=1, sticky=W)
number_label = ttk.Label(root, text="Zahl eingeben: ")
number_label.grid(row=0, column=0, sticky=W)
number_button = ttk.Button(root, text="Ok!", command=pruefen)
number_button.grid(row=2, column=1, sticky=E)



root.mainloop()

