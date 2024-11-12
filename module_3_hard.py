
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(x):         #создаем функцию с параметром пусть будет Х
    summa = 0                           #создаем счетчик
    if  isinstance(x, (int, float)):#isinstance проверяет параметр на принадлежность к целому числу и числу с плавающей точкой
        summa += x #простой счетчик чисел
    elif isinstance(x, str):#isinstance проверяет параметр на принадлежность к строке
        summa += len(x) #простой счетчик количества элементов в строке
    elif isinstance(x, dict):             #isinstance проверяет параметр на принадлежность к словарю
        for key, value in x.items():    #вытаскиваем из словаря ключи и значения
            summa += calculate_structure_sum(key) # после распаковки словаря ключ можно подсчитать summa+=len(key),
                                                #но воспользовались рекурсией, т.к. в этой функции есть счетчик для строки
            summa += calculate_structure_sum(value) #значение может быть чем угодно, и это что угодно пропустим
                                                    # через нашу функцию она определит это что угодно и подсчитает
    elif isinstance(x, (list, tuple, set)):#isinstance проверяет параметр на принадлежность к списку, кортежу, множеству
        for i in x: #проходим по кортежу, списку, множеству и поочередно присваиваем значения к i
            summa += calculate_structure_sum(i) # опять делаем рекурсию, т.к. например в списке может быть и список и строка, наша функция определит
    return summa # нашей программе не осталось более считать и она возвращает результат

result = calculate_structure_sum(data_structure)
print(result)