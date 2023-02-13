import random
from tkinter import *
from tkinter import messagebox

window1=Tk()
window1.title("MONEY")
window1.geometry("1000x1000")



sinek_As=PhotoImage(file="sinek-As.PNG")
sinek_2=PhotoImage(file="sinek-2.PNG")
sinek_3=PhotoImage(file="sinek-3.PNG")
sinek_4=PhotoImage(file="sinek-4.PNG")
sinek_5=PhotoImage(file="sinek-5.PNG")
sinek_6=PhotoImage(file="sinek-6.PNG")
sinek_7=PhotoImage(file="sinek-7.PNG")
sinek_8=PhotoImage(file="sinek-8.PNG")
sinek_9=PhotoImage(file="sinek-9.PNG")
sinek_10=PhotoImage(file="sinek-10.PNG")
sinek_J=PhotoImage(file="sinek-J.PNG")
sinek_Q=PhotoImage(file="sinek-Q.PNG")
sinek_K=PhotoImage(file="sinek-K.PNG")

abc=[sinek_As,sinek_2,sinek_3,sinek_4,sinek_5,sinek_6,sinek_7,sinek_8,sinek_9,sinek_10,sinek_J,sinek_Q,sinek_K]

def money():
    
    Frame(window1,height=1000,width=1000,bg="white").place(x=0,y=0)
    Label(window1,text=f"Your total money is {para.get()}$",font="times 15 bold",bg="white").place(x=600,y=10)
    def bet():
        if bahis.get()>para.get():
            messagebox.showwarning("Logic error!", "You cannot bet more than your money!")
    Button(window1,text="Enter your bet:",font="times 15 bold",width=12,command=bet,bg="white").place(x=20,y=10)
    bahis=Entry(window1,font="times 15 bold",relief=RAISED,width=15,bg="white")
    bahis.place(x=20,y=50)
    
    yourTotal=0
    dealerTotal=0

    you1=random.choice(abc)
    if you1==sinek_As:
        if yourTotal<=11:
            yourTotal+=11
        else:
            yourTotal+=1
    elif you1==sinek_K:
        yourTotal+=10
    elif you1==sinek_Q:
        yourTotal+=10
    elif you1==sinek_J:
        yourTotal+=10
    elif you1==sinek_10:
        yourTotal+=10
    elif you1==sinek_9:
        yourTotal+=9
    elif you1==sinek_8:
        yourTotal+=8
    elif you1==sinek_7:
        yourTotal+=7
    elif you1==sinek_6:
        yourTotal+=6
    elif you1==sinek_5:
        yourTotal+=5
    elif you1==sinek_4:
        yourTotal+=4
    elif you1==sinek_3:
        yourTotal+=3
    elif you1==sinek_2:
        yourTotal+=2
    Label(window1,image=you1,bg="white").place(x=100,y=400)

    you2=random.choice(abc)
    if you2==sinek_As:
        if yourTotal<=11:
            yourTotal+=11
        else:
            yourTotal+=1
    elif you2==sinek_K:
        yourTotal+=10
    elif you2==sinek_Q:
        yourTotal+=10
    elif you2==sinek_J:
        yourTotal+=10
    elif you2==sinek_10:
        yourTotal+=10
    elif you2==sinek_9:
        yourTotal+=9
    elif you2==sinek_8:
        yourTotal+=8
    elif you2==sinek_7:
        yourTotal+=7
    elif you2==sinek_6:
        yourTotal+=6
    elif you2==sinek_5:
        yourTotal+=5
    elif you2==sinek_4:
        yourTotal+=4
    elif you2==sinek_3:
        yourTotal+=3
    elif you2==sinek_2:
        yourTotal+=2
    Label(window1,image=you2,bg="white").place(x=150,y=400)
    
    if yourTotal<21:
        def hit1():
            nonlocal yourTotal
            x=random.choice(abc)
            if x==sinek_As:
                if yourTotal<=11:
                    yourTotal+=11
                else:
                    yourTotal+=1
            elif x==sinek_K:
                yourTotal+=10
            elif x==sinek_Q:
                yourTotal+=10
            elif x==sinek_J:
                yourTotal+=10
            elif x==sinek_10:
                yourTotal+=10
            elif x==sinek_9:
                yourTotal+=9
            elif x==sinek_8:
                yourTotal+=8
            elif x==sinek_7:
                yourTotal+=7
            elif x==sinek_6:
                yourTotal+=6
            elif x==sinek_5:
                yourTotal+=5
            elif x==sinek_4:
                yourTotal+=4
            elif x==sinek_3:
                yourTotal+=3
            elif x==sinek_2:
                yourTotal+=2
            Label(window1,image=x,bg="white").place(x=200,y=400)
            Label(window1,text="Your total is {}".format(yourTotal),bg="white",font="Times 15 bold").place(x=750,y=500)
            hit_1.destroy()
            if yourTotal<21:
                def hit2():
                    nonlocal yourTotal
                    x=random.choice(abc)
                    if x==sinek_As:
                        if yourTotal<=11:
                            yourTotal+=11
                        else:
                            yourTotal+=1
                    elif x==sinek_K:
                        yourTotal+=10
                    elif x==sinek_Q:
                        yourTotal+=10
                    elif x==sinek_J:
                        yourTotal+=10
                    elif x==sinek_10:
                        yourTotal+=10
                    elif x==sinek_9:
                        yourTotal+=9
                    elif x==sinek_8:
                        yourTotal+=8
                    elif x==sinek_7:
                        yourTotal+=7
                    elif x==sinek_6:
                        yourTotal+=6
                    elif x==sinek_5:
                        yourTotal+=5
                    elif x==sinek_4:
                        yourTotal+=4
                    elif x==sinek_3:
                        yourTotal+=3
                    elif x==sinek_2:
                        yourTotal+=2
                    Label(window1,image=x,bg="white").place(x=250,y=400)
                    Label(window1,text="Your total is {}".format(yourTotal),bg="white",font="Times 15 bold").place(x=750,y=500)
                    hit_2.destroy()
                    if yourTotal<21:
                        def hit3():
                            nonlocal yourTotal
                            x=random.choice(abc)
                            if x==sinek_As:
                                if yourTotal<=11:
                                    yourTotal+=11
                                else:
                                    yourTotal+=1
                            elif x==sinek_K:
                                yourTotal+=10
                            elif x==sinek_Q:
                                yourTotal+=10
                            elif x==sinek_J:
                                yourTotal+=10
                            elif x==sinek_10:
                                yourTotal+=10
                            elif x==sinek_9:
                                yourTotal+=9
                            elif x==sinek_8:
                                yourTotal+=8
                            elif x==sinek_7:
                                yourTotal+=7
                            elif x==sinek_6:
                                yourTotal+=6
                            elif x==sinek_5:
                                yourTotal+=5
                            elif x==sinek_4:
                                yourTotal+=4
                            elif x==sinek_3:
                                yourTotal+=3
                            elif x==sinek_2:
                                yourTotal+=2
                            Label(window1,image=x,bg="white").place(x=300,y=400)
                            Label(window1,text="Your total is {}".format(yourTotal),bg="white",font="Times 15 bold").place(x=750,y=500)
                            hit_3.destroy()
                    hit_3=Button(window1,text="HIT",font="Times 20 bold",width=10,height=2,command=hit3)
                    hit_3.place(x=250,y=750)
            hit_2=Button(window1,text="HIT",font="Times 20 bold",width=10,height=2,command=hit2)
            hit_2.place(x=250,y=750)
    hit_1=Button(window1,text="HIT",font="Times 20 bold",width=10,height=2,command=hit1)
    hit_1.place(x=250,y=750)

        
    deal1=random.choice(abc)
    if deal1==sinek_As:
        if dealerTotal<=11:
            dealerTotal+=11
        else:
            dealerTotal+=1
    elif deal1==sinek_K:
        dealerTotal+=10
    elif deal1==sinek_Q:
        dealerTotal+=10
    elif deal1==sinek_J:
        dealerTotal+=10
    elif deal1==sinek_10:
        dealerTotal+=10
    elif deal1==sinek_9:
        dealerTotal+=9
    elif deal1==sinek_8:
        dealerTotal+=8
    elif deal1==sinek_7:
        dealerTotal+=7
    elif deal1==sinek_6:
        dealerTotal+=6
    elif deal1==sinek_5:
        dealerTotal+=5
    elif deal1==sinek_4:
        dealerTotal+=4
    elif deal1==sinek_3:
        dealerTotal+=3
    elif deal1==sinek_2:
        dealerTotal+=2
    Label(window1,image=deal1,bg="white").place(x=100,y=100)

    deal2=random.choice(abc)
    if deal2==sinek_As:
        if dealerTotal<=11:
            dealerTotal+=11
        else:
            dealerTotal+=1
    elif deal2==sinek_K:
        dealerTotal+=10
    elif deal2==sinek_Q:
        dealerTotal+=10
    elif deal2==sinek_J:
        dealerTotal+=10
    elif deal2==sinek_10:
        dealerTotal+=10
    elif deal2==sinek_9:
        dealerTotal+=9
    elif deal2==sinek_8:
        dealerTotal+=8
    elif deal2==sinek_7:
        dealerTotal+=7
    elif deal2==sinek_6:
        dealerTotal+=6
    elif deal2==sinek_5:
        dealerTotal+=5
    elif deal2==sinek_4:
        dealerTotal+=4
    elif deal2==sinek_3:
        dealerTotal+=3
    elif deal2==sinek_2:
        dealerTotal+=2
    Label(window1,image=deal2,bg="white").place(x=150,y=100)

    def stay():
        nonlocal dealerTotal
        while dealerTotal<17: 
            x=random.choice(abc)
            if x==sinek_As:
                if dealerTotal<=11:
                    dealerTotal+=11
                else:
                    dealerTotal+=1
            elif x==sinek_K:
                dealerTotal+=10
            elif x==sinek_Q:
                dealerTotal+=10
            elif x==sinek_J:
                dealerTotal+=10
            elif x==sinek_10:
                dealerTotal+=10
            elif x==sinek_9:
                dealerTotal+=9
            elif x==sinek_8:
                dealerTotal+=8
            elif x==sinek_7:
                dealerTotal+=7
            elif x==sinek_6:
                dealerTotal+=6
            elif x==sinek_5:
                dealerTotal+=5
            elif x==sinek_4:
                dealerTotal+=4
            elif x==sinek_3:
                dealerTotal+=3
            elif x==sinek_2:
                dealerTotal+=2
            Label(window1,image=x,bg="white").place(x=200,y=100)
        Label(window1,text="Dealer total is {}".format(dealerTotal),bg="white",font="Times 15 bold").place(x=750,y=200)
    Button(window1,text="STAY",font="Times 20 bold",width=10,height=2,command=stay).place(x=500,y=750)

    Label(window1,text="Your total is {}".format(yourTotal),bg="white",font="Times 15 bold").place(x=750,y=500)
    Label(window1,text="Dealer total is {}".format(dealerTotal),bg="white",font="Times 15 bold").place(x=750,y=200)

    
    if yourTotal<=21 and dealerTotal<=21:
            if dealerTotal==21:
                Label(window1,text="Blackjack! Dealer win!",bg="white",font="Times 15 bold").place(x=350,y=900)
                
            elif yourTotal==21:
                Label(window1,text="Blackjack! You win!",bg="white",font="Times 15 bold").place(x=350,y=900)
                
            elif yourTotal>dealerTotal:
                Label(window1,text="Dealer lost! You win!",bg="white",font="Times 15 bold").place(x=350,y=900)
                
            elif yourTotal<dealerTotal:
                Label(window1,text="You lost! Dealer win!",bg="white",font="Times 15 bold").place(x=350,y=900)
                
    elif yourTotal>21:
        Label(window1,text="You bust! Dealer win!",bg="white",font="Times 15 bold").place(x=350,y=900)
        
    elif dealerTotal>21:
        Label(window1,text="Dealer bust! You win!",bg="white",font="Times 15 bold").place(x=350,y=900)

bas=Button(window1,text="Enter your money",font="times 15 bold",bg="green",command=money,relief=RAISED)
bas.place(x=65,y=50)
para=Entry(window1,font="times 15 bold",relief=RAISED)
para.place(x=50,y=10)


window1.mainloop()