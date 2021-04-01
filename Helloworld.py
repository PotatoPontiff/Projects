#1
Fav = input('Введите своё любимое слово: ')
print("Ваше любимое слово - ", Fav)
FavN = int(input('Ваше любимое число: '))
print(FavN ** 3)
print("Это куб вашего любимого числа")
Qst = input("Каков ответ на главный вопрос жизни, вселенной, и всего прочего? ")
print (Qst)
#2
Seconds = int(input("Введите время в секундах: "))
minutes = Seconds // 60
Seconds = Seconds % 60
hours = minutes // 60
minutes = minutes % 60
print(f"{hours} : {minutes} : {Seconds}")
#3
number = int(input("Введите число: "))
number1 = number * 11
number2 = number * 111
print(number, "+", number * 11, "+", number * 111, "=", number + number1 + number2)
#4
number = ' '.join(input('Введите число: '))
print(max(number))
#5
income = int(input("Введите доходность фирмы: "))
outcome = int(input("Введите издержки фирмы: "))
if outcome > income:
    print("У фирмы Х проблемы с доходами")
else:
    print("У фирмы Х отсутствуют проблемы с доходами")
totincome = income-outcome
workers = int(input("Введите число людей, работающих на фирму: "))
print ("На каждого работника приходится единиц чистой валюты: ", totincome / workers )
#6.
daynumber = 1
km = int(input("Спортсмен сегодня пробежал... "))
kmadd = km / 10
kmres = km

while True:

    if kmres < 4:
        print (f"На день номер {daynumber} спортсмен пробежал {kmres} км")
        daynumber = daynumber + 1
        kmres = kmres + kmadd
    else:
        print(f"Спортсмен достиг своей цели на {daynumber}-й день")
        break