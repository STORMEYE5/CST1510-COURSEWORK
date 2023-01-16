import socket
import tkinter as tk
from tkinter import *
import threading
import mysql.connector
import sys
import pickle
from tkinter import messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='CST1510_DATABASE'
)

mycursor = mydb.cursor(buffered=True)

HOST = "127.0.0.1"
PORT = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

FORMAT = "utf-8"


class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        self.login = Toplevel()
        self.login.title("Credentials")
        self.login.resizable(width=False,
                             height=False)
        self.login.configure(width=400,
                             height=300)

        self.pls = Label(self.login,
                         text="Please enter credentials",
                         justify=CENTER,
                         font="Helvetica 14 bold")

        self.pls.place(relheight=0.15,
                       relx=0.2,
                       rely=0.07)
        self.labelName = Label(self.login,
                               text="Name: ",
                               font="Helvetica 12")

        self.labelName.place(relheight=0.2,
                             relx=0.1,
                             rely=0.2)

        self.entryName = Entry(self.login,
                               font="Helvetica 14")

        self.entryName.place(relwidth=0.4,
                             relheight=0.12,
                             relx=0.47,
                             rely=0.24)

        self.labelPassword = Label(self.login,
                                   text="Password: ",
                                   font="Helvetica 12")

        self.labelPassword.place(relheight=0.2,
                                 relx=0.1,
                                 rely=0.4)

        self.entryPassword = Entry(self.login, show="*",
                                   font="Helvetica 14")

        self.entryPassword.place(relwidth=0.4,
                                 relheight=0.12,
                                 relx=0.47,
                                 rely=0.44)

        self.labelName2 = Label(self.login,
                                   text="Customer Name: ",
                                   font="Helvetica 12")

        self.labelName2.place(relheight=0.2,
                                 relx=0.1,
                                 rely=0.6)

        self.entryName2 = Entry(self.login,
                                   font="Helvetica 14")

        self.entryName2.place(relwidth=0.4,
                                 relheight=0.12,
                                 relx=0.47,
                                 rely=0.64)

        self.entryName.focus()
        self.entryPassword.focus()
        self.entryName2.focus()

        self.go = Button(self.login,
                         text="Continue",
                         font="Helvetica 14 bold",
                         command=lambda: self.store(self.entryName.get(), self.entryPassword.get(), self.entryName2.get()))

        self.go.place(relx=0.4,
                      rely=0.8)

        self.Window.mainloop()

    def store(self, name, password, customer_name):
        mycursor.execute("SELECT * FROM employees")
        self.results = mycursor.fetchall()
        z = 0

        for row in self.results:
            z += 1
            if name == "" or password == "" or customer_name == "":
                tk.messagebox.showwarning(title="WARNING", message="ENTRY SHOULD NOT BE LEFT EMPTY")
                break

            if name == row[0] and password == row[1] and customer_name != "":
                self.login.destroy()
                self.layout(name, customer_name)
                break
            elif name != row[0] or password != row[1]:
                if z == len(self.results):
                    tk.messagebox.showerror(title="ERROR", message="INVALID CREDENTIALS")
                    self.entryPassword.delete(0, END)
                    break
                continue
            continue

    def layout(self, name, customer_name):
        self.name = name
        self.name2 = customer_name
        self.Window.deiconify()
        self.Window.title("STORE")
        self.Window.resizable(width=True,
                              height=True)
        self.Window.configure(width=800, height=800, bg="white")
        self.labelHead = Label(self.Window,
                               bg="white",
                               text=f'SHOPKEEPER: {self.name}',
                               font="Helvetica 13 bold",
                               pady=5)
        self.labelHead.place(relwidth=0.4)
        self.labelHead2 = Label(self.Window,
                               bg="white",
                               text=f'CUSTOMER: {self.name2}',
                               font="Helvetica 13 bold",
                               pady=5)
        self.labelHead2.place(rely=0.04, relwidth=0.4)

        self.motor_list = ["2L-T", "2JZ", "3L", "5L", "3S", "3M"]

        self.label1 = Label(self.Window,
                            bg="white",
                            text="ENGINES",
                            font="Helvetica 10 bold",
                            pady=5)
        self.label1.place(rely=0.08, relwidth=0.4)

        self.motor_list = ["2L-T", "2JZ", "3L", "5L", "3S", "3M"]

        self.label1 = Label(self.Window, text="ENGINES")

        dist_y = 100
        self.entries_motors = []

        for mo in range(len(self.motor_list)):
            self.label2 = Label(self.Window, text=self.motor_list[mo])
            self.label2.place(x=80, y=dist_y)
            self.entry2 = Entry(self.Window, width=6)
            self.entry2.place(x=200, y=dist_y)
            self.entries_motors.append(self.entry2)

            dist_y += 40

        IMAGE_PATH = '2jz.png'
        img = Image.open(IMAGE_PATH)
        img = ImageTk.PhotoImage(img)
        lbl = tk.Label(self.Window, image=img)
        lbl.img = img
        lbl.place(x=300, y=20)

        IMAGE_PATH = '3s_ge_engine.png'
        img = Image.open(IMAGE_PATH)
        img = ImageTk.PhotoImage(img)
        lbl = tk.Label(self.Window, image=img)
        lbl.img = img
        lbl.place(x=400, y=250)

        self.buttonMsg = Button(self.Window,
                                text="Save",
                                font="Helvetica 10 bold",
                                width=20,
                                bg="#ABB2B9",
                                command=self.loop)

        self.buttonMsg.place(x=70,
                             y=700,
                             relheight=0.06,
                             relwidth=0.22)

        self.buttonMsg2 = Button(self.Window,
                                 text="Bill",
                                 font="Helvetica 10 bold",
                                 width=20,
                                 bg="#ABB2B9",
                                 command=self.bill)

        self.buttonMsg2.place(x=70,
                              y=750,
                              relheight=0.06,
                              relwidth=0.22)

        self.exit = Button(self.Window, text="EXIT PROGRAM", command=self.exit_program)
        self.exit.place(relx=0.88, rely=0.963)

    def loop(self):
        self.data_send = []
        for i in self.entries_motors:
            if i.get() == "":
                self.data_send.append(0)
            else:
                self.data_send.append(i.get())
        self.var1 = pickle.dumps(self.data_send)

        for j in range(len(self.motor_list)):
            mycursor.execute("""SELECT quantity FROM stock WHERE product_name = '%s' """ % (self.motor_list[j]))
            result = mycursor.fetchone()
            quantity = result[0]

            if int(self.data_send[j]) > quantity:
                tk.messagebox.showwarning(title="WARNING", message=f"VALUE REQUESTED HIGHER THAN STOCK\nMAXIMUM: {quantity}")
                break
            else:
                self.sendButton()

        for i in self.entries_motors:
            i.delete(0, END)

    def sendButton(self):
        self.msg = ""
        self.msg = self.var1
        snd = threading.Thread(target=self.message2)
        snd.start()

    def message2(self):
        while True:
            try:
                self.message_send = self.msg
                self.encoded_str = self.message_send
                s.send(self.encoded_str)
            except:
                s.close()

    def exit_program(self):
        sys.exit()

    def bill(self):
        self.bill_window = Tk()
        self.Window.withdraw()
        self.bill_window.configure(height=500, width=300)

        self.bill_window.title("RECEIPT")

        self.bill_labelhead = Label(self.bill_window, text="\t\tTOYOTA ENGINES")
        self.bill_labelhead.place(x=10, y=10)

        self.bill_labelhead2 = Label(self.bill_window, text="\t\t   ROYAL RD")
        self.bill_labelhead2.place(x=22, y=30)

        self.bill_labelhead3 = Label(self.bill_window, text="\t\t TEL: 4250297")
        self.bill_labelhead3.place(x=22, y=50)

        self.t = []
        for n in range(len(self.motor_list)):
            if self.entries_motors[n].get() == "":
                self.t.append(0)
            else:
                mycursor.execute("""SELECT price FROM stock WHERE product_name = '%s' """ % (self.motor_list[n]))
                result = mycursor.fetchone()
                price = result[0]

                self.t.append(eval(self.entries_motors[n].get()) * price)

        val_y = 100

        for bill_loop in range(len(self.motor_list)):
            if self.t[bill_loop] == 0:
                continue
            self.label_b1 = Label(self.bill_window, text=self.motor_list[bill_loop])
            self.label_b1.place(x=20, y=val_y)
            self.label_b2 = Label(self.bill_window, text=self.entries_motors[bill_loop].get())
            self.label_b2.place(x=180, y=val_y)
            self.label_b3 = Label(self.bill_window, text=self.t[bill_loop])
            self.label_b3.place(x=240, y=val_y)

            val_y += 20

        self.label_b4 = Label(self.bill_window, text="TOTAL:")
        self.label_b4.place(x=160, y=400)

        self.label_b5 = Label(self.bill_window, text=sum(self.t))
        self.label_b5.place(x=240, y=400)

        self.label_b6 = Label(self.bill_window, text="PRODUCT\t\t QTY\t       PRICE")
        self.label_b6.place(x=20, y=75)

        self.order = Button(self.bill_window, text="ORDER", command=self.loop)
        self.order.place(relx=0.50, rely=0.94)

        self.cancel = Button(self.bill_window, text="CANCEL ORDER", command=self.exit_program)
        self.cancel.place(relx=0.67, rely=0.94)


g = GUI()