from tkinter import*

window = Tk()
window.title("Auto Clicker")
window.geometry("400x300")
window.configure(bg = "#def6fa")

label1 = Label(window, text = "Auto Clicker", bg = "#def6fa", font = ("Arial 20 bold"),  fg = "#08827e")
label1.place(relx=0.5, rely=0.05, anchor="n")

label2 = Label(window, text = "Кліків на секунду:", bg = "#def6fa", font = ("Arial", 15),  fg = "#08827e")
label2.place(relx=0.5, rely=0.2, anchor="n")

clicks = Entry(window, width=40)
clicks.place(relx=0.5, rely=0.3, anchor="n")

def startbtn():
    print("Клацнуто кнопку 'Почати'.")

btn1 = Button(window, text = "Почати", command=startbtn, bg = "#4baf4f", fg = "white", font = ("Arial", 13), height=2, width=10)
btn1.place(relx=0.35, rely=0.42, anchor="n")

btn2 = Button(window, text = "Вийти", command=window.destroy, bg = "#f54035", fg = "white", font = ("Arial", 13), height=2, width=8)
btn2.place(relx=0.65, rely=0.42, anchor="n")
#4BAD4E
#f54035 Вийти

window.mainloop()