#Welcome! This code is written using procedural progrmaming language - python, and I am using modular approach.
#What this code does is described in README.md file
#Suggestions are welcomed - license specifies how you cna use the code.

import random as ran #need to select random numbers

lem_old = 0  #old lemons
lem_balance = 0 #lemon quantity
mon_balance = 30 #monetary balance
lemonades = 0 #lemonade glasses

day = -1 #evaluates to 0 -> 1 -> 2 etc.
wtr = 0 #weather -> 2.5 == good // 1.5 == bad

tot_cust = 0 #total customers
tot_balance = 0 #total balance

def valUserInput(inp):
    """Function to validate user input"""
    try:
        int(inp)
        return True
    except ValueError:
        return False

def endOfDay():
    """Function to update stats at the end of the day"""
    global lemonades
    global lem_balance
    global lem_old
    lem_old = lem_balance #updating number of old lemons: 0 to 1
    lem_balance = 0 #new day -> lemons became one day old, these are new lemons
    lemondes = 0 #remaining lemonades will go to 0
    
def bonusIncome():
    """Function to generate bonus income if applicable."""
    if ran.randint(0,1):
        temp = int(ran.randint(1, 50))
        if temp >= 1 and temp <= 10:
            print(f"You were polite to customers, they left you some tip: £{temp}")
            return temp
        elif temp >= 11 and temp <= 30:
            print(f"You have served some rich people, they left you some tip: £{temp}")
            return temp
        else:
            print(f"Someone has invested into your business, they gave you: £{temp}. Keep growing!")
            return temp
    else:
        print("You have served some greedy customers, you did not recieve any tips")
        return 0
        
def cutomerAmnt():
    """Function to generate number of customers"""
    global wtr
    global tot_cust
    daily_cust = int(wtr * 2 * ran.randint(1, 10))
    tot_cust += daily_cust
    return daily_cust

def weather():
    """Function to generate weather"""
    global wtr
    if ran.randint(0,1):
        print("\nIt is sunny today! More customers will come!")
        wtr = 2.5 #multiplyer for good weather
    else:
        print("\nIt is raining today! Less customers will come!")
        wtr = 1.5 #multiplyer for bad weather
        
def customerServe(num_of_cust):
    """Function to determine how much customers were served"""
    global lemonades
    global lemonades_used
    if num_of_cust > lemonades:
        lemonades_used = lemonades
        print(f"You managed to serve {lemonades_used} customers today. You did not have enough lemonade.")
    elif num_of_cust == lemonades: #num_of_cust == lemonades:
        print(f"You managed to serve {num_of_cust} customers today. You had just enough lemonades.")
    elif num_of_cust < lemonades:
        lemonades_used = num_of_cust
        print(f"You managed to serve {lemonades_used} customers today. You had more lemonade than needed.")
        
def buyLemons():
    """Function to buy lemons:
    input -> int() -> lem_balance ++;"""
    while True:
        print("""How many lemons do you want to buy?\n\
Please make sure the value is a multiple of 5 and between 25 and 150""")
        num_of_lemons = input().strip() #taking user input
        if valUserInput(num_of_lemons):
            num_of_lemons = int(num_of_lemons)
            if num_of_lemons % 5 == 0 and (num_of_lemons >= 25 and num_of_lemons <= 150):
            #check if number is a multiple of 5, and in 25<= x >=150
                global price #create price var
                price = int((num_of_lemons // 5)*1.5) #formula to calculate price
                global mon_balance #ref ro mon_balance var
                #check if player has enough money
                if mon_balance < price: #check if balance is less than price
                    print("Transaction was unsuccessful. You do not have enough money.\n")
                    continue
                
                else:
                    global lem_balance #ref global variable
                    global lem_old
                    mon_balance -= price #transaction
                    lem_balance += num_of_lemons #add lemons bought
                    print(f"Transaction was successful. You paid: £{price}. Come back another day.")
                    print(f"You now have {lem_balance} new lemons & {lem_old} old lemons and £{mon_balance} left")
                    break #message to the user and end of function
            else:
                print("Please follow the rules\n")
                continue
        else:
            print("Please make sure you enter a number\n")
            continue
  
def createLemonades():
    """Function to create lemonade"""
    global lem_balance
    global lem_old
    while True:      
        print("How many lemonade glasses would you like to make? 1 lemonade glasses = 5 lemons")
        print(f"Please provide a value between 5 and 50. You have {lem_balance + lem_old} lemons all together.")
        num_of_lemonades = input().strip() #taking user input      
        if valUserInput(num_of_lemonades):
            num_of_lemonades = int(num_of_lemonades)
            if (num_of_lemonades >= 5 and num_of_lemonades <= 50):
                #check if number is in 5<= x >=50
                lem_needed = num_of_lemonades * 5
                
                if (lem_balance + lem_old) < lem_needed:
                    print(f"You do not have enough lemons to make {num_of_lemonades} lemonades")
                    continue
                else:
                    global lemonades
                    total_lem = lem_balance + lem_old #sum
                    left_over = total_lem - lem_needed #left over
                    lem_balance = left_over
                    lemonades = num_of_lemonades
                    print(f"You have used {lem_needed} lemons. You now have {lemonades} lemonades. Come back another day.")
                    print(f"You now have {lem_balance} lemons left and {lemonades} lemonade glasses in total")
                    break
            else:
                print("Please follow the rules\n")
                continue
        else:
            print("Please make sure you enter a number\n")
            continue

if __name__ == "__main__":
    print(f"Welcome to the game. Please provide your nickname:")
    nickname = input()
    while True: # controls day-cycle outer loop
        
        if day == 2:
            print(f"Congradulations! You have come to an end of the game. In total you have earned £{tot_balance} and served {tot_cust} customers.")
            break
        else:
            day += 1
            
        while True: # inner loop one - asks if player wants to buy lemons
            print(f"\nWould you like to buy some lemons? You have {lem_balance + lem_old} lemons and £{mon_balance}. 5 lemons = £1.5")
            bli = input("Y/N: ").strip().upper()
            if bli == "Y":
                buyLemons()
                break #exit from this loop
            elif bli == "N":
                if lem_balance < 25:
                    print("You need to have at least 25 lemons before you can start your day.")
                    print(f"At the moment you have {lemons} lemons")
                    continue
                else:
                    print("Okay, let's continue!")
            else:
                print("Please enter Y or N only")
                continue
            
        while True: #inner loop two - asks if player wants to make lemonade
            print(f"\nWould you like to make some lemonade? You have {lem_balance + lem_old} lemons. You need at least 5 lemonades to start selling.\nOne lemonade = £2 to sell.")
            mli = input("Y/N: ").strip().upper()
            if mli == "Y":
                createLemonades()
                break #exit from this loop
            elif mli == "N":
                if lemonades < 5:
                    print("You need to have at least 5 lemonade glasses before you can start your day.")
                    continue
                else:
                    print("Okay, let's continue!")
            else:
                print("Please enter Y or N only")
                continue
        
        print(f"You are at day: {day}.")
        weather() #determine weather
        customers = cutomerAmnt() #determine number of customers
        print(f"The number of customers today is {customers}\n")
        customerServe(customers) #determine number of customers served
        bonus = bonusIncome() #determine bonus for the day
        daily_balance = bonus + lemonades_used*2 #money earned at each day
        mon_balance += daily_balance #RAM balance
        tot_balance += mon_balance #Total balance
        print(f"\nToday you have made £{daily_balance}. Your total balance is £{mon_balance}")
        endOfDay()
        print(f"You have completed day {day}!")
