import random
# <=====================RULES=========================>
def rules():
    print("=" * 40)
    print("         COMPUTER /VS/ YOU         ")
    print("=" * 40)
    print("1. ROLES: One player is the BATTER and one is the BALLER.")
    print("2. INPUT: Both players secretly choose a number from 1 to 6.")
    print("\n3. SCORING:")
    print("   • WICKET: If the numbers MATCH, the Batter is OUT.")
    print("   • RUNS:   If they DIFFER, the Batter adds their number to their score.")
    print("\n4. WINNING:")
    print("   • Both players get one innings to bat.")
    print("   • The player with the highest total score wins!")
    print("=" * 40)

# <=====================TOSS=========================>
def toss():
    print("\n\n")
    print("<-------- TOSS BEGAINS --------->")
    print("="*40)
    while True:
    # <===RANDOM_MODULE_WORK=====>
        tos={"head":1,"tail":0}
        tos_random=random.choice([1,0])


        print("CHOSE {HEAD /OR/ TAIL}")
        mt_choice=input("\nTHE CHOICE ==> ")
        t_choice=mt_choice.lower()
        if(t_choice=="head" or t_choice=="tail"):
            if(tos_random==tos[t_choice]):
                print("\n")
                print("-=-" * 40)
                print("YOU WON THE TOSS !!!!-------@@-->")
                print("-=-" * 40)
                bat_ball_c_win()
                break
            elif(tos_random!=tos[t_choice]):
                print("-=-" * 40)
                print("YOU LOST THE TOSS !!!!------##-->")
                print("-=-" * 40)
                bat_ball_c_loss()
                break
        else:
            print("\n")
            print("=" * 40)
            print(f"WRONG INPUT --> {t_choice} <--")
            print("=" * 40)
            print("\n")

# <=====================TOSS_WIN=========================>

def bat_ball_c_win():
    t_run=0
    bot_run=0

    while True:
        print("\n")
        print("=" * 40)
        print("YOU HAVE WON!! THE TOSS --->\n{ BAT / BALL }")
        b_b_c=input("\nTHE CHOICE ==> ")
        b_b_c.lower()
        if(b_b_c=="bat"):
            tra="Bat"
            print("\n\n")
            print("=" * 40)
            print(f"THE PLAYERS HAVE ENTERED AND YOU ARE [{tra}ing]")
            a=batt(t_run,bot_run)
            b=ball(t_run,bot_run)
            score_b(a,b)
            score_b_view()


                
            
        elif(b_b_c=="ball"):
            tra="Ball"
            print("\n\n")
            print("=" * 40)
            print(f"THE PLAYERS HAVE ENTERED AND YOU ARE [{tra}ing]")
            a=ball(t_run,bot_run)
            b=batt(t_run,bot_run)
            score_b(a,b)
            score_b_view()



        else:
            print(f"WRONG INPUT --> {b_b_c} <-- ")
            break

# <=====================TOSS_LOSS=========================>

def bat_ball_c_loss():
    t_run=0
    bot_run=0
    b_b_r=random.choice(["BAT","BALL"])
    print("\n")
    print("=" * 40)
    print(f"THE COMPUTER HAS WON!! THE TOSS AND HAS CHOSEN TO ==> [{b_b_r}] FIRST ")
    if(b_b_r=="BAT"):
        a=batt(t_run,bot_run)
        b=ball(t_run,bot_run)
        score_b(a,b)
        score_b_view()

    elif(b_b_r=="BALL"):
        a=ball(t_run,bot_run)
        b=batt(t_run,bot_run)
        score_b(a,b)
        score_b_view()

# <========================SCORE BOARD=======================>
def score_b(a,b):
    with open("score.txt","w") as f:
        f.write("\n===============================================\n")
        f.write("<== THE SCORE OF MATCHs.. ==> \n")
        f.write(f"THE PLAYER SCORE ==> {a}\n")
        f.write(f"THE BOT SCORE ==> {b}\n")
        f.write("================================================\n")

def score_b_view():
    choice=input("WHOULD YOU LIKE TO VIEW THE SCORE BOARD / (ENTER) TO CONTINU / (E) TO EXIT ==> ")
    a=choice.lower()
    if(a == ""):
        with open("score.txt","r") as f:
            for i in range(4):
                print(f.readline())
    elif(a == "e"):
        exit()

# <========================BAT=======================>

def batt(t_run,bot_run):
    print("\n\n")
    print("=" * 40)
    print("YOU WILL BE ASKED TO CHOSE A NUMBER BETWEEN ( 1 -> 6) ")
    print("=" * 40)
    ball=1

    while True:
        if(ball>6):
            break
        else:
            comp_bb=random.choice([1,2,3,4,5,6,7])
            run=int(input(f"\nYOU'R ON STRIKE : BALL No[{ball}] : HIT ===>  "))
            ball+=1
            if(run>6 or run<1):
                print(f"YOU MISSED THE BALL : YOU({run}) : BOT_BALL({comp_bb}) : TOTAL RUNS({t_run})")
            else:
                if(run==comp_bb):
                    print(f"[ OUT @@!!] : WICKET!!! YOU LOST A WICKET : YOU({run}) : BOT_BALL({comp_bb}) : TOTAL RUNS({t_run})")
                    break
                elif(comp_bb>6):
                    t_run+=run+1                        
                    print(f"NO BALL / WIDE : +1 : YOU({run}) : BOT_BAT({comp_bb}) : TOTAL RUNS({t_run})")
                    ball-=1
                elif(run!=comp_bb):
                    t_run+=run              
                    print(f"YOU SCORED [{run}] RUNNS!! : YOU({run}) : BOT_BALL({comp_bb}) : TOTAL RUNS({t_run})")
    return t_run                
# <========================BALL=======================>

def ball(t_run,bot_run):
    print("\n\n")
    print("=" * 40)
    print("YOU WILL BE ASKED TO CHOSE A NUMBER BETWEEN ( 1 -> 6) ")
    print("=" * 40)

    ball=1
    while True:
        if(ball>6):
            break
        else:
            comp_bat=random.choice([1,2,3,4,5,6,7,8])
            print("-"*40)
            run=int(input(f"\nYOU'R ON THE BALLING PTTCH : BALL No[{ball}] : BALL ===>  "))
            ball+=1
            print("-"*40)
            if(run>6 or run<1):
                print(f"NO BALL / WIDE : YOU({run}) : BOT_BAT({comp_bat}) : BOT RUNS({bot_run})")
                ball-=1
            else:
                if(run==comp_bat):
                    print(f"[ OUT @@!!] : WICKET!!! YOU GOT THE BOT! : YOU({run}) : BOT_BAT({comp_bat}) : BOT TOTAL({bot_run})")                
                    break
                elif(comp_bat>6):
                    print(f"BOT MISSED THE BALL : YOU({run}) : BOT_BALL({comp_bat}) : TOTAL RUNS({bot_run})")
                elif(run!=comp_bat and comp_bat<7):
                    bot_run+=comp_bat              
                    print(f" BOT SCORED [{comp_bat}] RUNS!! : YOU({run}) : BOT_BAT({comp_bat}) : BOT RUNS({bot_run})")
    return bot_run                
# <========================MAIN=======================>

print("\nWELCOME TO THE HAND CRICKET :-  { IT IS A FUN GAME }\n")
print("=" * 40)
print("\n\nTO BEGAIN PRESS {ENTER} / TO LEARN RULES PRESS {R}\n")
print("=" * 40)


while True:
    m1=input("\nYOUR CHOICE ==> ")
    m1.lower()
    if (m1==""):
        toss()
    elif(m1=="r"):
        rules()
    else:
        print("-=-" * 40)
        print(f"WRONG INPUT --> {m1} <-- ")
        print("-=-" * 40)