# Задание №6
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции
# поступления и снятия средств в список.
# class BankAccount:
s = 10000
count = 0
RICHLIMIT = 5_000_000
RICHTAX = 0.9
THREEOPERATIONS = 3
BONUSTHREE = 1.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600
operations = []

def apply_rich_tax(balance):
    if balance >= RICHLIMIT:
        return balance * RICHTAX
    return balance

def apply_bonus(balance, count):
    if count % THREEOPERATIONS == 0 and count != 0:
        return balance * BONUSTHREE
    return balance

def deposit(balance, amount, count, operations):
    if amount % FREENDERING == 0:
        operations.append(f"Пополнение: +{amount} ")
        count += 1
        return balance + amount, count
    return balance, count

def withdraw(balance, amount, count, operations):
    if amount % FREENDERING == 0:
        comission = amount * COMMISSIONOUTDROW
        comission = min(MAXLIMIT, max(MINLIMIT, comission))
        if (comission + amount) <= balance:
            operations.append(f"Снятие: -{amount} (Комиссия: -{comission} )")
            count += 1
            return balance - (amount + comission), count
    return balance, count

while True:
    action = input('Введите операцию 1-пополнить,2-снять,3-список операций: ')
    
    if action == '1':
        withdrow = int(input('Введите сумму: '))
        s, count = deposit(s, withdrow, count, operations)
    elif action == '2':
        withdrow = int(input('Введите сумму: '))
        s, count = withdraw(s, withdrow, count, operations)
    else:
        break

    s = apply_rich_tax(s)
    s = apply_bonus(s, count)

    print(f"Сумма на счете: {s} ")

print("Список всех операций:")
for operation in operations:
    print(operation)
    
