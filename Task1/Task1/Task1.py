while True: #Начинаем бесконечный цикл
    minutes = int(input("Enter a minutes, please: ")) #Ввод минут через консоль и приведение в численный тип
    hours = int(minutes/60)  #Перевод минут в часы, деление без остатка
    minutes %= 60 #Получаем колличесто минут после получения часов, остаток от деления
    print ("Time from midnight ",hours,":",minutes) #Выводим часы и минуты в консоль
    if input("Try again? ") == "no": #Проверяем желает ли пользователь повторить ввод
        break #В случае ввода ноу, прерываем бесконечный цикл