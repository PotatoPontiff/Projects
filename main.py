#1
List = [1, 1.5, True, "Max", "Winnie"]
print(List)
iq = int(input(f"Введите число от 1 до {len(List)}: ")) - 1
print(type(List[iq]))
#2
n = 0
while n <= len(List):
    List[n] = List[n+1]
    n = n + 2
    if n+1 % 2 != 0:
        print(List)
        break
#3
Month = int(input("Введите месяц числом (От 1 до 12): "))
MonthD = {1 : "Зима", 2 : "Зима", 3 : "Весна", 4 : "Весна", 5 : "Весна", 6 : "Лето", 7 : "Лето", 8 : "Лето", 9 : "Осень", 10: "Осень", 11 : "Осень", 12 : "Зима. С наступающим Новым Годом!"}
print(f"Сейчас {MonthD[Month]}")
#4
Stroka = input("Введите любой текст: ")
Stroka.split()
q = len(Stroka)
y = 0
for mn in range(q):
    if len(Stroka[y]) > 10:
        print(Stroka[y[0:9]])
    else:
        print(Stroka[y])
    y = y + 1

#5
Numbers = [9, 12, 4, 11, 1, 6, 1]
Numbers.sort(reverse = True)
print(Numbers)
number = int(input("Введите число: "))
Numbers.append(number)
Numbers.sort(reverse = True)
print(f"Пользователь ввёл в список число {number}")
print(Numbers)
