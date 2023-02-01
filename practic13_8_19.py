try:
    count_people = int(input("Сколько билетов Вы хотите приобрести?:") or 0)
except ValueError:
    count_people = int(0)
finally:
    print("Спасибо за участие в конференции")  # Обработка ввода пустой сторки и сторчных символов
age_people = []
minors = []
junior = []
adults = []
price_minors = 0  # цена детского билета
price_junior = 990  # цена молодежного билета
price_adults = 1390  # цена взрослого билета
while len(age_people) < count_people:
    age_people.append(int(input("Возраст участника конференции")))  # Проводим опрос о возрасте и наполняем список заказа
else:
    print("Ваша бронь:")
for age in age_people:
    if age < 18:
        minors.append(price_minors)  # Обробатываем посетителей детского тарифа
    elif 18 < age <= 25:
        junior.append(price_junior)  # Обробатываем посетителей молодежного тарифа
    else:
        adults.append(price_adults)  # Обробатываем посетителей взрослого тарифа
        # Исходя из бронирования по возрастам формируем чек
if len(minors) > 0:
    print("  детских          "+str(len(minors)) +"шт  "+ "  цена " +  str(price_minors) + " руб")
if len(junior) > 0:
    print("  молодежных "+str( len(junior)) +"шт  "+"  цена " + str(price_junior) + " руб")
if len(adults) > 0:
    print("  взрослых       " +str( (len(adults))) +"шт  "+"  цена " + str(price_adults) + " руб")

print("Итого со скидкой 10% " + str((sum(junior) + sum(adults)) * 0.9) + "  руб" if sum(junior) + sum(
    adults) >= 2970 else "Итого:" + str(sum(junior) + sum(adults)))
# Расчет скидки  осуществляется если есть 3 оплачиваемых билета, в нашем \
# случае минимальная сумма такого короитерия это 3 билета молодежного \
# тарифа 990* 3= 2970
