import random

y=""
f=0
Zufallszahlen=[]
Ally=lambda:"a"
Betray=lambda :"b"
def Entscheidung(x,y):
    list=[x,y]
    print(Spielername[x]+" "+"and"+" "+Spielername[y]+" are in one room")
    print()
    a=random.choice(list)
    return a
def Passiv(x,z1,z2):
    if x==z1:
        return z2
    else:return z1
def Bedingung(x,y):

    if x=="a" and y=="a":
         return "A"
    elif x=="a" and y=="b":
         return "B"
    if x=="b" and y=="a":
        return "C"
    elif x=="b" and y=="b":
            return "D"
#Auswertung
def results():
    print(str(Spielername[Aktiver_Spieler1])+" "+"has:"+str(Punkte[Aktiver_Spieler1])+" "+"points")
    if Passiver_Spieler1==9:
         print()
    else:print(str(Spielername[Passiver_Spieler1]) + " " + "has:" + str(Punkte[Passiver_Spieler1]) + " " + "points")
    print(str(Spielername[Aktiver_Spieler2])+" "+"has:"+str(Punkte[Aktiver_Spieler2])+" "+"points")
    if Passiver_Spieler2==9:
         print()
    else:print(str(Spielername[Passiver_Spieler2]) + " " + "has:" + str(Punkte[Passiver_Spieler2]) + " " + "points")
def results_choice_A(a1,p1):
    if p1==9:
         print(Spielername[a1]+" chose:Ally")
    else:print(Spielername[a1]+" and "+Spielername[p1]+" chose:Ally")
def results_choice_B(a1,p1):
    if p1==9:
         print(Spielername[a1]+" chose:Betray")
    else:print(Spielername[a1]+" and "+Spielername[p1]+" chose:Betray")

def Punktevergabe(c,d):
    if Bedingung(c,d)=="A":
        Punkte[Aktiver_Spieler1]+=1
        Punkte[Passiver_Spieler1]+=1
        Punkte[Aktiver_Spieler2] += 1
        Punkte[Passiver_Spieler2] += 1
        History[Aktiver_Spieler1]=1
        History[Passiver_Spieler1]=1
        History[Passiver_Spieler2]=1
        History[Aktiver_Spieler2]=1
        results_choice_A(Aktiver_Spieler1,Passiver_Spieler1)
        results_choice_A(Aktiver_Spieler2,Passiver_Spieler2)
    elif Bedingung(c,d)=="B":
        Punkte[Aktiver_Spieler1] -= 1
        Punkte[Passiver_Spieler1] -= 1
        Punkte[Aktiver_Spieler2] += 2
        Punkte[Passiver_Spieler2] += 2
        History[Aktiver_Spieler1] = 1
        History[Passiver_Spieler1] = 1
        History[Passiver_Spieler2] = 0
        History[Aktiver_Spieler2] = 0
        results_choice_A(Aktiver_Spieler1, Passiver_Spieler1)
        results_choice_B(Aktiver_Spieler2, Passiver_Spieler2)
    elif Bedingung(c,d)=="C":
        Punkte[Aktiver_Spieler1] += 2
        Punkte[Passiver_Spieler1] += 2
        Punkte[Aktiver_Spieler2] -= 1
        Punkte[Passiver_Spieler2] -= 1
        History[Aktiver_Spieler1] = 0
        History[Passiver_Spieler1] = 0
        History[Passiver_Spieler2] = 1
        History[Aktiver_Spieler2] = 1
        results_choice_B(Aktiver_Spieler1, Passiver_Spieler1)
        results_choice_A(Aktiver_Spieler2, Passiver_Spieler2)
    elif Bedingung(c,d)=="D":
        History[Aktiver_Spieler1] = 0
        History[Passiver_Spieler1] = 0
        History[Passiver_Spieler2] = 0
        History[Aktiver_Spieler2] = 0
        results_choice_B(Aktiver_Spieler1, Passiver_Spieler1)
        results_choice_B(Aktiver_Spieler2, Passiver_Spieler2)

History=[1,1,1,1,1,1,1,1,1,1] #1=Ally 0=Betray
#Verhalten
def V_always_cooperate():
    return Ally()
def V_always_defect():
    return Betray()
Counter_per_nasty=[2]
def V_per_nasty():
    if Counter_per_nasty[-1]==2:
        Counter_per_nasty.append(1)
        return Betray()
    elif Counter_per_nasty[-1]==1:
         Counter_per_nasty.append(0)
         return Betray()
    elif Counter_per_nasty[-1]==0:
            Counter_per_nasty.append(2)
            return Ally()
Counter_spite=[0]
def V_spite():
    a=Punkte[3]
    if Punkte[3]<=a:
        Punkte[3]=a
        a = Punkte[3]
    else:Counter_spite.append(1)
    if Counter_spite[-1]==0:
        return Ally()
    else:return Betray()
def V_random():
    Liste=[0,1]
    a=random.choice(Liste)
    if a==0:
        return Betray()
    else:return Ally()
Counter_per_kind=[2]
def V_per_kind():
    if Counter_per_nasty[-1]==2:
        Counter_per_kind.append(1)
        return Ally()
    elif Counter_per_nasty[-1]==1:
         Counter_per_kind.append(0)
         return Ally()
    elif Counter_per_kind[-1]==0:
            Counter_per_kind.append(2)
            return Betray()
Counter_Tit_for_Tat=[1]
Counter_Tit_for_Tat2=[0]
def V_Tit_for_Tat():
    if Counter_Tit_for_Tat[-1]==1:
        Counter_Tit_for_Tat.append(0)
        return Ally()
    elif Counter_Tit_for_Tat2[-1]==1:
        if History[Aktiver_Spieler2]==1:
            return Ally()
        else:return Betray()
    elif Counter_Tit_for_Tat2[-1]==2:
        if History[Aktiver_Spieler1]==1:
            return Ally()
        else:return Betray()
Counter_mistrust=[1]
Counter_mistrust2=[0]
def V_mistrust():
    if Counter_mistrust[-1]==1:
        Counter_mistrust.append(0)
        return Betray()
    elif Counter_mistrust2[-1]==1:
        if History[Aktiver_Spieler2]==1:
             return Ally()
        else:return Betray()
    elif Counter_mistrust2[-1]==2:
        if History[Aktiver_Spieler1]==1:
             return Ally()
        else:return Betray()
def Your_choice():
    print("choose a or b")
    choice = input()
    while choice != "a" and choice != "b":
        print("choose a or b")
        choice = input()
    return choice


#Player
Spielername0=["Player_always_cooperate","Player_always_defect","Player_per_nasty","Player_spite","Player_random","Player_per_kind","Player_Tit_for_Tat","Your_player","Player_mistrust","Nothing"]
Spielername=["Luna","Dio","Clover ","Quark","Alice","Tenmyouji","K","Your_Player","Phi","Schaube"]
Punkte=[4,4,4,4,4,4,4,4,4,4,4]
Verhalten=[V_always_cooperate(),V_always_defect(),V_per_nasty(),V_spite(),V_random(),V_per_kind(),V_Tit_for_Tat(),Your_choice(),V_mistrust()]

while f==0: #Verteilung
    Counter_Zahlen=[0]
    Zufallszahlen = [0,1, 2, 3,4,5,6,8]
    print("Next Round")
                                    #Your turn
    Zufallszahl = random.choice(Zufallszahlen)
    Zufallszahlen.remove(Zufallszahl)
    Zufallszahl2 = random.choice(Zufallszahlen)
    Zufallszahlen.remove(Zufallszahl2)
    Aktiver_Spieler2 = Entscheidung(Zufallszahl, Zufallszahl2)
    Passiver_Spieler2 = Passiv(Aktiver_Spieler2, Zufallszahl, Zufallszahl2)
    d = Verhalten[Aktiver_Spieler2]
    Aktiver_Spieler1 = 7
    Passiver_Spieler1 = 9
    c = Your_choice()
    Punktevergabe(c,d)

    results()
                                                    #2 vs 2
    for a in range(2):
        Zufallszahl = random.choice(Zufallszahlen)
        Zufallszahlen.remove(Zufallszahl)
        Zufallszahl2 = random.choice(Zufallszahlen)
        Zufallszahlen.remove(Zufallszahl2)
        if a == 0:
            Aktiver_Spieler1 = Entscheidung(Zufallszahl, Zufallszahl2)
            if Counter_Zahlen[-1]==1:
                 Passiver_Spieler1=9
            else:Passiver_Spieler1=Passiv(Aktiver_Spieler1,Zufallszahl,Zufallszahl2)
            c=Verhalten[Aktiver_Spieler1]
            if Aktiver_Spieler1==7:
                Counter_Tit_for_Tat2.append(1)
            if Aktiver_Spieler1==9:
                Counter_mistrust2.append(1)
        else:
            Aktiver_Spieler2 = Entscheidung(Zufallszahl, Zufallszahl2)
            if Counter_Zahlen[-1]==1:
                Passiver_Spieler2=9
            else:Passiver_Spieler2=Passiv(Aktiver_Spieler2,Zufallszahl,Zufallszahl2)
            d=Verhalten[Aktiver_Spieler2]
            if Aktiver_Spieler1 == 7:
                Counter_Tit_for_Tat2.append(2)
            if Aktiver_Spieler1 == 9:
                Counter_mistrust2.append(2)

    Punktevergabe(c,d)


    results()

                                                    # 1 vs 1
    Zufallszahl = random.choice(Zufallszahlen)
    Zufallszahlen.remove(Zufallszahl)
    Zufallszahl2 = random.choice(Zufallszahlen)
    Zufallszahlen.remove(Zufallszahl2)

    Aktiver_Spieler1 = Zufallszahl
    Passiver_Spieler1 = 9
    c = Verhalten[Aktiver_Spieler1]
    if Aktiver_Spieler1 == 7:
        Counter_Tit_for_Tat2.append(1)
    if Aktiver_Spieler1 == 9:
        Counter_mistrust2.append(1)

    Aktiver_Spieler2 = Zufallszahl2
    Passiver_Spieler2 = 9
    d = Verhalten[Aktiver_Spieler2]
    if Aktiver_Spieler1 == 7:
        Counter_Tit_for_Tat2.append(2)
    if Aktiver_Spieler1 == 9:
            Counter_mistrust2.append(2)
    print(Spielername[Zufallszahl]+" and "+Spielername[Zufallszahl2]+" are in their own rooms")
    Punktevergabe(c,d)

    results()

    #Siegesbedingungen
    for a in range(9):
        if Punkte[a] >= 9:
            print(Spielername[a]+"  has won")
            f=1
            if Punkte[7]>=9:
                print("You won")
            else:print("You lost")


