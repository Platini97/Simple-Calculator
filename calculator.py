# Kalkulator

from tkinter import *
import datetime

class Application(Frame):
    liczba1 = 0
    liczba2 = 0
    now = datetime.datetime.now()
    """Kalkulator GUI"""


    def __init__(self, master):
        """Tworzy ramkę"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        now = datetime.datetime.now()

    # metoda z widżetami
    def create_widgets(self):
        """Metoda z widżetami"""
        # label liczba 1
        self.label = Label(self, text="Number 1: ")
        self.label.grid(row=1, column=0, sticky=W)
        # entry liczba 1
        self.liczba1_ent = Entry(self)
        self.liczba1_ent.grid(row=1, column=1, sticky=W)
        # label liczba 2
        self.label_2 = Label(self, text="Number 2: ")
        self.label_2.grid(row=3, column=0, sticky=W)
        # entry liczba 2
        self.liczba2_ent = Entry(self)
        self.liczba2_ent.grid(row=3, column=1, sticky=W)
        # label znak matematyczny
        self.label_znak = Label(self, text="Char(+,-,*,/): ")
        self.label_znak.grid(row=5, column=0, sticky=W)
        # entry znak matematyczny
        self.znak_ent = Entry(self)
        self.znak_ent.grid(row=5, column=1, sticky=W)
        # button znak matematyczny
        self.submit_znak = Button(self, text="Calculate", command=self.znak)  # wstawić command
        self.submit_znak.grid(row=5, column=2, sticky=W)
        # label wynik
        self.label = Label(self, text="Equal: ")
        self.label.grid(row=7, column=0, sticky=W)
        # text wynik
        self.wynik_txt = Text(self, width=15, height=1, wrap=WORD)
        self.wynik_txt.grid(row=7, column=1, sticky=W)
        #data i godzina
        self.data_txt = Text(self, width = 15, height = 1, wrap = WORD)
        self.data_txt.grid(row=8,column = 1, sticky = W)

        self.wynik_txt.delete(0.0, END)
        self.data_txt.insert(0.0, self.now)

    def znak(self):
        """Przekazuje znak"""
        x = float(self.liczba1_ent.get())
        y = float(self.liczba2_ent.get())
        contents = self.znak_ent.get()

        if contents == "+":
            wynik = x + y
        elif contents == "-":
            wynik = x - y
        elif contents == "*":
            wynik = x * y
        elif contents == "/":
            wynik = x / y

        self.wynik_txt.delete(0.0, END)
        self.wynik_txt.insert(0.0, wynik)


# część główna
root = Tk()
root.title("Calculator")
root.geometry("310x150")
app = Application(root)
root.mainloop()

