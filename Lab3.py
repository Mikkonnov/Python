import time

cnt = 0   # заводим счётчик чисел                                                  
buffer = 1   # буфер чтения равен 1                                                       
divs = [] # заводим массив в котором будут храниться нужные числа

print (time.ctime())
start = time.time()

try:
    with open("/Users/mihail_konnovlist.ru/Desktop/Lab AISD/numbers 3.txt", "r") as file:  # открываем файл                            
        part = file.read(buffer)  # читаем файл по кускам по 1 символу                                 

        if not part: # если кусок отсутствует
             print("Файл пустой")

        while part:    # пока кусок не пуст                                            

            while (part < '0' or part > '9') and part != '.' and part: # пропускаем кусок если это не цифры и не точка
                part = file.read(buffer)                           

            while (part >= '0' and part <= '9') or part == '.'and part:     # Ищем целые или десятичные числа                  
                divs.append(part)
                part = file.read(buffer)
                divs == []
            if divs != []:
                if len(divs) == len(set(list(divs))):
                    cnt += 1
                    if cnt == 1:
                        print ("Такие числа:")
                        
                    print (''.join(divs))
            divs = []
        
    if cnt == 0:
        print ("Таких чисел нет")
    else:
        print ("Данных чисел:", cnt)
        
except FileNotFoundError:             # Если файл отсуствует в директории
    print("\nФайл text.txt в директории проекта не обнаружен."
          "\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")
    
print ("Время работы алгоритма =", time.time()-start, "секунд")
