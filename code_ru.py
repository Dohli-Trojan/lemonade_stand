#Добро пожаловать! Этот код написан с использованием процедурного языка программирования — Python, и я использую модульный подход.
#Что делает этот код, описано в файле README.md
#Предложения приветствуются. В лицензии указано, как вы можете использовать код.

import random as ran #поможет сделать рандом

lem_old = 0 #старые лимоны
lem_balance = 0 #количество лимонов
mon_balance = 30 #денежный баланс
лимонады = 0 #стаканы с лимонадом

day = -1 #преобразуется в 0 -> 1 -> 2 и т.д.
wtr = 0 #погода -> 2,5 == солнечно // 1,5 == дождливо

tot_cust = 0 #всего клиентов за игру
tot_balance = 0 #общий баланс за игру

def valUserInput(inp):
    """Функция проверки ввода пользователя"""
    try:
        int(inp)
        return True
    except ValueError:
        return False

def endOfDay():
    """Функция обновления статистики в конце дня"""
    global lemonades
    global lem_balance
    global lem_old
    lem_old = lem_balance #обновление количества старых лимонов -> от 0 дней до 1 день
    lem_balance = 0 # новый день -> старые лимоны обновлены выше. это новые лимоны
    lemondes = 0 #оставшихся лимонадов станет 0

def bonusIncome():
    """Функция для получения бонусного дохода, если применимо."""
    if ran.randint(0,1):
        temp = int(ran.randint(1, 50))
        if temp >= 1 and temp <= 10:
            print(f"Вы были вежливы с клиентами, они оставили вам чаевые: £{temp}")
            return temp
        elif temp >= 11 and temp <= 30:
            print(f"Вы обслуживали богатых людей, они оставили вам чаевые:: £{temp}")
            return temp
        else:
            print(f"Кто-то вложил деньги в ваш бизнес, они дали вам: £{temp}. Продолжайте расти!")
            return temp
    else:
        print("Вы обслужили жадных клиентов, чаевых не получили")
        return 0

def cutomerAmnt():
    """Функция для генерации количества клиентов"""
    global wtr
    global tot_cust
    daily_cust = int(wtr * 2 * ran.randint(1, 10))
    tot_cust += daily_cust
    return daily_cust

def weather():
    """Функция создания погоды"""
    global wtr
    if ran.randint(0,1):
        print("\nIt is sunny today! More customers will come!")
        wtr = 2.5 #множитель для хорошей погоды
    else:
        print("\nIt is raining today! Less customers will come!")
        wtr = 1.5 #множитель для плохой погоды

def customerServe(num_of_cust):
    """Функция определения количества обслуженных клиентов"""
    global lemonades
    global lemonades_used
    if num_of_cust > lemonades:
        lemonades_used = lemonades
        print(f"Сегодня вам удалось обслужить {lemonade_used} клиентов. У вас не хватило лимонада.")
    elif num_of_cust == lemonades: #num_of_cust == lemonades:
        print(f"Сегодня вам удалось обслужить {num_of_cust} клиентов. У вас было достаточно лимонада.")
    elif num_of_cust < lemonades:
        lemonades_used = num_of_cust
        print(f"Сегодня вам удалось обслужить {lemonade_used} клиентов. У вас было больше лимонада, чем нужною")

def buyLemons():
    """Функция для покупки лимонов:
     меняем тип данных ввода игрока и изменяем переменные"""
    while True:
        print("""Сколько лимонов вы хотите купить?\n\
Убедитесь, что значение кратно 5 и находится в диапазоне от 25 до 150""")
        num_of_lemons = input().strip() #ввод пользователя
        if valUserInput(num_of_lemons): #проверка ввода пользователя 
            num_of_lemons = int(num_of_lemons)
            if num_of_lemons % 5 == 0 and (num_of_lemons >= 25 and num_of_lemons <= 150):
            #проверяем, кратно ли число 5 и 25<= x >=150
                global price #создаём переменную price
                price = int((num_of_lemons // 5)*1.5) #формула для подсчёта цены
                global mon_balance #денежный баланс
                #проверка: достаточно ли у игрока денег
                if mon_balance < price: #проверка: достаточно ли денег
                    print("Транзакция не удалась. У вас недостаточно денег.\n")
                    continue
                
                else:
                    global lem_balance 
                    global lem_old
                    mon_balance -= price #транзакция
                    lem_balance += num_of_lemons #добавление лимонов в инвентарь
                    print(f"Транзакция прошла успешно. Вы заплатили: £{price}. Вернитесь в другой день.")
                    print(f"Теперь у вас осталось {lem_balance} новых лимонов & {lem_old} старых лимонов и осталось £{mon_balance}")
                    break #сообщение пользователю и завершение функции
            else:
                print("Пожалуйста, следуйте правилам.\n")
                continue
        else:
            print("Пожалуйста, убедитесь, что вы вводите числою\n")
            continue

def createLemonades():
    """Функция создания лимонада"""
    global lem_balance
    global lem_old
    while True:      
        print("Сколько стаканов лимонада вы хотите сделать? 1 стакан лимонада = 5 лимонов")
        print(f"Укажите значение от 5 до 50. Всего у вас {lem_balance + lem_old} лимонов.")
        num_of_lemonades = input().strip() #ввод игрока     
        if valUserInput(num_of_lemonades):
            num_of_lemonades = int(num_of_lemonades)
            if (num_of_lemonades >= 5 and num_of_lemonades <= 50):
                #проверяем, находится ли число в диапазоне 5<= x >=50
                lem_needed = num_of_lemonades * 5
                
                if (lem_balance + lem_old) < lem_needed:
                    print(f"У вас недостаточно лимонов, чтобы сделать {num_of_lemonade} лимонадов")
                    continue
                else:
                    global lemonades
                    total_lem = lem_balance + lem_old #сумма
                    left_over = total_lem - lem_needed #остаток
                    lem_balance = left_over
                    lemonades = num_of_lemonades
                    print(f"Вы использовали {lem_needed} лимонов. Теперь у вас есть {lemonade} стаканов лимонада. Приходите в другой день.")
                    print(f"Теперь у вас осталось {lem_balance} лимонов. Всего у вас {lemonades} стаканов с лимонадом")
                    break
            else:
                print("Пожалуйста, следуйту правилам.\n")
                continue
        else:
            print("Пожалуйста, убедитесь, что вы вводите число\n")
            continue

if __name__ == "__main__":
    print(f"Добро пожаловать в игру. Пожалуйста, укажите свой никнейм:")
    nickname = input()
    while True: # управляет дневным циклом
        
        if day == 2:
            print(f"Поздравляем! Вы подошли к концу игры. В общей сложности вы заработали £{tot_balance} и обслужили {tot_cust} клиентов.")
            break
        else:
            day += 1
            
        while True: # внутренний цикл один — спрашивает, хочет ли игрок купить лимоны
            print(f"\nХотите купить лимонов? У вас есть {lem_balance + lem_old} лимонов и £{mon_balance}. 5 лимонов = £1,5")
            bli = input("Y/N: ").strip().upper()
            if bli == "Y":
                buyLemons()
                break #выход из петли после покупки
            elif bli == "N":
                if lem_balance < 25:
                    print("Чтобы начать торговать, вам необходимо иметь как минимум 25 лимонов.")
                    print(f"На данный момент у вас есть {lemons} лимонов")
                    continue
                else:
                    print("Хорошо, продолжим!")
            else:
                print("Пожалуйста, введите только Y или N")
                continue
            
        while True: # внутренний цикл два — спрашивает, хочет ли игрок приготовить лимонад
            print(f"\nХотите приготовить лимонад? У вас есть {lem_balance + lem_old} лимонов. Чтобы начать продавать, вам нужно как минимум 5 лимонадов.\nОдин лимонад = £2 для продажи.")
            mli = input("Y/N: ").strip().upper()
            if mli == "Y":
                createLemonades()
                break #выход из петли после приготовления
            elif mli == "N":
                if lemonades < 5:
                    print("Чтобы начать торговать, вам необходимо иметь как минимум 5 стаканов лимонада.")
                    continue
                else:
                    print("Хорошо, продолжим!")
            else:
                print("Пожалуйста, введите только Y или N")
                continue
        
        print(f"День: {day}.")
        weather() #определение погоды
        customers = cutomerAmnt() #определенме кол-ва клиентов
        print(f"Количество клиентов сегодня равно {customers}\n")
        customerServe(customers) #определение количество обслуженных клиентов
        bonus = bonusIncome() #определение бонуса
        daily_balance = bonus + lemonades_used*2 ##деньги, заработанные за сегодня
        mon_balance += daily_balance 
        tot_balance += mon_balance 
        print(f"\nСегодня вы заработали £{daily_balance}. Ваш общий баланс составляет £{mon_balance}")
        endOfDay()
        print(f"Вы завершили день {day}!")
