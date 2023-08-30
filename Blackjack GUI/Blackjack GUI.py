import random
from tkinter import *
from tkinter import messagebox

cards=["sinek-As.PNG","sinek-2.PNG","sinek-3.PNG","sinek-4.PNG","sinek-5.PNG","sinek-6.PNG","sinek-7.PNG","sinek-8.PNG","sinek-9.PNG","sinek-10.PNG",
       "sinek-J.PNG","sinek-K.PNG","sinek-Q.PNG"]
card=random.choice(cards)
cards_back="back.png"
card_values = {
    "sinek-As.PNG": 11,
    "sinek-2.PNG": 2,
    "sinek-3.PNG": 3,
    "sinek-4.PNG": 4,
    "sinek-5.PNG": 5,
    "sinek-6.PNG": 6,
    "sinek-7.PNG": 7,
    "sinek-8.PNG": 8,
    "sinek-9.PNG": 9,
    "sinek-10.PNG": 10,
    "sinek-J.PNG": 10,
    "sinek-K.PNG": 10,
    "sinek-Q.PNG": 10,
}

window=Tk()
window.title("Blackjack GUI")
window.configure(bg="green")

money=100
player_cards = []
dealer_cards = []
player_total=0
dealer_total=0
current_bet = 0


def calculate_card_total(card_list):
    total = sum(card_values[card] for card in card_list)
    aces = card_list.count("sinek-As.PNG")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

player_card_images=[] 
player_card_x=20
def show_player_card(card_image):
    global player_card_x
    card_image=PhotoImage(file=card_image)
    player_card_images.append(card_image)
    canvas_player.create_image(player_card_x,150,image=card_image, anchor=W)
    player_card_x+=40

dealer_card_images=[] 
dealer_card_x=20
def show_dealer_card(card_image):
    global dealer_card_x
    card_image=PhotoImage(file=card_image)
    dealer_card_images.append(card_image)
    canvas_dealer.create_image(dealer_card_x,150,image=card_image, anchor=W)
    dealer_card_x+=40

def on_hit():
    global player_cards,player_total
    new_card=random.choice(cards)
    player_cards.append(new_card)
    show_player_card(new_card)
    player_total=calculate_card_total(player_cards)
    print("Player Total:",player_total)
    if player_total > 21:
        messagebox.showinfo(title="Game Over", message="Dealer wins! Player busts.")
        on_deal()

def on_stay():
    global dealer_cards,dealer_total
    while dealer_total<=16:
        new_card=random.choice(cards)
        dealer_cards.append(new_card)
        show_dealer_card(new_card)
        dealer_total=calculate_card_total(dealer_cards)
        print("dealer Total:",dealer_total)
    determine_winner()


def on_entry_click(event):
    if entry_bet.get()=="Enter Bet":
        entry_bet.delete(0,END)
        entry_bet.config(fg='black')

def on_enter(event):
    global money, current_bet
    entered_bet = entry_bet.get()
    if entered_bet.isdigit():
        entered_bet = int(entered_bet)
        if entered_bet <= money:
            current_bet = entered_bet
            new_money = money - entered_bet
            money = new_money
            label_money.config(text=f"Money: ${new_money}")
            label_bet.config(text=f"Bet: ${current_bet}")
            on_deal()
            button_hit.config(state=NORMAL)
            button_stay.config(state=NORMAL)
            button_deal.config(state=NORMAL)
        else:
            messagebox.showerror(title="Logic Error", message="Please Do Not Bet More Than Money.")
    else:
        messagebox.showerror(title="Value Error", message="Please Enter a Digit")

def reset_game():
    global player_cards, dealer_cards, player_card_images, dealer_card_images, player_card_x, dealer_card_x
    player_cards = []
    dealer_cards = []
    for image in player_card_images:
        canvas_player.delete(image)
    for image in dealer_card_images:
        canvas_dealer.delete(image)
    player_card_images = []
    dealer_card_images = []
    player_card_x = 20
    dealer_card_x = 20
    button_hit.config(state=DISABLED)
    button_stay.config(state=DISABLED)
    button_deal.config(state=DISABLED)

def on_deal():
    global player_cards, dealer_cards, player_total, dealer_total
    reset_game()
    player_cards = []
    dealer_cards = []
    if current_bet > 0:
        for _ in range(2):
            new_card = random.choice(cards)
            player_cards.append(new_card)
            show_player_card(new_card)
        new_card = random.choice(cards)
        dealer_cards.append(new_card)
        show_dealer_card(new_card)
        player_total = calculate_card_total(player_cards)
        dealer_total = calculate_card_total(dealer_cards)



label_money=Label(text=f"Money: ${money}",bg="green",font="bold 20",padx=20,pady=20)
label_money.grid(column=0,row=0)

label_bet=Label(text="Bet: $",bg="green",font="bold 20",padx=20,pady=20)
label_bet.grid(column=2,row=0)

label_enter=Label(text="Click The Enter",bg="green",font="bold 10")
label_enter.place(x=535,y=57)

entry_bet=Entry(width=8,font="bold 10")
entry_bet.insert(END,"Enter Bet")
entry_bet.place(x=470,y=57)
entry_bet.bind("<FocusIn>", on_entry_click)
entry_bet.bind("<Return>", on_enter)

label_your_card=Label(text="Your Cards",bg="green",font="Courier 20 bold",padx=20,pady=20)
label_your_card.grid(column=0,row=1)

label_your_dealer=Label(text="Your Dealer",bg="green",font="Courier 20 bold",padx=20,pady=20)
label_your_dealer.grid(column=2,row=1)

canvas_player = Canvas(width=300, height=300, bg="green", highlightthickness=0)
canvas_player.grid(column=0, row=2)

canvas_dealer = Canvas(width=300, height=300, bg="green", highlightthickness=0)
canvas_dealer.grid(column=2, row=2)

button_hit=Button(text="HIT",padx=10,pady=10,command=on_hit)
button_hit.grid(column=0,row=3)

button_stay=Button(text="STAY",padx=10,pady=10,command=on_stay)
button_stay.grid(column=2,row=3)

button_deal = Button(text="DEAL", padx=10, pady=10, command=on_deal)
button_deal.grid(column=1, row=3)

button_hit.config(state=DISABLED)
button_stay.config(state=DISABLED)
button_deal.config(state=DISABLED)

def determine_winner():
    global dealer_total, player_total, money, current_bet
    player_total = calculate_card_total(player_cards)
    dealer_total = calculate_card_total(dealer_cards)
    
    if dealer_total > 21:
        messagebox.showinfo(title="Game Over", message="Player wins! Dealer busts.")
        money += current_bet * 2
    elif player_total > 21:
        messagebox.showinfo(title="Game Over", message="Dealer wins! Player busts.")
    elif dealer_total > player_total:
        messagebox.showinfo(title="Game Over", message="Dealer wins!")
    elif player_total > dealer_total:
        messagebox.showinfo(title="Game Over", message="Player wins!")
        money += current_bet * 2
    else:
        messagebox.showinfo(title="Game Over", message="It's a tie!")
        money += current_bet
    current_bet = 0
    label_money.config(text=f"Money: ${money}")
    label_bet.config(text=f"Bet: ${current_bet}")
    on_deal()


window.mainloop()