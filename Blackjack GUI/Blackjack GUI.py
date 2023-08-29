import random
from tkinter import *
from tkinter import messagebox

cards=["sinek-As.PNG","sinek-2.PNG","sinek-3.PNG","sinek-4.PNG","sinek-5.PNG","sinek-6.PNG","sinek-7.PNG","sinek-8.PNG","sinek-9.PNG","sinek-10.PNG",
       "sinek-J.PNG","sinek-K.PNG","sinek-Q.PNG"]
card=random.choice(cards)
cards_back="back.png"

window=Tk()
window.title("Blackjack GUI")
window.configure(bg="green")

money=100

def on_entry_click(event):
    if entry_bet.get() == "Enter Bet":
        entry_bet.delete(0, END)
        entry_bet.config(fg='black')

def on_enter(event):
    global money
    entered_bet = entry_bet.get()
    if entered_bet.isdigit():
        if int(entered_bet)<=money:
            new_money=money-int(entered_bet)
            money=new_money
            label_money.config(text=f"Money: ${new_money}")
            print("Onaylandı:", entered_bet)
        else:
            messagebox.showerror(title="Logic Error",message="Please Do Not Bet More Than Money.")
    else:
        messagebox.showerror(title="Value Error",message="Please Enter Digit")

label_money=Label(text=f"Money: ${money}",bg="green",font="bold 20",padx=20,pady=20)
label_money.grid(column=0,row=0)

label_bet=Label(text="Bet: $",bg="green",font="bold 20",padx=20,pady=20)
label_bet.grid(column=2,row=0)

entry_bet=Entry(width=8,font="bold 10")
entry_bet.insert(END,"Enter Bet")
entry_bet.place(x=490,y=27)
entry_bet.bind("<FocusIn>", on_entry_click)
entry_bet.bind("<Return>", on_enter)

label_your_card=Label(text="Your Cards",bg="green",font="Courier 20 bold",padx=20,pady=20)
label_your_card.grid(column=0,row=1)

label_your_dealer=Label(text="Your Dealer",bg="green",font="Courier 20 bold",padx=20,pady=20)
label_your_dealer.grid(column=2,row=1)

canvas_player=Canvas(width=300,height=300,bg="green",highlightthickness=0)
photo1=PhotoImage(file=card)
canvas_player.create_image(150,150,image=photo1)
canvas_player.grid(column=0,row=2)

canvas_dealer=Canvas(width=300,height=300,bg="green",highlightthickness=0)
photo2=PhotoImage(file=cards_back)
canvas_dealer.create_image(150,150,image=photo2)
canvas_dealer.grid(column=2,row=2)

button_hit=Button(text="HIT",padx=10,pady=10)
button_hit.grid(column=0,row=3)

button_stay=Button(text="STAY",padx=10,pady=10)
button_stay.grid(column=2,row=3)


window.mainloop()