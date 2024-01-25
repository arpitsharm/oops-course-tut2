import tkinter as tk
from tkinter import messagebox
import random


class Application:
    def __init__(self, runed) -> None:
                
        window  = runed
        window.title("TUT")
        window.resizable(False, False)
        window.configure(background="Black", border="2", relief="groove")
        window.geometry("700x550+50+20")
        '''
        geomectry rules

        Rule No.1 - all thing on a '' or ""
        Rule No.2 - width height yes --error width , height X
        Rule No.3 - height width yes --error height , width X
        Rule No.4 - Simmilarly x+y mean possitions = p1+p2

        '''


        # Button, Labels, Entry # tkinter
        # Button, Labels, Entry advance beaty # tkinter.ttk



        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.StringVar()
        self.var5 = tk.StringVar()

        a = random.randint(0, 1000000000)
        b = str(a)


        def genrate():
            if self.var1.get() == ""  or self.var2.get() == ""  or self.var3.get() == ""  or self.var4.get() == ""  or self.var5.get() == "":
                messagebox.showerror("Project 1", "All Fields Are Requierd")

            else:
                with open(f"{b[0:2] + self.var1.get()}", "w") as f:
                    f.write(f"Your ID :- {b}\n")
                    f.write(f"Your Name :- {self.var1.get()}\n")
                    f.write(f"Your Email :- {self.var2.get()}\n")
                    f.write(f"Your Gender :- {self.var3.get()}\n")
                    f.write(f"Your Phone No. :- {self.var4.get()}\n")
                    f.write(f"Your Amount :- {self.var5.get()}\n")

                messagebox.showinfo("Project 1", "Sussfully Slip Create!!!")




        title = tk.Label(master = window, text = "Project 1", background="Blue", foreground="black", font=("calibri", 30), bd=10, relief="raised")
        title.pack(fill = "x")


        lbl1 = tk.Label(master = window, text = "Your ID : ", background="black", foreground="white", font=("times new roman", 14))
        lbl1.place(x=10, y=100)
        # lbl1.pack(padx=10, pady=10)
        idlabel = tk.Label(master = window, text = f"{a}", background="black", foreground="white", font=("times new roman", 14))
        idlabel.place(x=180, y=100)

        lbl2 = tk.Label(master = window, text = "Your Name : ", background="black", foreground="white", font=("times new roman", 14))
        lbl2.place(x=10, y=150)
        f2 = tk.Entry(window, textvariable=self.var1)
        f2.place(x=180, y=155)

        lbl3 = tk.Label(master = window, text = "Your Email : ", background="black", foreground="white", font=("times new roman", 14))
        lbl3.place(x=10, y=200)
        f3 = tk.Entry(window, textvariable=self.var2)
        f3.place(x=180, y=205)

        lbl4 = tk.Label(master = window, text = "Your Gender : ", background="black", foreground="white", font=("times new roman", 14))
        lbl4.place(x=10, y=250)
        f4 = tk.Entry(window, textvariable=self.var3)
        f4.place(x=180, y=255)

        lbl5 = tk.Label(master = window, text = "Your Phone No. : ", background="black", foreground="white", font=("times new roman", 14))
        lbl5.place(x=10, y=300)
        f5 = tk.Entry(window, textvariable=self.var4)
        f5.place(x=180, y=305)

        lbl6 = tk.Label(master = window, text = "Your Amout : ", background="black", foreground="white", font=("times new roman", 14))
        lbl6.place(x=10, y=350)
        f6 = tk.Entry(window, textvariable=self.var5)
        f6.place(x=180, y=355)



        btn1 = tk.Button(window, text="Genrate Slip", command=genrate)
        btn1.place(x=80, y=400)









        window.mainloop()


obj = Application(tk.Tk())
