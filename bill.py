# Billing app with python

from tkinter import*

class Bill_App:
    def __init__ (self, root):
        self.root= root
        self.root.geometry("1350x700+0+0")
        self.root.title("customer invoice")  # self.root.img("T:\\Education & work\\Education\\python\\billing app")
        bg_color="#000000"
        title= Label(self.root, text="TEHZIB", bd=12, bg= bg_color, relief=GROOVE, fg="red",  font= ("times new roman", 30, "bold"), pady=2 ).pack(fill=X)

        # ________customer details
        F1=LabelFrame(self.root, bd=10, text= "Customer details", bg=bg_color, font=("times new roman", 20, "bold"), fg="red")
        F1.place(x=0, y=80, relwidth=1)

        cn_lbl= Label(F1, text= "Name", fg="cyan", bg=bg_color, font=("times new roman", 18, "bold" )).grid(row=0, column=0, padx=2, pady=20)
        cn_txt= Entry(F1, width=70, font="calibre 15", bd=7).grid(row=0, column=1, pady=20, padx=0)

        cc_lbl = Label(F1, text="Contact no", fg="cyan", bg=bg_color, font=("times new roman", 18, "bold")).grid( row=0, column=2, padx=0, pady=20)
        cc_txt = Entry(F1, width=30, font="calibre 15", bd=7).grid(row=0, column=3, pady=20, padx=0)

        co_lbl = Label(F1, text="Order no", fg="cyan", bg=bg_color, font=("times new roman", 18, "bold")).grid(row=0,column=4, padx=0 ,pady=20)
        co_txt = Entry(F1, width=30, font="calibre 15", bd=7).grid(row=0, column=5, pady=20, padx=0)

        cd_lbl = Label(F1, text="Date", fg="cyan", bg=bg_color, font=("times new roman", 18, "bold")).grid(row=1, column=2,padx=0,pady=20)
        cd_txt = Entry(F1, width=30, font="calibre 15", bd=7).grid(row=1, column=3, pady=20, padx=0)

        ca_lbl = Label(F1, text="Address", fg="cyan", bg=bg_color, font=("times new roman", 18, "bold")).grid(row=1,column=0,padx=2,pady=20)
        ca_txt = Entry(F1, width=70, font="calibre 15", bd=7).grid(row=1, column=1, pady=20, padx=0)

        bill_btn = Button(F1, text="Confirm", width=10, bd=7, font=("times new roman", 18, "bold")).grid(row=1,column=5, padx=0, pady=20)




root= Tk()
obj = Bill_App(root)
root.mainloop()